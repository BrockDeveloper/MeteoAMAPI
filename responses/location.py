from responses.basemodel import BaseModel


class Location(BaseModel):

    name: str
    latitude: float
    longitude: float


    def from_dict(data: dict):

        coords = data["coordinates"].split(" / ")
        latitude = float(coords[0].split(" ")[1].strip())
        longitude = float(coords[1].split(" ")[1].strip())

        return Location(
            name = data["location"],
            latitude = latitude,
            longitude = longitude
        )