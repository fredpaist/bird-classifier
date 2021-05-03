from unittest import TestCase, mock

from app.service.bird_service import BirdService
from tests.mocking.mock_data import MOCK_BIRD_IMAGE_URL, MOCK_BIRD_1, MOCK_BIRD_2, MOCK_BIRD_3, \
    MOCK_BIRD_4, MOCK_BIRD_5

with mock.patch.object(BirdService, "load_birds") as mock_birds_load:
    mock_birds_load.return_value = [MOCK_BIRD_1, MOCK_BIRD_2, MOCK_BIRD_3, MOCK_BIRD_4]

from app.service.classifier_service import ClassifierService

BIRD_LOAD_ANSWER = {0: MOCK_BIRD_1, 1: MOCK_BIRD_2, 2: MOCK_BIRD_3, 867: MOCK_BIRD_4, 781: MOCK_BIRD_5}


@mock.patch('app.service.classifier_service.BirdService.load_birds')
class TestClassifierService(TestCase):

    def test_classify_bird(self, mock_bird_service_load):
        mock_bird_service_load.return_value = BIRD_LOAD_ANSWER

        classifier_service = ClassifierService()
        result = classifier_service.classify_bird(MOCK_BIRD_IMAGE_URL)
        self.assertEqual(result[2].id, MOCK_BIRD_4.id)
        pass
