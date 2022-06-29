from typing import Union, List
from pydantic import BaseModel, Field, validator
from app.domain.value_object.spot.spot_name import SpotName
from app.domain.value_object.spot.spot_description import SpotDescription
from app.domain.value_object.latitude import Latitude
from app.domain.value_object.longitude import Longitude
from .comments_schema import Comment
from . import validators


class SpotBase(BaseModel):
    name: str = Field(max_length=SpotName.MAX_LENGTH, example='東京駅')
    description: str = Field(max_length=SpotDescription.MAX_LENGTH,
                             example='スポットの説明文が入る')
    latitude: Union[float, str] = Field(example=35.68142354732969)
    longitude: Union[float, str] = Field(example=139.76709261114823)

    @validator('name')
    def valid_name(cls, v):
        label = 'スポット名'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v, max=SpotName.MAX_LENGTH)
        return v

    @validator('description')
    def valid_description(cls, v):
        label = 'おすすめポイント'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v,
                                max=SpotDescription.MAX_LENGTH)
        return v

    @validator('latitude')
    def valid_latitude(cls, v):
        label = '緯度'
        validators.not_blank(label, v)
        validators.valid_float_type(label, v)
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
        validators.valid_float_type(label, v)
        validators.valid_number_value(
            label=label,
            value=v,
            min=Longitude.MIN_VALUE,
            max=Longitude.MAX_VALUE
        )
        return v


class SpotCreate(SpotBase):
    pass


class Spot(SpotBase):
    id: int = Field(example=1)
    user_id: int = Field(example=1)

    class Config:
        orm_mode = True


class SpotWithComments(Spot):
    comments: List[Comment] = Field(
        example={'id': 1, 'user_id': 1, 'spot_id': 1, 'comment': 'コメント文が入る'})
