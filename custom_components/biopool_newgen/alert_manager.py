
from homeassistant.components.persistent_notification import async_create

class AlertManager:
    def __init__(self, hass):
        self.hass = hass

    async def send_alert(self, title, message):
        await async_create(
            self.hass,
            message,
            title,
            notification_id="biopool_alert"
        )
