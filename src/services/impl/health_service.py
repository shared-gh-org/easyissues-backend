import httpx
import logging
import time

from src.services.ihealth_service import IHealthService
from src.models.health_models import HealthPublic, InternetPublic
from src.utils.constants import STATUSDOWN, STATUSUP
from src.repository.dao.health_dao import HealthDao


class HealthService(IHealthService):
    def __init__(self, health_dao=HealthDao()):
        self.health_dao = health_dao

    async def health_check(self) -> HealthPublic:
        health_metrics = {"status": STATUSDOWN, "disk": "NaN", "sessions": -1}
        try:
            health_metrics = await self.health_dao.get_health_metrics()
        except Exception as e:
            logging.error(f"Error while trying to get health metrics:{e}")
        try:
            async with httpx.AsyncClient() as client:
                start_time = time.perf_counter()
                response = await client.get("https://github.com")
                end_time = time.perf_counter()

                latency = (end_time - start_time) * 1000  # ms
                throughput = (
                    len(response.content) / (end_time - start_time) / 1024
                )  # KB/s

                internet_status = (
                    STATUSUP if response.status_code == 200 else STATUSDOWN
                )

                internet = InternetPublic(
                    status=internet_status,
                    latency=f"{latency:.2f} ms",
                    throughput=f"{throughput:.2f} KB/s",
                )
        except Exception as e:
            logging.error(f"Error while checking internet health: {e}")
            internet = InternetPublic(
                status=STATUSDOWN, latency="NaN", throughput="NaN"
            )

        return HealthPublic(internet=internet, database=health_metrics)
