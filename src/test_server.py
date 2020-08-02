import unittest
import server
from schemas import Data


class TestServer(unittest.TestCase):

    def test_current_day(self):
        self.assertEqual(server.current_day(), "Sunday")

    def test_current_weekday(self):
        self.assertEqual(server.current_weekday(Data), "Sunday")

    def test_future_date(self):
        self.assertEqual(server.future_date(0, 0), "Sunday")


if __name__ == "__main__":
    unittest.main()
