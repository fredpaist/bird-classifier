# setup
1) Install Python 3
2) Install requirements `pip install -r requirements.txt`
3) Run the code `python main.py

\* The model:
The sample model is taken from Tensorflow Hub:
https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1

The labels for model outputs can be found here:
https://www.gstatic.com/aihub/tfhub/labelmaps/aiy_birds_V1_labelmap.csv

The model has been verified to run with TensorFlow 2.

\** Production: The code was deployed as a python service using Docker with Kubernetes for the infrastructure layer.

