
from custom_components.biopool_newgen.erp_compliance import ErpCompliance

def test_erp_enforce_runtime():
    erp = ErpCompliance({"erp_min_hours": 8})
    assert erp.should_enforce_min_runtime(5.0) is True
