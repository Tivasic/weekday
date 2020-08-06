from datetime import datetime

from pydantic import BaseModel


class Data(BaseModel):
    date: datetime
    weekday: str
    futuredate: str


