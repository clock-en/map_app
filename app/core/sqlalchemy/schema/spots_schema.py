from pydantic import BaseModel, Field
from app.domain.value_object.spot.spot_name import SpotName


class SpotBase(BaseModel):
    name: str = Field(max_length=SpotName.MAX_LENGTH, example='東京駅')
    latitude: float = Field(example=35.68142354732969)
    longitude: float = Field(example=139.76709261114823)
    user_id: int = Field(example=1)


class SpotCreate(SpotBase):
    pass


class Spot(SpotBase):
    id: int = Field(example=1)

    class Config:
        orm_mode = True
