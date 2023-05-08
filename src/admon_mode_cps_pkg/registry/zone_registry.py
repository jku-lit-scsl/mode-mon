class Zone:
    def __init__(self, zone_id, name, description='') -> None:
        super().__init__()
        self.zone_id = zone_id
        self.name = name
        self.description = description
