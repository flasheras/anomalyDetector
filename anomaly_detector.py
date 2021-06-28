import os
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.ai.anomalydetector.models import DetectRequest, TimeSeriesPoint, TimeGranularity, AnomalyDetectorError
from azure.core.credentials import AzureKeyCredential
import pandas as pd

SUBSCRIPTION_KEY = os.environ["ANOMALY_DETECTOR_KEY"]
ANOMALY_DETECTOR_ENDPOINT = os.environ["ANOMALY_DETECTOR_ENDPOINT"]
TIME_SERIES_DATA_PATH = os.path.join("./sample_data", "request-data.csv")

# Client that authenticates against your anomaly detector resource
client = AnomalyDetectorClient(AzureKeyCredential(SUBSCRIPTION_KEY), ANOMALY_DETECTOR_ENDPOINT)

# Empty list to store your data series
series = []

# Load data with Pandas. Uses date_parser instead of parse_dates included in doc.
data_file = pd.read_csv(TIME_SERIES_DATA_PATH, header=None, encoding='utf-8', date_parser=[0])

# Iterate dataframe and extract date and value. Insert into list
for index, row in data_file.iterrows():
    series.append(TimeSeriesPoint(timestamp=row[0], value=row[1]))

# Define the window to analyze anomalies
request = DetectRequest(series=series, granularity=TimeGranularity.daily)

# You have several options. Detect anomalies in the entire dataset with detect_entire_series, 
# or on the latest data point using detect_last_point. 
# The detect_change_point function detects points that mark changes in a trend.
print('Detecting anomalies in the entire time series.')

try:
    response = client.detect_entire_series(request)
    # Print anomalies
    if any(response.is_anomaly):
        print('An anomaly was detected at index:')
        for i, value in enumerate(response.is_anomaly):
            if value:
                print(i)
    else:
        print('No anomalies were detected in the time series.')

except Exception as e:
    print(e)
