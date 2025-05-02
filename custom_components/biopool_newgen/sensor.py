from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    async_add_entities([PiscineBioStatusSensor(entry)], True)

class PiscineBioStatusSensor(SensorEntity):
    def __init__(self, entry: ConfigEntry):
        self._attr_name = "État Piscine Bio"
        self._attr_unique_id = f"{DOMAIN}_status"
        self._attr_native_value = "ok"
        self._attr_should_poll = False

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "biopool")},
            "name": "Piscine Bio",
            "manufacturer": "BioPool NewGen",
            "entry_type": "service"
        }