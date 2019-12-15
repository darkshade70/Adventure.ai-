# AdventureAI Inventory System Classes

# Weights different stats hold over the item's power value
healthWeight = 0.4
armorWeight = 0.5
damageWeight = 0.9

# Potion Controls
healthPotHeal = 50
poisonPotDamage = 50

# Sell value ratio to powerw
sellValueRatio = 1.5

class Helmet:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getArmor(self):
        return self.armor
    def getPower(self):
        return self.health*healthWeight + self.armor*armorWeight
    def getSellValue(self):
        return self.getPower()*sellValueRatio

class Chestplate:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getArmor(self):
        return self.armor
    def getPower(self):
        return self.health*healthWeight + self.armor*armorWeight
    def getSellValue(self):
        return self.getPower()*sellValueRatio

class Leggings:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getArmor(self):
        return self.armor
    def getPower(self):
        return self.health*healthWeight + self.armor*armorWeight
    def getSellValue(self):
        return self.getPower()*sellValueRatio

class Boots:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getArmor(self):
        return self.armor
    def getPower(self):
        return self.health*healthWeight + self.armor*armorWeight
    def getSellValue(self):
        return self.getPower()*sellValueRatio

class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.health = damage
        self.power = self.damage*damageWeight
    def getName(self):
        return self.name
    def getDamage(self):
        return self.damage
    def getPower(self):
        return self.damage*damageWeight
    def getSellValue(self):
        return self.getPower()*sellValueRatio

class Shield:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getArmor(self):
        return self.armor
    def getPower(self):
        return self.health*healthWeight + self.armor*armorWeight
    def getSellValue(self):
        return self.getPower()*sellValueRatio

class HealthPotion:
    healValue = healthPotHeal
    def getSellValue(self):
        return 10000

class PoisonPotion:
    poisonValue = poisonPotDamage
    def getSellValue(self):
        return 10000

class OversightPotion:
    def getSellValue(self):
        return 25000

class Inventory:
    def __init__(self, helmet, chestplate, leggings, boots, sword, shield, healthPots, poisonPots, oversightPots):
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.sword = sword
        self.shield = shield
        self.healthPots = healthPots
        self.poisonPots = poisonPots
        self.oversightPots = oversightPots
    # Gets
    def getHelmet(self):
        return self.helmet
    def getChestplate(self):
        return self.chestplate
    def getLeggings(self):
        return self.leggings
    def getBoots(self):
        return self.boots
    def getSword(self):
        return self.sword
    def getShield(self):
        return self.shield
    def getHealthPotions(self):
        return self.healthPots
    def getPoisonPotions(self):
        return self.poisonPots
    def getOversightPotions(self):
        return self.oversightPots
    # Sets
    def setHelmet(self, newHelmet):
        self.helmet = newHelmet
    def setChestplate(self, newChestplate):
        self.chestplate = newChestplate
    def setLeggings(self, newLeggings):
        self.leggings = newLeggings
    def setBoots(self, newBoots):
        self.boots = newBoots
    def setSword(self, newSword):
        self.sword = newSword
    def setShield(self, newShield):
        self.shield = newShield
    def setHealthPotions(self, newHealthPots):
        self.healthPots = newHealthPots
    def setPoisonPotions(self, newPoisonPots):
        self.poisonPots = newPoisonPots
    def setOversightPotions(self, newOversightPots):
        self.oversightPots = newOversightPots
    # Calculate Totals
    def calculateTotalPower(self):
        return self.helmet.getPower() + self.chestplate.getPower() + self.leggings.getPower() + self.boots.getPower() + self.sword.getPower() + self.shield.getPower()
    def calculateTotalValue(self):
        return self.calculateTotalPower()*sellValueRatio

class randomStatGenerator:
    def __init__(self, level):
        randomFactor = random.random(-3.5, 3.5)
        self.power = level*100 + math.floor(level * randomFactor)
        self.health = math.floor(power/1.8 * healthWeight)
        self.armor = math.floor(power/1.8 * armorWeight)
        self.damage = math.floor(power/1.8 * damageWeight)
    def getPower(self):
        return self.power
    def getHealth(self):
        return self.health
    def getArmor(self):
        return self.armor
    def getDamage(self):
        return self.damage

class Vendor:
    def __init__(self, level):
        self.randomStat1 = randomStatGenerator(level)
        self.randomStat2 = randomStatGenerator(level)
        choice = random.randint(0, 17)
        # Note: All prices can be gotten by doing Vendor.item1.getSellValue() or Vendor.item2.getSellValue()
        if choice in [1, 2]:
            # Helmet
            self.item1 = Helmet("Vendor's Helm", self.randomStat1.getHealth(), self.randomStat1.getArmor())
        elif choice in [3, 4]:
            # Chestplate
            self.item1 = Chestplate("Vendor's Chestplate", self.randomStat1.getHealth(), self.randomStat1.getArmor())
        elif choice in [5, 6]:
            # Leggings
            self.item1 = Leggings("Vendor's Leggings", self.randomStat1.getHealth(), self.randomStat1.getArmor())
        elif choice in [7, 8]:
            # Boots
            self.item1 = Boots("Vendor's Boots", self.randomStat1.getHealth(), self.randomStat1.getArmor())
        elif choice in [9, 10]:
            # Sword
            self.item1 = Sword("Vendor's Sword", self.randomStat1.getDamage())
        elif choice in [11, 12]:
            # Shield
            self.item1 = Shield("Vendor's Shield", self.randomStat1.getHealth(), self.randomStat1.getArmor())
        elif choice in [13, 14]:
            # Health Pots
            self.item1 = HealthPotion()
        elif choice in [15, 16]:
            # Poison Pots
            self.item1 = PoisonPotion()
        elif choice == 17:
            # Oversight Pots
            self.item1 = OversightPotion()

        #Item 2
        choice = random.randint(0, 17)
        # Note: All prices can be gotten by doing Vendor.item1.getSellValue() or Vendor.item2.getSellValue()
        if choice in [1, 2]:
            # Helmet
            self.item2 = Helmet("Vendor's Helm", self.randomStat2.getHealth(), self.randomStat2.getArmor())
        elif choice in [3, 4]:
            # Chestplate
            self.item2 = Chestplate("Vendor's Chestplate", self.randomStat2.getHealth(), self.randomStat2.getArmor())
        elif choice in [5, 6]:
            # Leggings
            self.item2 = Leggings("Vendor's Leggings", self.randomStat2.getHealth(), self.randomStat2.getArmor())
        elif choice in [7, 8]:
            # Boots
            self.item2 = Boots("Vendor's Boots", self.randomStat2.getHealth(), self.randomStat2.getArmor())
        elif choice in [9, 10]:
            # Sword
            self.item2 = Sword("Vendor's Sword", self.randomStat2.getDamage())
        elif choice in [11, 12]:
            # Shield
            self.item2 = Shield("Vendor's Shield", self.randomStat2.getHealth(), self.randomStat2.getArmor())
        elif choice in [13, 14]:
            # Health Pots
            self.item2 = HealthPotion()
        elif choice in [15, 16]:
            # Poison Pots
            self.item2 = PoisonPotion()
        elif choice == 17:
            # Oversight Pots
            self.item2 = OversightPotion()