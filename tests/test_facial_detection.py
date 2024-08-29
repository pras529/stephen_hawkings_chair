import unittest
from src.hardware.facial_detection import detect_facial_movement

class TestFacialDetection(unittest.TestCase):
    def test_facial_detection(self):
        # Since the function runs an infinite loop, this is a basic placeholder test
        self.assertTrue(callable(detect_facial_movement))

if __name__ == "__main__":
    unittest.main()
