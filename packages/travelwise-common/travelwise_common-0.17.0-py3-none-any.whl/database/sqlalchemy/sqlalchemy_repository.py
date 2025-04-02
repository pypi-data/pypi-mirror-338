from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from database.base_repository import BaseRepository


class SQLAlchemyRepository(BaseRepository):
    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def get_all(self) -> list:
        records = self.session.query(self.model).all()
        return records

    def filter(self, **filters) -> list:
        query = self.session.query(self.model)
        for key, value in filters.items():
            query = query.filter(getattr(self.model, key) == value)
        return query.all()

    def get(self, identifier) -> Any:
        record = self.session.get(self.model, identifier)
        return record

    def commit(self):
        """Commit the current transaction."""
        self.session.commit()

    def rollback(self):
        """Rollback the current transaction."""
        self.session.rollback()

    def add(self, **data) -> dict[str, Any]:
        """Insert a new row into the given model."""
        try:
            instance = self.model(**data)
            self.session.add(instance)
            self.commit()
            return instance
        except SQLAlchemyError as e:
            self.rollback()
            raise e

    def update(self, identifier, **data) -> Any:
        try:
            instance = self.get(identifier)
            if instance:
                for key, value in data.items():
                    setattr(instance, key, value)
                self.commit()
                return instance
            else:
                return None
        except SQLAlchemyError as e:
            self.rollback()
            raise e

    def delete(self, identifier) -> bool:
        """Delete a row by ID."""
        try:
            instance = self.get(identifier)
            if instance:
                self.session.delete(instance)
                self.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.rollback()
            raise e
