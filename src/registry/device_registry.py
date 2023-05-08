class Device:
    def __init__(self, device_id, name, zone_id):
        super().__init__()
        self.id = device_id
        self.name = name
        self.zone_id = zone_id
        self.property_list = []

    def can_move_freely(self) -> None:
        self.property_list.append(Property(name='can_move_freely', is_active=True))

    # TODO: add other CPS behavior here in the future...


class PropertyList:
    def __init__(self) -> None:
        super().__init__()
        self.prop_list: list[Property] = list()


class Property:
    def __init__(self, name: str, is_active=False) -> None:
        super().__init__()
        self.property_name = name
        self.is_active = is_active
