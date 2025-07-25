from abc import ABC, abstractmethod
from src.models.health_models import HealthPublic


class IHealthService(ABC):
    @abstractmethod
    def health_check(self) -> HealthPublic:
        """
        Method to return the health of the dependencies
        """
        pass
