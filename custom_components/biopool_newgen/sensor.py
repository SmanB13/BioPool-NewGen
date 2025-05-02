from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([PiscineBioStatusSensor(entry)], True)

class PiscineBioStatusSensor(SensorEntity):
    def __init__(self, entry: ConfigEntry):
        self._attr_name = "État du système piscine"
        self._attr_unique_id = f"{DOMAIN}_core_status"
        self._attr_native_value = "En ligne"
        self._attr_should_poll = False
        self._attr_icon = "mdi:pool"