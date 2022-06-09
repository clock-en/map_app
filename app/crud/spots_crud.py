from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from app.model import spots_model
from app.core.sqlalchemy.schema import spots_schema


def set_spot_condition(lat: float, lng: float):
    return and_(
        spots_model.Spot.latitude == lat,
        spots_model.Spot.longitude == lng
    )


def get_spot_by_id(db: Session, id: int):
    return db.query(spots_model.Spot).filter(
        spots_model.Spot.id == id
    ).first()


def get_registered_spot(db: Session, name: str, lat: float, lng: float):
    spot_condition = set_spot_condition(lat, lng)
    return db.query(spots_model.Spot).filter(
        or_(spots_model.Spot.name == name, spot_condition)
    ).first()


def create_spot(db: Session, spot: spots_schema.SpotCreate):
    new_spot = spots_model.Spot(
        name=spot.name,
        latitude=spot.latitude,
        longitude=spot.longitude,
        user_id=spot.user_id
    )
    db.add(new_spot)
    db.commit()
    db.refresh(new_spot)
    return new_spot


def get_spots(db: Session):
    return db.query(spots_model.Spot).all()
