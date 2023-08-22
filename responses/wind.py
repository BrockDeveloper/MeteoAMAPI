from responses.basemodel import BaseModel


class Wind(BaseModel):

    speed: float
    direction: float


    def from_dict(data: dict):

        return Wind(
            speed = float(data["wind"].split(" ")[0]),
            direction= int(data["wind"].split(" ")[3].replace("°", ""))
        )