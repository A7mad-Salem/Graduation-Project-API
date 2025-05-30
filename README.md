🛣️ Road Quality Prediction API (DSC-BiLSTM Model)
This repository contains a FastAPI-powered API that predicts road quality clusters using the DSC-BiLSTM deep learning model.
It also calculates the Road Quality Index (RQI) for a given geographic range based on start and end GPS coordinates.

📊 Features
✅ Predict road quality clusters:

Normal road (0)

Pothole (1)

Speedbump (2)

Bad road (3)

✅ Calculate the Road Quality Index (RQI) using the method from the W345 paper:

Considers road roughness, potholes, and speedbump classification (good/bad).

✅ Accepts start and end latitude/longitude coordinates and returns predictions for nearby points (within 500m) and the RQI.

✅ Built using:

PyTorch (for model inference)

FastAPI (for API backend)

Haversine distance calculation for geospatial filtering

🚀 API Endpoints
1️⃣ /predict_in_range (POST)
Predicts road clusters and calculates the RQI for a given geographic range.

Request Body (JSON):


json

Copy

Edit

{
  "start_lat": 31.43496067,
  "start_lon": 31.67756983,
  "end_lat": 31.45252233,
  "end_lon": 31.68269767
}

Response:

json

Copy

Edit

{
 
  "predictions": [
  
    {"Latitude": 31.45, "Longitude": 31.67, "Predicted Cluster": 0},
    
    {"Latitude": 31.46, "Longitude": 31.68, "Predicted Cluster": 2},
    
    ...
  ],
  
  "RQI": 0.812,
  
  "RQI_Quality": "Good"
}

🏗️ How to Run the API Locally
1️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Start the API server:

bash
Copy
Edit
uvicorn app:app --reload --port 5000
3️⃣ Access Swagger UI:

Open: http://127.0.0.1:5000/docs

📂 Project Structure
graphql
Copy
Edit
├── app.py              # FastAPI app with endpoints

├── utils.py            # Model loading and preprocessing utilities

├── DSC-BiLSTM_model.pth  # Trained model weights

├── train_raw_tensor.pt  # Raw input tensor

├── train_fft_tensor.pt  # FFT input tensor

├── y_train.csv          # Labels with Latitude, Longitude, Cluster

├── requirements.txt     # Python dependencies

└── README.md            # This file

📖 RQI Calculation Method
The RQI is computed as:

RQI
=
1
−
0.4
×
𝑅
𝑆
𝑅
𝑅
+
0.3
×
𝑃
𝐻
𝑅
+
0.1
×
𝐺
𝑆
𝑃
𝑅
+
0.2
×
𝐵
𝑆
𝑃
𝑅
0.4
RQI=1− 
0.4
0.4×RSRR+0.3×PHR+0.1×GSPR+0.2×BSPR
​
 
Where:

RSRR = Bad Road Rate

PHR = Pothole Rate

GSPR = Good Speedbump Rate (accY < 0.1012)

BSPR = Bad Speedbump Rate (accY ≥ 0.1012)

📬 Contact For questions or contributions, reach out via LinkedIn or email at xx.ahmadsalem.xx@gmail.com.
