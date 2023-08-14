from models.basemodel import BaseModel
from models.general import General
from models.sun import Sun
from models.temperature import Temperature
from models.wind import Wind
from models.pressure import Pressure


class Forecast(BaseModel):

    general: General = None
    temperature: Temperature = None
    wind: Wind = None
    sun: Sun = None
    pressure: Pressure = None


    def from_dict(data: dict) -> "Forecast":

        obj = Forecast()

        obj.general = General.from_dict(data)
        obj.temperature = Temperature.from_dict(data)
        obj.wind = Wind.from_dict(data)
        obj.sun = Sun.from_dict(data)
        obj.pressure = Pressure.from_dict(data)

        return obj