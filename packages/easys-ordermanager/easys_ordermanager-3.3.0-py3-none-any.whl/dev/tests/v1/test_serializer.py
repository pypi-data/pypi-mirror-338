import json
from pathlib import Path
from unittest import TestCase

from django.conf import settings

from easys_ordermanager.v1.serializer import Serializer


class SerializerV1TestCase(TestCase):
    def setUp(self):
        example_path = Path(settings.BASE_DIR) / "dev" / "tests" / "v1" / "example.json"
        with example_path.open() as f:
            self.fixture = json.load(f)

    def test_validate_data(self):
        s = Serializer(data=self.fixture)
        self.assertTrue(s.is_valid(raise_exception=True))
