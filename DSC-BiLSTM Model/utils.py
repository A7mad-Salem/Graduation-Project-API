import torch
import pandas as pd
from model import Classifier

def load_model_and_data():
    raw_arr = torch.load("train_raw_tensor.pt")
    fft_arr = torch.load("train_fft_tensor.pt")
    df_y = pd.read_csv("y_train.csv")

    labels = df_y['Manual Cluster'].values
    latitudes = df_y['Latitude'].values
    longitudes = df_y['Longitude'].values

    raw_feat = raw_arr.shape[1]
    fft_feat = fft_arr.shape[1]
    num_classes = len(set(labels))

    model = Classifier(raw_feat, fft_feat, num_classes)
    model.load_state_dict(torch.load("best.pth", map_location='cpu'))
    model.eval()

    return model, raw_arr, fft_arr, latitudes, longitudes
