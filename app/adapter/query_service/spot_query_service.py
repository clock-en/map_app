from typing import List, Union
from app.core.sqlalchemy.data_model.spot_data_model import SpotDataModel
from app.domain.entity.spot import Spot
from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.spot.spot_name import SpotName
from app.domain.value_object.spot.spot_description import SpotDescription
from app.infrastructure.dao.spot_dao import SpotDao


class SpotQueryService(object):
    __spot_dao: SpotDao

    def __init__(self) -> None:
        self.__spot_dao = SpotDao()

    def fetch_all_spots(self) -> Union[Spot, None]:
        return self.__create_spot_list(self.__spot_dao.get_all_spots())

    def fetch_spots_by_user_id(self, user_id: Id) -> Union[List[Spot], None]:
        return self.__create_spot_list(
            self.__spot_dao.get_spots_by_user_id(user_id))

    def fetch_spot_by_id(self, id: Id) -> Union[Spot, None]:
        return self.__create_spot_with_comment_entity(
            self.__spot_dao.get_spot_by_id(id))

    def fetch_registered_spots(
        self,
        name: SpotName,
        latitude: Latitude,
        longitude: Longitude
    ) -> Union[List[Spot], None]:
        return self.__create_spot_list(
            self.__spot_dao.get_registered_spots(name, latitude, longitude)
        )

    def fetch_my_registered_spot_by_ids(
        self,
        id: Id,
        user_id: Id,
    ) -> Union[Spot, None]:
        return self.__create_spot_entity(
            self.__spot_dao.get_registered_spot_by_ids(id, user_id)
        )

    def __create_spot_list(self, db_spots: List[SpotDataModel]) -> List[Spot]:
        return list(map(self.__create_spot_entity, db_spots))

    def __create_spot_entity(
        self,
        db_spot: Union[SpotDataModel, None]
    ) -> Union[Spot, None]:
        if db_spot is None:
            return None
        return Spot(
            id=Id(db_spot.id),
            name=SpotName(db_spot.name),
            description=SpotDescription(db_spot.description),
            latitude=Latitude(db_spot.latitude),
            longitude=Longitude(db_spot.longitude),
            user_id=Id(db_spot.user_id),
            created_at=JaDatetime(db_spot.created_at),
            updated_at=JaDatetime(db_spot.updated_at),
        )

    def __create_spot_with_comment_entity(
        self,
        db_spot: Union[SpotDataModel, None]
    ) -> Union[Spot, None]:
        if db_spot is None:
            return None
        return Spot(
            id=Id(db_spot.id),
            name=SpotName(db_spot.name),
            description=SpotDescription(db_spot.description),
            latitude=Latitude(db_spot.latitude),
            longitude=Longitude(db_spot.longitude),
            user_id=Id(db_spot.user_id),
            created_at=JaDatetime(db_spot.created_at),
            updated_at=JaDatetime(db_spot.updated_at),
        )
