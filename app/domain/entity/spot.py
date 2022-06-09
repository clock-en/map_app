from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.spot.spot_name import SpotName


@dataclass(init=False, eq=True, frozen=True)
class Spot():
    id: Id
    name: SpotName
    latitude: Latitude
    longitude: Longitude
    user_id: Id

    def __init__(
        self,
        id: Id,
        name: SpotName,
        latitude: Latitude,
        longitude: Longitude,
        user_id: Id,
    ) -> None:
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'latitude', latitude)
        object.__setattr__(self, 'longitude', longitude)
        object.__setattr__(self, 'user_id', user_id)