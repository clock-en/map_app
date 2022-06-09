from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.spot.spot_name import SpotName
from app.infrastructure.dao.spot_dao import SpotDao


class SpotQueryService(object):
    __spot_dao: SpotDao

    def __init__(self) -> None:
        self.__spot_dao = SpotDao()

    def fetch_all_spots(self):
        return self.__spot_dao.get_all_spots()

    def find_by_id(self, id: Id):
        return self.__spot_dao.get_spot_by_id(id)

    def fetch_registered_spot(
        self,
        name: SpotName,
        latitude: Latitude,
        longitude: Longitude
    ):
        return self.__spot_dao.get_registered_spot(name, latitude, longitude)
