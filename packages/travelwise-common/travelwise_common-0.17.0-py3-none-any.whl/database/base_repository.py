from abc import ABC, abstractmethod
from typing import Any, List


class BaseRepository(ABC):
    """Abstract base repository defining common CRUD operations."""

    @abstractmethod
    def get_all(self) -> List[Any]:
        """Retrieve all records."""
        pass

    @abstractmethod
    def filter(self, **filters) -> List[Any]:
        """Retrieve records matching given filters."""
        pass

    @abstractmethod
    def get(self, identifier: Any) -> Any:
        """Retrieve a single record by identifier."""
        pass

    @abstractmethod
    def add(self, **data) -> Any:
        """Insert a new record."""
        pass

    @abstractmethod
    def update(self, identifier: Any, **data) -> Any:
        """Update an existing record."""
        pass

    @abstractmethod
    def delete(self, identifier: Any) -> bool:
        """Delete a record by identifier."""
        pass
