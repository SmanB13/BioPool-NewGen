
from datetime import datetime, timedelta

class FiltrationScheduler:
    def __init__(self, hass, pool_volume_m3=40, pump_flow_m3h=10):
        self.hass = hass
        self.pool_volume_m3 = pool_volume_m3
        self.pump_flow_m3h = pump_flow_m3h
        self.schedule_today = []

    def get_required_cycle_duration(self):
        # Retourne la durée nécessaire en heures pour une filtration complète du bassin
        return self.pool_volume_m3 / self.pump_flow_m3h

    def plan_cycle(self, start: datetime, duration_h: float):
        # Ajoute un cycle de filtration dans le planning journalier
        end = start + timedelta(hours=duration_h)
        self.schedule_today.append((start.time(), end.time()))

    def inject_oxybio(self):
        now = datetime.now().replace(hour=4, minute=0, second=0, microsecond=0)
        self.plan_cycle(now, self.get_required_cycle_duration())

    def inject_biobacter(self):
        oxybio_time = datetime.now().replace(hour=4, minute=0, second=0, microsecond=0)
        start = oxybio_time + timedelta(hours=12)
        self.plan_cycle(start, self.get_required_cycle_duration())

    def get_schedule_display(self):
        return [f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}" for start, end in self.schedule_today]
