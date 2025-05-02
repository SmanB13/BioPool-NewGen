from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([PiscineStatusSensor()])

class PiscineStatusSensor(SensorEntity):
    def __init__(self):
        self._attr_name = "Piscine Bio - Statut"
        self._attr_native_value = "Actif"
        self._attr_should_poll = False
        self._attr_icon = "mdi:pool"