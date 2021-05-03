import tensorflow_hub as hub
from tensorflow_hub import KerasLayer

import config


# Wrapper class for tensorflow bird classifier model
class BirdModel:
    __model = hub.KerasLayer(config.bird_model_url, signature="image_classifier", output_key="logits")

    @property
    def model(self) -> KerasLayer:
        return self.__model
