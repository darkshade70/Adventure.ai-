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

class PoisonPotion:
    poisonValue = poisonPotDamage

class OversightPotion:
    pass

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
