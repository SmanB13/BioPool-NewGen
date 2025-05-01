
from homeassistant import config_entries
import voluptuous as vol
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig
from .const import DOMAIN

class BioPoolOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = self.config_entry.options
        data_schema = vol.Schema({
            vol.Required("volume_m3", default=options.get("volume_m3", 45)): vol.All(vol.Coerce(int), vol.Range(min=5, max=200)),
            vol.Required("seuil_antigel", default=options.get("seuil_antigel", 2)): vol.Coerce(int),
            vol.Required("pac_consigne", default=options.get("pac_consigne", 25)): vol.Coerce(int),
            vol.Optional("cover_active", default=options.get("cover_active", False)): bool,
            vol.Optional("pac_active", default=options.get("pac_active", True)): bool,
            vol.Optional("dashboard_enabled", default=options.get("dashboard_enabled", True)): bool,
            vol.Optional(
                "temperature_entity",
                default=options.get("temperature_entity", "sensor.pool_temp")
            ): EntitySelector(EntitySelectorConfig(domain="sensor")),
        })

        return self.async_show_form(step_id="init", data_schema=data_schema)

async def async_get_options_flow(config_entry):
    return BioPoolOptionsFlowHandler(config_entry)
