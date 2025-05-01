
from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

CONFIG_SCHEMA = vol.Schema({
    vol.Required("volume_m3", default=45): vol.All(vol.Coerce(int), vol.Range(min=5, max=200)),
    vol.Required("seuil_antigel", default=2): vol.Coerce(int),
    vol.Required("cover_active", default=False): bool,
    vol.Required("pac_active", default=True): bool,
    vol.Optional("temperature_entity", default="sensor.pool_temp"): str,
})

class BiopoolNewgenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="BioPool", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=CONFIG_SCHEMA,
            errors=errors
        )
