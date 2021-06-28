# anomalyDetector
This repository uses pyenv: more info 

To use anomaly detector you need an <a href="https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesAnomalyDetector">Azure Anomaly Detector Resource</a>

When your resource is deployed you will need the anomaly detector key and endpoint. Export both as environment variables (in UNIX):
<ul>
<li>export ANOMALY_DETECTOR_KEY=replace-with-your-anomaly-detector-key</li>
<li>export ANOMALY_DETECTOR_ENDPOINT=replace-with-your-anomaly-detector-endpoint</li>
</ul>

The directory ./sample_data contains a file named request-data.csv that is used in anomaly_detector.py to detect univariate anomalies inside data.

Code inside anomaly_detector.py is self documented.

This .py requires python 3.X, Pandas and azure-ai-anomalydetector libraries installed.

pip install pandas
pip install --upgrade azure-ai-anomalydetector