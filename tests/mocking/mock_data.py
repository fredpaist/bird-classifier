import os

from app.model.bird import Bird

MOCK_BIRD_LOAD_URL = "file:\\" + os.path.abspath("mocking/mock_data.csv")

MOCK_BIRD_1 = Bird(0, "Haemorhous cassinii")
MOCK_BIRD_2 = Bird(1, "Aramus guarauna")
MOCK_BIRD_3 = Bird(2, "Rupornis magnirostris")
MOCK_BIRD_4 = Bird(3, "Corvus brachyrhynchos")
MOCK_BIRD_5 = Bird(4, "Sturnus vulgaris vulgaris")

MOCK_BIRD_IMAGE_URL = "file:\\" + os.path.abspath("mocking/mock_image.jpg")


def get_mock_birds_list():
    return [MOCK_BIRD_1, MOCK_BIRD_2, MOCK_BIRD_3, MOCK_BIRD_4, MOCK_BIRD_5]

