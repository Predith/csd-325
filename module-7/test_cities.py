
import unittest
from city_functions import location

# Test case class
class TestLocation(unittest.TestCase):

    def test_city_country_population(self):
        result = location("Santiago", "Chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")

# Run the test
if __name__ == '__main__':
    unittest.main()
