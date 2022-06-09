from sqlalchemy.orm import Session
from app.core.sqlalchemy.database import SessionLocal


class Dao(object):
    db: Session

    def __init__(self) -> None:
        self.db = SessionLocal()

    def __del__(self):
        self.db.close()
