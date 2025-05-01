
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_ENTITY_ID
from .const import DOMAIN

class BioPoolNewGenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="BioPool-NewGen", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("temp_sensor_entity"): str,
                vol.Required("pump_relay_entity"): str,
                vol.Required("uv_relay_entity"): str,
                vol.Optional("oxybio_relay_entity"): str,
                vol.Optional("biobacter_relay_entity"): str,
                vol.Optional("simulate_hardware", default=True): bool,
                vol.Optional("pool_volume_m3", default=40): int,
                vol.Optional("oxybio_capacity_l", default=20): int,
                vol.Optional("oxybio_concentration", default=0.25): float,
                vol.Optional("biobacter_capacity_l", default=5): int,
            }),
        )
