import unittest
from app.models import Source

class SourcesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.new_source = Source("1234","The New York Times")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))