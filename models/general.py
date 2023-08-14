from datetime import datetime
from models.basemodel import Base


COPYRIGHT = "https://www.meteoam.it"


class General(Base):

    copyright: str = COPYRIGHT
    location: str = None
    latitude: float = None
    longitude: float = None
    datetime: str = None


    def from_dict(data: dict):

        obj = General()


        obj.location = data["location"]

        coords = data["coordinates"].split(" / ")
        obj.latitude = float(coords[0].split(" ")[1].strip())
        obj.longitude = float(coords[1].split(" ")[1].strip())

        obj = General()


        obj.location = data["location"]

        coords = data["coordinates"].split(" / ")
        obj.latitude = float(coords[0].split(" ")[1].strip())
        obj.longitude = float(coords[1].split(" ")[1].strip())

        # datetime 
        obj.datetime = General.__get_isodate(data["datetime"])

        return obj
        # datetime 
        obj.datetime = self.__get_isodate(data["datetime"])

        return obj
    

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