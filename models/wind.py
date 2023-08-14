from models.basemodel import Base


class Speed(Base):
    
    value: float = None
    unit: str = "km/h"


    def from_dict(data: dict) -> "Speed":

        obj = Speed()

        obj.value = float(data["wind"].split(" ")[0])

        return obj


class Direction(Base):
        
    value: int = None
    unit: str = "degrees"


    def from_dict(data: dict) -> "Direction":

        obj = Direction()

        obj.value = int(data["wind"].split(" ")[3].replace("°", ""))

        return obj


class Wind(Base):

    speed: Speed = None
    direction: Direction = None


    def from_dict(data: dict) -> "Wind":

        obj = Wind()

        obj.speed = Speed.from_dict(data)
        obj.direction = Direction.from_dict(data)

        return obj