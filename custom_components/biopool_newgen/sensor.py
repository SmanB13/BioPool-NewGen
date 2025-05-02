from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([PiscineBioPoolStatus(entry)], True)

class PiscineBioPoolStatus(SensorEntity):
    def __init__(self, entry: ConfigEntry):
        self._attr_name = "État Piscine BioPool"
        self._attr_unique_id = f"{DOMAIN}_main_status_v8"
        self._attr_native_value = "Fonctionnel"
        self._attr_should_poll = False
        self._attr_icon = "mdi:pool"