import torch
import torch.nn.functional as F
import torch.nn as nn

class _SepConv1d(nn.Module):
    def __init__(self, ni, no, kernel, stride, pad):
        super().__init__()
        self.depthwise = nn.Conv1d(ni, ni, kernel_size=kernel, stride=stride, padding=pad, groups=ni)
        self.pointwise = nn.Conv1d(ni, no, kernel_size=1)

    def forward(self, x):
        return self.pointwise(self.depthwise(x))

class SepConv1d(nn.Module):
    def __init__(self, ni, no, kernel, stride, pad, drop=None,
                 activ=lambda: nn.ReLU(inplace=True)):
        super().__init__()
        layers = [_SepConv1d(ni, no, kernel, stride, pad)]
        if activ: layers.append(activ())
        if drop is not None: layers.append(nn.Dropout(drop))
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        return self.layers(x)

class Flatten(nn.Module):
    def __init__(self, keep_batch_dim=True):
        super().__init__()
        self.keep_batch_dim = keep_batch_dim

    def forward(self, x):
        if self.keep_batch_dim:
            return x.view(x.size(0), -1)
        return x.view(-1)

class Classifier(nn.Module):
    def __init__(self, raw_ni, fft_ni, no, drop=0.3):
        super().__init__()
        self.lstm = nn.LSTM(input_size=35, hidden_size=64, num_layers=2,
                            batch_first=True, bidirectional=True, dropout=drop)
        self.classifier = nn.Sequential(
            nn.Linear(64, 64),
            nn.ReLU(inplace=True),
            nn.Dropout(drop)
        )
        self.raw = nn.Sequential(
            SepConv1d(raw_ni, 64, 10, 2, 3, drop=drop),
            SepConv1d(64, 128, 3, 4, 2, drop=drop),
            SepConv1d(128, 256, 3, 4, 2, drop=drop),
            SepConv1d(256, 512, 3, 4, 2),
            Flatten(),
            nn.Linear(1024, 64),
            nn.ReLU(inplace=True),
            nn.Dropout(drop),
            nn.Linear(64, 64),
            nn.ReLU(inplace=True)
        )
        self.out = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(inplace=True),
            nn.Dropout(drop),
            nn.Linear(64, no)
        )

    def forward(self, t_raw, t_fft):
        raw_out = self.raw(t_raw)
        self.lstm.flatten_parameters()
        _, (hidden, _) = self.lstm(t_fft)
        fft_out = hidden[-1]
        fft_out = self.classifier(fft_out)
        t_in = torch.cat([raw_out, fft_out], dim=1)
        return self.out(t_in)
