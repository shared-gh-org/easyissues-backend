import requests

from src.services.ihealth_service import IHealthService
from src.models.health_models import HealthPublic
from src.utils.constants import STATUSNOTOK, STATUSOK


class HealthService(IHealthService):
    def health_check(self) -> HealthPublic:
        response = requests.get("https://github.com")
        if response.status_code == 200:
            return HealthPublic(status=STATUSOK)
        return HealthPublic(status=STATUSNOTOK)
