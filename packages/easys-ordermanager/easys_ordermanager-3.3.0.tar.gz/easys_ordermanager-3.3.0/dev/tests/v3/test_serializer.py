import json
from pathlib import Path
from unittest import TestCase

from django.conf import settings

from easys_ordermanager.v3.serializer import Serializer


class SerializerV3TestCase(TestCase):
    def test_validate_data(self):
        example_path = Path(settings.BASE_DIR) / "dev" / "tests" / "v3" / "example.json"
        with example_path.open() as f:
            fixture = json.load(f)
        s = Serializer(data=fixture)
        self.assertTrue(s.is_valid(raise_exception=True))

    def test_validate_existing_stroer_lp_example(self):
        example_path = Path(settings.BASE_DIR) / "dev" / "tests" / "v3" / "existing_stroer_lp_example.json"
        with example_path.open() as file:
            fixture = json.load(file)
            serializer = Serializer(data=fixture)
            self.assertTrue(serializer.is_valid(raise_exception=True))
