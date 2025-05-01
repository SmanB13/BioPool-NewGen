
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    async_add_entities([BioPoolStatusSensor()])

class BioPoolStatusSensor(SensorEntity):
    _attr_name = "BioPool Status"
    _attr_unique_id = "biopool_status"
    _attr_icon = "mdi:water-pump"
    _attr_native_unit_of_measurement = None
    _attr_state_class = None

    def __init__(self):
        self._attr_native_value = "OK"
