import urllib.request

import cv2
import numpy as np

import config
from app.model.bird import Bird


class BirdService:

    def load_birds(self) -> dict:
        bird_labels_raw = urllib.request.urlopen(config.bird_labels_url)
        bird_labels_lines = bird_labels_raw.read().splitlines()
        # bird_labels_lines = [line.decode('utf-8').replace('\n', '') for line in bird_labels_raw.readlines()]
        bird_labels_lines.pop(0)  # remove header (id, name)
        birds = {}
        for bird_line in bird_labels_lines:
            decoded_bird = bird_line.decode('utf-8')
            bird_id = int(decoded_bird.split(',')[0])
            bird_name = decoded_bird.split(',')[1]
            birds[bird_id] = Bird(bird_id, bird_name)

        return birds

    def load_image(self, image_url: str) -> np.ndarray:
        image_get_response = urllib.request.urlopen(image_url)
        image_array = np.asarray(bytearray(image_get_response.read()), dtype=np.uint8)

        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (224, 224))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image / 255
