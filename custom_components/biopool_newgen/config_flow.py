
from homeassistant import config_entries
import voluptuous as vol
from homeassistant.helpers.selector import (
    EntitySelector,
    EntitySelectorConfig
)
from .const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        SCHEMA = vol.Schema({
            vol.Required("volume_m3", default=45): vol.All(vol.Coerce(int), vol.Range(min=5, max=200)),
            vol.Required("seuil_antigel", default=2): vol.Coerce(int),
            vol.Required("pac_consigne", default=25): vol.Coerce(int),
            vol.Optional("cover_active", default=False): bool,
            vol.Optional("pac_active", default=True): bool,
            vol.Optional("dashboard_enabled", default=True): bool,
            vol.Optional(
                "temperature_entity",
                default="sensor.pool_temp"
            ): EntitySelector(EntitySelectorConfig(domain="sensor")),
        })

        if user_input is not None:
            return self.async_create_entry(title="Piscine Bio", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=SCHEMA,
            errors=errors
        )
