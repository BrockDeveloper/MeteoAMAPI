from models.basemodel import Base


class Temperature(Base):

    current: float = None
    minimum: float = None
    maximum: float = None
    humidity: float = None
    unit: str = "Celsius degrees"


    def from_dict(data: dict) -> "Temperature":

        obj = Temperature()

        obj.current = float(data["temperature"].replace("°", ""))
        obj.minimum = float(data["temperature_min"].replace("°", ""))
        obj.maximum = float(data["temperature_max"].replace("°", ""))
        obj.humidity = float(data["humidity"].replace("%", ""))/100

        return obj