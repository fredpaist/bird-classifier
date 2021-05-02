import time

import numpy as np
import tensorflow.compat.v2 as tf

# Getting some unknown linter errors, disable everything to get this to production asap
import config
from app.bird_model import BirdModel
from app.service.bird_service import BirdService


class ClassifierService:
    __bird_model = BirdModel()

    def __init__(self):
        self.__bird_service = BirdService()
        self.__birds: dict = self.__bird_service.load_birds()

    def add_scores_to_birds(self, model_raw_output: np.ndarray):
        for index, value in np.ndenumerate(model_raw_output):
            bird_index = index[1]
            self.__birds[bird_index].score = value

        return self.order_birds_by_result_score(self.__birds)

    def order_birds_by_result_score(self, bird_labels: dict) -> list:
        return sorted(bird_labels.items(), key=lambda x: x[1].score)

    def get_top_three(self, birds_names_with_results_ordered: list) -> list:
        return list(map(lambda value: value[1], birds_names_with_results_ordered[3*(-1):]))

    def find_possible_bird_names(self, image: np.ndarray) -> np.ndarray:
        bird_model = self.__bird_model.model
        # Generate tensor
        image_tensor = tf.convert_to_tensor(image, dtype=tf.float32)
        image_tensor = tf.expand_dims(image_tensor, 0)
        return bird_model.call(image_tensor).numpy()

    def classify_bird(self, image_url: str, start_time):
        image = self.__bird_service.load_image(image_url)
        print('image loaded: %s' % (time.time() - start_time))

        model_raw_output = self.find_possible_bird_names(image)
        print('model call finished: %s' % (time.time() - start_time))

        birds_with_results_ordered = self.add_scores_to_birds(model_raw_output)
        print('results ordered: %s' % (time.time() - start_time))

        return self.get_top_three(birds_with_results_ordered)

    def main(self, start_time):
        print('started service: %s' % (time.time() - start_time))
        for index, image_url in enumerate(config.image_urls):
            top_three = self.classify_bird(image_url, start_time)
            # Print results to kubernetes log
            print('Run: %s' % int(index + 1))
            print('Top match: %s' % top_three[2])
            print('Second match: %s' % top_three[1])
            print('Third match: %s' % top_three[0])
            print('first run finish: %s' % (time.time() - start_time))
            print('\n')
