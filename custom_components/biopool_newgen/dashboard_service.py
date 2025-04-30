
from homeassistant.core import HomeAssistant

class DashboardService:
    def __init__(self, hass: HomeAssistant):
        self.hass = hass

    async def expose_state(self, entity_id: str, state: str, attributes: dict = None):
        await self.hass.states.async_set(entity_id, state, attributes or {})

    async def update_full_status(self, mode: str, temperature: float, runtime: float,
                                 uv: float, oxybio: float, biobacter: float):
        await self.expose_state(
            "sensor.biopool_status",
            mode,
            {
                "friendly_name": "Filtration Status",
                "icon": "mdi:pool",
                "temperature": temperature,
                "runtime_hours": runtime,
                "uv_level": uv,
                "oxybio_level": oxybio,
                "biobacter_level": biobacter
            }
        )
