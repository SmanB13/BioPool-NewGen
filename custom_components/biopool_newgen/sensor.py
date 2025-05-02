from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([BioPoolStatusSensor(hass)])

class BioPoolStatusSensor(SensorEntity):
    def __init__(self, hass: HomeAssistant):
        self._attr_name = "Statut Piscine Bio"
        self._attr_native_value = "Disponible"
        self._attr_icon = "mdi:pool"
        self._attr_should_poll = False