from responses.basemodel import BaseModel
from responses.temperature import Temperature
from responses.wind import Wind

class Forecast(BaseModel):

    text: str
    pressure: float
    wind: Wind
    temperature: Temperature
    humidity: float


    def from_dict(data: dict):

        text = "Unkonwn [to be implemented]"
        humidity = float(data["humidity"].replace("%", ""))/100
        pressure = int(data["pressure"].split(" ")[0])

        return Forecast(
            text = text,
            pressure = pressure,
            wind = Wind.from_dict(data),
            temperature = Temperature.from_dict(data),
            humidity = humidity
        )