
class ModeManager:
    def __init__(self, mode: str = "erp"):
        self.mode = mode.lower()

    def set_mode(self, mode: str):
        self.mode = mode.lower()

    def is_erp(self):
        return self.mode == "erp"

    def is_public(self):
        return self.mode == "public"

    def is_demo(self):
        return self.mode == "demo"

    def can_modify(self):
        return self.mode in ["erp", "demo"]

    def should_simulate(self):
        return self.mode == "demo"

    def is_read_only(self):
        return self.mode == "public"
