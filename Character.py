from abilityModifier import abilityModifier
from Dice import Dice
from equipmentTable import equipmentTable
from luckScoreTable import luckScoreTable
import csv

"""A Character class that rolls a new character automatically."""

class Character:
    inventory = []
    XP = 0

    def __init__(self):

        self.abilities = self.rollAbilities()
        self.modifiers = self.getModifiers()
        self.HP = self.rollHP()
        self.coppahs = self.rollCoppahs()
        self.inventory.append(self.rollEquipment())
        self.BALR = self.getBirthAugrandLuckyRoll()
        self.occupation = self.getOccupation()
        self.inventory.append(self.getTrainedWeapon())
        self.checkSlingDart()
        self.inventory.append(self.getTradeGoods())
        self.checkPushCart()
        self.checkIfFarmer()
        self.AC = 10 + int(self.modifiers.get('Agility'))

    def checkIfFarmer(self):
        d8 = Dice(1, 8)
        if self.occupation == 'Farmer':
            farmerType = {
                1: 'Potato',
                2: 'Wheat',
                3: 'Turnip',
                4: 'Corn',
                5: 'Rice',
                6: 'Parsnip',
                7: 'Radish',
                8: 'Rutabaga'
            }
            roll = d8.roll()
            self.occupation = f'{farmerType.get(roll)} Farmer'

    def checkPushCart(self):
        d6 = Dice(1, 6)
        if self.inventory[len(self.inventory) - 1] == 'Pushcart':
            cartContents = {
                1: 'Tomaters',
                2: 'A Whole lotta Nuffin',
                3: 'Straw',
                4: 'Yer Dead',
                5: 'Dirt',
                6: 'Rocks'
            }
            roll = d6.roll()
            self.inventory[len(self.inventory) - 1] = f'Pushcart full o\' {cartContents.get(roll)}'

    def checkSlingDart(self):
        d6 = Dice(1, 6)
        if self.inventory[len(self.inventory) - 1] == 'Sling':
            roll = d6.roll()
            self.inventory.append(f'{roll} Sling Stones')
        if self.inventory[len(self.inventory) - 1] == 'Dart':
            roll = d6.roll()
            self.inventory.append(f'{roll} Darts')

    def rollAbilities(self):
        abilities = {'Strength': 0,
                     'Agility': 0,
                     'Stamina': 0,
                     'Personality': 0,
                     'Intelligence': 0,
                     'Luck': 0}
        dice = Dice(3, 6)

        for ability in abilities:
            abilities[ability] = dice.roll()

        return abilities

    def getModifiers(self):
        modifiers = {'Strength': '',
                     'Agility': '',
                     'Stamina': '',
                     'Personality': '',
                     'Intelligence': '',
                     'Luck': ''}
        for ability in self.abilities:
            modifiers[ability] = abilityModifier.table.get(self.abilities.get(ability))[0]

        for skill in modifiers:
            if int(modifiers.get(skill)) >= 0:
                modifiers[skill] = f'+{modifiers.get(skill)}'

        return modifiers

    def rollHP(self):
        die = Dice(1, 4)
        HP = die.roll() + abilityModifier.table.get(self.abilities.get('Stamina'))[0]
        if HP < 1:
            HP = 1

        return HP

    def rollCoppahs(self):
        dice = Dice(5, 12)
        return dice.roll()

    def rollEquipment(self):
        eqt = equipmentTable()
        die = Dice(1, 24)
        return eqt.rollTable.get(die.roll())

    def getBirthAugrandLuckyRoll(self):
        table = luckScoreTable
        die = Dice(1, 30)
        return table.table.get(die.roll())

    def getOccupation(self):
        die = Dice(1, 100)
        roll = die.roll()
        with open('occupations.csv', 'r') as occupations:
            reader = csv.reader(occupations)
            for row in reader:
                if roll == int(row[0]):
                    return row[1].title().strip()

    def getTrainedWeapon(self):
        with open('occupations.csv', 'r') as occupations:
            reader = csv.reader(occupations)
            for row in reader:
                if self.occupation == row[1].title().strip():
                    return row[2].title().strip()

    def getTradeGoods(self):
        with open('occupations.csv', 'r') as occupations:
            reader = csv.reader(occupations)
            for row in reader:
                if self.occupation == row[1].title().strip():
                    return row[3].title().strip()



jon = Character()
print(f'HP: {jon.HP}')
print(f'XP: {jon.XP}')
print(f'Armor Class: {jon.AC}')
print(f'Coppahs: {jon.coppahs}')
print(f'Birth Augr and Lucky Roll: {jon.BALR}')
print(f'Occupation: {jon.occupation}')
print(f'Inventory: {jon.inventory}')
for ability in jon.abilities:
    print(f'{ability}: {jon.abilities.get(ability)}')
    print(f'Modifier: {jon.modifiers.get(ability)}\n')
















