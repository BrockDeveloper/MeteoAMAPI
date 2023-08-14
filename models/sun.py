from models.basemodel import Base


class Sun(Base):

    sunrise: str = None
    sunset: str = None


    def from_dict(data: dict) -> "Sun":

        obj = Sun()

        obj.sunrise = data["sunrise"]
        obj.sunset = data["sunset"]

        return obj