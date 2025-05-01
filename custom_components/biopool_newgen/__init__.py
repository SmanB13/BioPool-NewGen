
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "biopool_newgen"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    async def handle_autotest(call):
        issues = []
        required_entities = ["sensor.pool_temp", "switch.pompe_filtration", "switch.uv_lamp"]
        for eid in required_entities:
            state = hass.states.get(eid)
            if not state or state.state in ["unavailable", "unknown"]:
                issues.append(f"Entité manquante: {eid}")
        title = "BioPool Autotest"
        msg = "✅ Tous les systèmes sont OK." if not issues else "\n".join(issues)
        hass.components.persistent_notification.create(title=title, message=msg)

    hass.services.async_register(DOMAIN, "run_autotest", handle_autotest)
    return True
