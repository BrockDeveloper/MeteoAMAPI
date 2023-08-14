from models.basemodel import Base


class Pressure(Base):

    value: int = None
    unit: str = "hPa"


    def from_dict(data: dict) -> "Pressure":

        obj = Pressure()

        obj.value = int(data["pressure"].split(" ")[0])

        return obj