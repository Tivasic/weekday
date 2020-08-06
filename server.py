import datetime

from fastapi import FastAPI

from schemas import Data
from dictionary import weekdays

app = FastAPI()


# 1.GET-запрос, которые возвращает текущий день недели на сервере.

@app.get('/')
def current_day():
    # Получает текущий день недели.
    day = weekdays[datetime.datetime.today().isoweekday()]
    return day


# 2. POST-запрос, в теле которого приходит дата
# и возвращается день недели.

@app.post('/')
def current_weekday(item: Data):
    # Отправляет на сервер текущую дату и
    # возвращает день недели.
    item.weekday = weekdays[datetime.datetime.today().isoweekday()]
    return item.weekday


# 3. Запрос, который скажет, какой день недели будет через указанное
# время (N дней, M часов, ...) от текущей даты.

@app.post('/future_date')
def future_date(numberdays, numberhrs):
    # Отправляет на сервер указанные дни и часы
    # и возвращает день недели через указанное время.
    Data.futuredate = datetime.datetime.today().now()
    numberdays = int(numberdays)
    numberhrs = int(numberhrs)

    if numberdays >= 0:
        n = datetime.timedelta(days=numberdays)
        Data.futuredate = Data.futuredate + n

    if numberhrs >= 0:
        m = datetime.timedelta(hours=numberhrs)
        Data.futuredate = Data.futuredate + m

    Data.futuredate = weekdays[Data.futuredate.isoweekday()]
    return Data.futuredate
