import unittest
from temas.temas import Control

class TestControl(unittest.TestCase):
    def test_control_distance(self):
        temas = Control(port=8082)
        result = temas.distance()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
