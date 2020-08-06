import server
import datetime

import pytest

from schemas import Data
from dictionary import weekdays


class Test_weekday:

    def test_current_day(self):
        assert server.current_day() == weekdays[datetime.datetime.today().isoweekday()]

    def test_current_weekday(self):
        assert server.current_weekday(self) == weekdays[datetime.datetime.today().isoweekday()]

    def test_future_date(self):
        assert server.future_date(1, 10) == Data.futuredate


if __name__ == "__main__":
    pytest.main()
