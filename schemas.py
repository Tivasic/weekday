from pydantic import BaseModel
from datetime import datetime


class Data(BaseModel):
    date: datetime
    weekday: str


class Calc(BaseModel):
    futuredate: str
