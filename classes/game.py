import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, attack, magic, defense):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attackLow = attack - 10
        self.attackHigh = attack + 10
        self.defense = defense
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generateDamage(self):
        return random.randrange(self.attackLow, self.attackHigh)

    def generateSpellDamage(self, i):
        magicLow = self.magic[i]["damage"]-5
        magicHigh = self.magic[i]["damage"]+5
        return random.randrange(magicLow, magicHigh)

    def takeDamage(self, damage):
        self.hp -= damage