from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.spot.spot_name import SpotName
from app.domain.value_object.spot.spot_description import SpotDescription


@dataclass(init=False, eq=True, frozen=True)
class Spot():
    id: Id
    name: SpotName
    description: SpotDescription
    latitude: Latitude
    longitude: Longitude
    user_id: Id
    created_at: JaDatetime
    updated_at: JaDatetime

    def __init__(
        self,
        id: Id,
        name: SpotName,
        description: SpotDescription,
        latitude: Latitude,
        longitude: Longitude,
        user_id: Id,
        created_at: JaDatetime,
        updated_at: JaDatetime,
    ) -> None:
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'description', description)
        object.__setattr__(self, 'latitude', latitude)
        object.__setattr__(self, 'longitude', longitude)
        object.__setattr__(self, 'user_id', user_id)
        object.__setattr__(self, 'created_at', created_at)
        object.__setattr__(self, 'updated_at', updated_at)
