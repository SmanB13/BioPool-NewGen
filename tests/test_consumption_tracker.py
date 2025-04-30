
from custom_components.biopool_newgen.consumption_tracker import CONSUMABLES

def test_consumable_keys():
    assert "uv" in CONSUMABLES
    assert "oxybio" in CONSUMABLES
    assert "biobacter" in CONSUMABLES
