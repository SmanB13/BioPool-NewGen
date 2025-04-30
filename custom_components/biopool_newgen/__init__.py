
async def async_update_status(hass):
    data = hass.data["biopool_newgen"]
    mode = data["pool"].mode
    temperature = await data["temperature"].get_temperature(hass)
    runtime = data["stats"].get_runtime_hours()
    consumables = data["tracker"].check_levels()

    uv = consumables["uv"]["value"] or 0
    oxybio = consumables["oxybio"]["value"] or 0
    biobacter = consumables["biobacter"]["value"] or 0

    await data["dashboard"].update_full_status(
        mode, temperature, runtime, uv, oxybio, biobacter
    )
