import unittest
from funny_app.py import generate_random_joke

class TestJokeGeneration(unittest.TestCase):
    def test_generated_joke(self):
        # Ensure the generated joke is not empty
        joke = generate_random_joke()
        self.assertTrue(joke, "Generated joke should not be empty")

if __name__ == '__main__':
    unittest.main()
