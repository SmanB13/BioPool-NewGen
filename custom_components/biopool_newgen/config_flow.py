import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig
from .const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        schema = vol.Schema({
            vol.Required("volume_m3", default=45): vol.All(vol.Coerce(int), vol.Range(min=5, max=200)),
            vol.Required("seuil_antigel", default=2): vol.Coerce(int),
            vol.Required("pac_consigne", default=25): vol.Coerce(int),
            vol.Optional("cover_active", default=False): bool,
            vol.Optional("pac_active", default=True): bool,
            vol.Optional("dashboard_enabled", default=True): bool,
            vol.Optional("temperature_entity"): EntitySelector(EntitySelectorConfig(domain="sensor")),
            vol.Optional("pump_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
            vol.Optional("uv_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
            vol.Optional("oxybio_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
            vol.Optional("biobact_entity"): EntitySelector(EntitySelectorConfig(domain="switch")),
        })

        if user_input is not None:
            return self.async_create_entry(title="Piscine Bio", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
            description_placeholders={
                "intro": "Bienvenue dans votre cockpit de piscine Bio 🌿. Configurez les équipements et automatismes."
            }
        )