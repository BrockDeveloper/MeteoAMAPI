from responses.basemodel import BaseModel


class Temperature(BaseModel):

    current: float
    min: float
    max: float


    def from_dict(data: dict):

        return Temperature(
            current = float(data["temperature"].replace("°", "")),
            min = float(data["temperature_min"].replace("°", "")),
            max = float(data["temperature_max"].replace("°", ""))
        )