
from custom_components.biopool_newgen.energy_optimizer import EnergyOptimizer

def test_off_peak_hours():
    optimizer = EnergyOptimizer({"peak_hours": [(6, 10), (18, 22)]})
    assert isinstance(optimizer.is_off_peak(), bool)
