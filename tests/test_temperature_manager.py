
from custom_components.biopool_newgen.temperature_manager import TemperatureManager

def test_temperature_override_enabled():
    manager = TemperatureManager({"simulate_when_missing": True})
    assert manager.override_enabled is True
