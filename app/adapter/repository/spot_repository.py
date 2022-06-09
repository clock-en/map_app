from app.infrastructure.dao.spot_dao import SpotDao
from app.domain.entity.spot import Spot
from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.spot.spot_name import SpotName
from app.domain.value_object.spot.new_spot import NewSpot


class SpotRepository(object):
    __spot_dao: SpotDao

    def __init__(self) -> None:
        self.__spot_dao = SpotDao()

    def create(self, new_spot: NewSpot):
        db_spot = self.__spot_dao.create_spot(new_spot)
        return Spot(
            id=Id(db_spot.id),
            name=SpotName(db_spot.name),
            latitude=Latitude(db_spot.latitude),
            longitude=Longitude(db_spot.longitude),
            user_id=Id(db_spot.user_id)
        )