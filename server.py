import datetime
from fastapi import FastAPI
from schemas import Calc, Data
from dictionary import weekdays


app = FastAPI()


# 1.GET-запрос, которые возвращает текущий день недели на сервере


@app.get('/')
def current_day():
    day = weekdays[datetime.datetime.today().isoweekday()]
    return day


# 2. POST-запрос, в теле которого приходит дата и возвращается день недели.


@app.post('/')
def current_weekday(item: Data):
    item.weekday = weekdays[datetime.datetime.today().isoweekday()]
    return item.weekday


# 3. Запрос, который скажет, какой день недели будет через указанное время
#    (N дней, M часов, ...) от текущей даты


@app.post('/future_date')
def future_date(numberdays, numberhrs):

    Calc.futuredate = datetime.datetime.today().now()
    numberdays = int(numberdays)
    numberhrs = int(numberhrs)

    if numberdays >= 0:
        n = datetime.timedelta(days=numberdays)
        Calc.futuredate = Calc.futuredate + n

    if numberhrs >= 0:
        m = datetime.timedelta(hours=numberhrs)
        Calc.futuredate = Calc.futuredate + m

    Calc.futuredate = weekdays[Calc.futuredate.isoweekday()]
    return Calc.futuredate
