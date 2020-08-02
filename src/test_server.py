import server
from schemas import Data


def test_day():
    assert server.current_day() == "Sunday"
