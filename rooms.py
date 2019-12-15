class StartRoom():
    def __init__(self):
        self.name = "Start"
        self.image = "Pixel Art/start.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class StairsRoom():
    def __init__(self):
        self.name = "Stairs"
        self.image = "Pixel Art/stairs.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class VendorRoom():
    def __init__(self):
        self.name = "Vendor"
        self.image = "Pixel Art/vendor.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class MobRoom():
    def __init__(self):
        self.name = "Mob"
        self.image = "Pixel Art/mob.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class EmptyRoom():
    def __init__(self):
        self.name = "Empty"
        self.image = "Pixel Art/room.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class TrapsRoom():
    def __init__(self):
        self.name = "Traps"
        self.image = "Pixel Art/trap.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class ItemsRoom():
    def __init__(self):
        self.name = "Items"
        self.image = "Pixel Art/item.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class MoneyRoom():
    def __init__(self):
        self.name = "Money"
        self.image = "Pixel Art/money.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []


class BossRoom():
    def __init__(self):
        self.name = "Boss"
        self.image = "Pixel Art/boss.png"
        self.state = False  # True - cleared stage / False - not cleaed stage
        self.outcomes = []
