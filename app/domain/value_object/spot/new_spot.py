from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.spot.spot_name import SpotName


@dataclass(init=False, eq=True, frozen=True)
class NewSpot():

    name: SpotName
    latitude: Latitude
    longitude: Longitude
    user_id: Id

    def __init__(
        self,
        name: str,
        latitude: float,
        longitude: float,
        user_id: int,
    ) -> None:
        object.__setattr__(self, 'name', SpotName(name))
        object.__setattr__(self, 'latitude', Latitude(latitude))
        object.__setattr__(self, 'longitude', Longitude(longitude))
        object.__setattr__(self, 'user_id', Id(user_id))
