
from custom_components.biopool_newgen.demo_simulator import DemoSimulator

def test_demo_simulation_output():
    sim = DemoSimulator()
    data = sim.get_simulated_state()
    assert "temperature" in data
    assert "uv_remaining" in data
    assert "mode" in data
