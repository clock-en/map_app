from sqlalchemy import or_, and_
from app.core.sqlalchemy.data_model.spot_data_model import SpotDataModel
from app.domain.value_object.id import Id
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.spot.spot_description import SpotDescription
from app.domain.value_object.spot.spot_name import SpotName
from app.domain.value_object.spot.new_spot import NewSpot
from .dao import Dao


class SpotDao(Dao):
    def get_all_spots(self):
        return self.db.query(SpotDataModel).all()

    def get_spot_by_id(self, id: Id):
        return self.db.query(SpotDataModel).filter(
            SpotDataModel.id == id.value
        ).first()

    def get_spot_by_user_id(self, user_id: Id):
        return self.db.query(SpotDataModel).filter(
            SpotDataModel.user_id == user_id.value
        ).all()

    def get_registered_spots(
            self, name: SpotName, latitude: Latitude, longitude: Longitude):
        spot_condition = self.__set_spot_condition(
            latitude.value, longitude.value)
        return self.db.query(SpotDataModel).filter(
            or_(SpotDataModel.name == name.value, spot_condition)
        ).all()

    def get_registered_spot_by_ids(
            self, id: Id, user_id: Id):
        return self.db.query(SpotDataModel).filter(
            and_(SpotDataModel.id == id.value,
                 SpotDataModel.user_id == user_id.value)
        ).first()

    def create_spot(self, spot: NewSpot):
        new_spot = SpotDataModel(
            name=spot.name.value,
            description=spot.description.value,
            latitude=spot.latitude.value,
            longitude=spot.longitude.value,
            user_id=spot.user_id.value
        )
        self.db.add(new_spot)
        self.db.commit()
        self.db.refresh(new_spot)
        return new_spot

    def modify_spot(
        self,
        id: Id,
        name: SpotName,
        description: SpotDescription,
        latitude: Latitude,
        longitude: Longitude
    ):
        spot = self.db.query(SpotDataModel).filter(
            SpotDataModel.id == id.value).first()
        spot.name = name.value
        spot.description = description.value
        spot.latitude = latitude.value
        spot.longitude = longitude.value
        self.db.commit()
        return spot

    def __set_spot_condition(self, latitude: float, longitude: float):
        return and_(
            SpotDataModel.latitude == latitude,
            SpotDataModel.longitude == longitude
        )
