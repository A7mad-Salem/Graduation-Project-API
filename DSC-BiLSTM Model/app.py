from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import load_model_and_data
import torch.nn.functional as F
import torch
import warnings
import requests
import pandas as pd
from fastapi.responses import JSONResponse
warnings.filterwarnings("ignore", category=FutureWarning)


app = FastAPI()

model, raw_arr, fft_arr, latitudes, longitudes = load_model_and_data()
df_y = pd.read_csv("y_train.csv")

class RangeRequest(BaseModel):
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float

@app.post("/predict_in_range")
def predict_in_range(request: RangeRequest):
    try:
        # Step 1: Get start and end from request
        start_lat, start_lon = request.start_lat, request.start_lon
        end_lat, end_lon = request.end_lat, request.end_lon

        # Step 2: Calculate bounding box (handle reverse coords too)
        min_lat, max_lat = sorted([start_lat, end_lat])
        min_lon, max_lon = sorted([start_lon, end_lon])

        # Step 3: Filter all rows within bounding box
        mask = (
            (df_y['Latitude'] >= min_lat) & (df_y['Latitude'] <= max_lat) &
            (df_y['Longitude'] >= min_lon) & (df_y['Longitude'] <= max_lon)
        )
        filtered_df = df_y[mask]

        if filtered_df.empty:
            return {"message": "No data found in the specified range."}

        # Step 4: Get indices of filtered rows
        filtered_indices = filtered_df.index.tolist()

        # Step 5: Predict using model on those indices
        with torch.no_grad():
            raw_data = raw_arr[filtered_indices].to('cpu')
            fft_data = fft_arr[filtered_indices].to('cpu')
            outputs = model(raw_data, fft_data)
            predictions = torch.argmax(outputs, dim=1).cpu().tolist()

        # Step 6: Attach predictions to corresponding rows
        result = []
        for idx, pred in zip(filtered_indices, predictions):
            row = df_y.loc[idx]
            result.append({
                "Latitude": row["Latitude"],
                "Longitude": row["Longitude"],
                "Predicted Cluster": int(pred)
            })

        return {"predictions": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


  
#uvicorn app:app --reload --port 5000
# To run the server, use the command above in your terminal.
# You can then send a POST request to the /predict_in_range endpoint with the required parameters.
# Example request body:
# {
 # "start_lat": 31.43496067,
 # "start_lon": 31.67756983,
 # "end_lat": 31.45252233,
 # "end_lon": 31.68269767
#}
# This will return the predictions for the specified range of latitudes and longitudes. 