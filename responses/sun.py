from responses.basemodel import BaseModel


class Sun(BaseModel):

    sunrise: str
    sunset: str


    def from_dict(data: dict):

        return Sun(
            sunrise = data["sunrise"],
            sunset = data["sunset"]
        )