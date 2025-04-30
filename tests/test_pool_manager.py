
from custom_components.biopool_newgen.pool_manager import FILTER_MODES

def test_valid_modes():
    assert "auto" in FILTER_MODES
    assert "manual" in FILTER_MODES
    assert "off" in FILTER_MODES
