from responses.basemodel import BaseModel
from responses.location import Location
from responses.sun import Sun
from responses.forecast import Forecast
from datetime import datetime


class Response(BaseModel):

    source: str = "www.meteoam.it"
    location: Location
    timestamp: str
    forecast: Forecast
    sun: Sun


    def from_dict(data: dict):

        return Response(
            location = Location.from_dict(data),
            timestamp = Response.__get_isodate(data["datetime"]),
            forecast = Forecast.from_dict(data),
            sun = Sun.from_dict(data)
        )
    



    def __get_isodate(textual_datetime: str) -> str:

        month_conversion = {
            "gennaio": 1,
            "febbraio": 2,
            "marzo": 3,
            "aprile": 4,
            "maggio": 5,
            "giugno": 6,
            "luglio": 7,
            "agosto": 8,
            "settembre": 9,
            "ottobre": 10,
            "novembre": 11,
            "dicembre": 12,
        }

        # split textual_datetime in date and time
        date, time = textual_datetime.split(" | ")

        # split date in day, month and year
        day, month, year = date.split(" ")

        # split time in hour and minute
        hour, minute = time.split(":")

        # convert month from textual to numeric
        month = month_conversion[month]

        # create datetime object
        dt = datetime(int(year), month, int(day), int(hour), int(minute))

        # convert datetime object to iso format with utc offset
        return dt.isoformat()