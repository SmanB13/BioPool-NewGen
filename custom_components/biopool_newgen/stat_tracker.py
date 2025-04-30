
from datetime import datetime, timedelta
from homeassistant.helpers.event import async_track_time_interval

class FiltrationStats:
    def __init__(self, hass, pump_entity):
        self.hass = hass
        self.pump_entity = pump_entity
        self.total_runtime_today = timedelta()
        self.last_check = datetime.now()

    async def start_tracking(self):
        async_track_time_interval(self.hass, self._update_runtime, timedelta(minutes=5))

    async def _update_runtime(self, now):
        state = self.hass.states.get(self.pump_entity)
        if state and state.state == "on":
            delta = now - self.last_check
            self.total_runtime_today += delta
        self.last_check = now

    def get_runtime_hours(self):
        return round(self.total_runtime_today.total_seconds() / 3600, 2)
