# BirdClassifier
Sample application to find the bird name from image by using the sample model provided by Tensorflow.  

The model: The sample model is taken from Tensorflow Hub:
https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1

The labels for model outputs can be found here:
https://www.gstatic.com/aihub/tfhub/labelmaps/aiy_birds_V1_labelmap.csv

The model has been verified to run with TensorFlow 2.

Bird images used
```
https://upload.wikimedia.org/wikipedia/commons/c/c8/Phalacrocorax_varius_-Waikawa%2C_Marlborough%2C_New_Zealand-8.jpg,
https://quiz.natureid.no/bird/db_media/eBook/679edc606d9a363f775dabf0497d31de8c3d7060.jpg,
https://upload.wikimedia.org/wikipedia/commons/8/81/Eumomota_superciliosa.jpg,
https://i.pinimg.com/originals/f3/fb/92/f3fb92afce5ddff09a7370d90d021225.jpg,
https://cdn.britannica.com/77/189277-004-0A3BC3D4.jpg
```

## Setup
1) Install Python 3
2) Install requirements `pip install -r requirements.txt`
3) Run the code `python main.py`

## Requirements
| Requirement | Version |
| --- | --- |
| `tensorflow` | 2.5.0rc0 |
| `tensorflow_hub` | 0.11.0 |
| `opencv-python` | 4.5.1.48 |
| `numpy` | 1.19.3 |
