from unittest import TestCase, mock

from app.service.bird_service import BirdService
from tests.mocking.mock_data import MOCK_BIRD_1, MOCK_BIRD_2, MOCK_BIRD_3, MOCK_BIRD_LOAD_URL


@mock.patch("app.service.bird_service.config.bird_labels_url", MOCK_BIRD_LOAD_URL)
class TestBirdService(TestCase):
    bird_service = BirdService()

    def test_load_birds(self, ):
        birds = self.bird_service.load_birds()

        self.assertEqual(birds[0].id, MOCK_BIRD_1.id)
        self.assertEqual(birds[0].name, MOCK_BIRD_1.name)
        self.assertEqual(birds[1].id, MOCK_BIRD_2.id)
        self.assertEqual(birds[1].name, MOCK_BIRD_2.name)
        self.assertEqual(birds[2].id, MOCK_BIRD_3.id)
        self.assertEqual(birds[2].name, MOCK_BIRD_3.name)
