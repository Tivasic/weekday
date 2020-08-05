import server
from schemas import Data


def test_current_day():
    assert server.current_day() == "Wednesday"


def test_current_weekday():
    assert server.current_weekday(Data) == "Wednesday"


def test_future_date():
    assert server.future_date(0, 0) == "Wednesday"




