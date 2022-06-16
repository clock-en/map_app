from pydantic import BaseModel, Field, validator
from app.domain.value_object.spot.spot_name import SpotName
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from app.domain.value_object.id import Id
from . import validators


class SpotBase(BaseModel):
    name: str = Field(max_length=SpotName.MAX_LENGTH, example='東京駅')
    latitude: float = Field(example=35.68142354732969)
    longitude: float = Field(example=139.76709261114823)
    user_id: int = Field(example=1)

    @validator('name')
    def valid_name(cls, v):
        label = 'スポット名'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v, max=SpotName.MAX_LENGTH)
        return v

    @validator('latitude')
    def valid_latitude(cls, v):
        label = '緯度'
        validators.not_blank(label, v)
        validators.valid_number_value(
            label=label,
            value=v,
            min=Latitude.MIN_VALUE,
            max=Latitude.MAX_VALUE
        )
        return v

    @validator('longitude')
    def valid_longitude(cls, v):
        label = '経度'
        validators.not_blank(label, v)
        validators.valid_number_value(
            label=label,
            value=v,
            min=Longitude.MIN_VALUE,
            max=Longitude.MAX_VALUE
        )
        return v

    @validator('user_id')
    def valid_user_id(cls, v):
        label = 'ユーザーID'
        validators.not_blank(label, v)
        validators.valid_number_value(label=label, value=v, min=Id.MIN_VALUE)
        return v


class SpotCreate(SpotBase):
    pass


class Spot(SpotBase):
    id: int = Field(example=1)

    class Config:
        orm_mode = True
