
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "biopool_newgen"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Enregistrer le service d'autotest
    async def handle_autotest(call):
        issues = []
        required_entities = ["sensor.pool_temp", "switch.pompe_filtration", "switch.uv_lamp"]
        for eid in required_entities:
            state = hass.states.get(eid)
            if not state or state.state in ["unavailable", "unknown"]:
                issues.append(f"Entité manquante: {eid}")
        msg = "✅ Tous les systèmes sont OK." if not issues else "\n".join(issues)
        hass.components.persistent_notification.create(title="BioPool Autotest", message=msg)

    hass.services.async_register(DOMAIN, "run_autotest", handle_autotest)

    # Création automatique du tableau de bord si demandé
    if entry.data.get("dashboard_enabled", True):
        dashboard_url = "lovelace-biopool"
        dashboard_title = "BioPool NewGen"
        dashboard_icon = "mdi:pool-thermometer"
        dashboard_path = hass.config.path("custom_components/biopool_newgen/dashboards/biopool_dashboard.yaml")

        hass.components.frontend.async_register_built_in_panel(
            component_name="lovelace",
            sidebar_title=dashboard_title,
            sidebar_icon=dashboard_icon,
            frontend_url_path=dashboard_url,
            config={"mode": "yaml", "title": dashboard_title},
            require_admin=True
        )

    return True


async def async_get_options_flow(config_entry):
    from .options_flow import BioPoolOptionsFlowHandler
    return BioPoolOptionsFlowHandler(config_entry)
