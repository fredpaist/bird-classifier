import logging
import time
from urllib.error import HTTPError

import numpy as np
import tensorflow.compat.v2 as tf

import config
from app.bird_model import BirdModel
from app.service.bird_service import BirdService


class ClassifierService:
    __bird_model = BirdModel()
    __log = logging.getLogger()

    def __init__(self):
        self.__bird_service = BirdService()
        self.__birds: dict = self.__bird_service.load_birds()

    def add_scores_to_birds(self, model_raw_output: np.ndarray):
        for index, value in np.ndenumerate(model_raw_output):
            bird_index = index[1]
            if bird_index in self.__birds:
                self.__birds[bird_index].score = value
            else:
                self.__log.debug("Bird with index %s not found from labels" % bird_index)

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

    def classify_bird(self, image_url: str) -> list:
        self.__log.info('Loading image %s' % image_url)
        try:
            image = self.__bird_service.load_image(image_url)
        except HTTPError as e:
            self.__log.error('Server couldn\'t fulfill the request. For url:' + image_url)
            return []

        self.__log.info('Find possible bird names')
        model_raw_output = self.find_possible_bird_names(image)
        self.__log.info('Order birds by score')
        birds_with_results_ordered = self.add_scores_to_birds(model_raw_output)
        self.__log.info('Get top three possible answers')
        return self.get_top_three(birds_with_results_ordered)

    def classify_sample_images(self, start_time):
        for index, image_url in enumerate(config.image_urls):
            top_three = self.classify_bird(image_url)
            print('Run: %s' % int(index + 1), image_url)
            print('Top match: %s' % top_three[2])
            print('Second match: %s' % top_three[1])
            print('Third match: %s' % top_three[0])
            print('Run finish: %s' % (time.time() - start_time))
            print('\n')
