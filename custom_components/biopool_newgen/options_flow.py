
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_ENTITY_ID
from .const import DOMAIN

class BioPoolOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("temp_sensor_entity", default=self.config_entry.options.get("temp_sensor_entity", "")): str,
                vol.Optional("pump_entity", default=self.config_entry.options.get("pump_entity", "")): str,
                vol.Optional("uv_entity", default=self.config_entry.options.get("uv_entity", "")): str,
                vol.Optional("biobacter_entity", default=self.config_entry.options.get("biobacter_entity", "")): str,
                vol.Optional("oxybio_entity", default=self.config_entry.options.get("oxybio_entity", "")): str
            })
        )
