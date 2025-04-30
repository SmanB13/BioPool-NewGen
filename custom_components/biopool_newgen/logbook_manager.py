
import logging
from homeassistant.core import HomeAssistant
from homeassistant.components.persistent_notification import async_create

_LOGGER = logging.getLogger(__name__)

class LogbookManager:
    def __init__(self, hass: HomeAssistant):
        self.hass = hass

    async def log(self, name: str, message: str):
        _LOGGER.info("[BioPool Log] %s: %s", name, message)
        await self.hass.services.async_call(
            "logbook", "log",
            {
                "name": f"BioPool - {name}",
                "message": message,
                "domain": "biopool_newgen"
            },
            blocking=False
        )
        await async_create(
            self.hass,
            message,
            f"BioPool Alert - {name}",
            notification_id=f"biopool_alert_{name}"
        )
