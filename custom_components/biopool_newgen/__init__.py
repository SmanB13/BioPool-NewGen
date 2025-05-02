from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .dashboard_service import DashboardService

DOMAIN = "biopool_newgen"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Lancer dashboard si demandé
    if entry.data.get("dashboard_enabled", True):
        dashboard = DashboardService(hass)
        await dashboard.create_or_update_dashboard()

    # Charger la plateforme sensor
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return unload_ok