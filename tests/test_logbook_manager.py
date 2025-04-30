
def test_logbook_format():
    name = "Filtration"
    message = "Pump activated"
    log_entry = f"BioPool - {name}: {message}"
    assert "BioPool - Filtration: Pump activated" == log_entry
