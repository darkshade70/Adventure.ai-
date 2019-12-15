class StartRoom():
    def __init__(self):
        self.name = "Start"
        self.image = "Pixel Art/start.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = ""
        self.connected = []


class StairsRoom():
    def __init__(self):
        self.name = "Stairs"
        self.image = "Pixel Art/stairs.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = ""
        self.connected = []


class VendorRoom():
    def __init__(self):
        self.name = "Vendor"
        self.image = "Pixel Art/vendor.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = "outcomes/items.json"
        self.connected = []


class MobRoom():
    def __init__(self):
        self.name = "Mob"
        self.image = "Pixel Art/mob.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = "outcomes/items.json"
        self.connected = []



class EmptyRoom():
    def __init__(self):
        self.name = "Empty"
        self.image = "Pixel Art/room.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = ""
        self.connected = []



class TrapsRoom():
    def __init__(self):
        self.name = "Traps"
        self.image = "Pixel Art/trap.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = "outcomes/traps.json"
        self.connected = []


class ItemsRoom():
    def __init__(self):
        self.name = "Items"
        self.image = "Pixel Art/item.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = "outcomes/items.json"
        self.connected = []


class MoneyRoom():
    def __init__(self):
        self.name = "Money"
        self.image = "Pixel Art/money.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = "outcomes/items.json"
        self.connected = []


class BossRoom():
    def __init__(self):
        self.name = "Boss"
        self.image = "Pixel Art/boss.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = "outcomes/items.json"
        self.connected = []
