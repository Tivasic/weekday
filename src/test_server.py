import unittest
import server
from schemas import Data


class TestServer(unittest.TestCase):

    def test_current_day(self):
        self.assertEqual(server.current_day(), "Monday")

    def test_current_weekday(self):
        self.assertEqual(server.current_weekday(Data), "Monday")

    def test_future_date(self):
        self.assertEqual(server.future_date(0, 0), "Monday")


if __name__ == '__main__':
    unittest.main()

