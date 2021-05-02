import time
from unittest import TestCase, mock

from app.service.bird_service import BirdService
from tests.mocking.mock_data import MOCK_BIRD_IMAGE_URL, MOCK_BIRD_1, MOCK_BIRD_2, MOCK_BIRD_3, \
    MOCK_BIRD_4, MOCK_BIRD_5

with mock.patch.object(BirdService, "load_birds") as mock_birds_load:
    mock_birds_load.return_value = [MOCK_BIRD_1, MOCK_BIRD_2, MOCK_BIRD_3, MOCK_BIRD_4]


from app.service.classifier_service import ClassifierService


@mock.patch('app.service.classifier_service.BirdService')
class TestClassifierService(TestCase):

    def test_classify_bird(self, mock_bird_service):
        mock_bird_service.load_birds.return_value = {0: MOCK_BIRD_1, 1: MOCK_BIRD_2, 2: MOCK_BIRD_3, 3: MOCK_BIRD_4, 4: MOCK_BIRD_5}

        classifier_service = ClassifierService()
        classifier_service.classify_bird(MOCK_BIRD_IMAGE_URL, time.time())
        pass
