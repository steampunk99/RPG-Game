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

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            return self.hp

    def getHp(self):
        return self.hp

    def getMax_hp(self):
        return self.max_hp

    def getMp(self):
        return self.mp

    def getMax_mp(self):
        return self.max_mp

    def reduce_Mp(self, cost):
        self.mp -= cost

    def heal(self, damage):
        self.hp -= damage
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def choose_Action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)

    def choose_Magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"])
            i += 1
