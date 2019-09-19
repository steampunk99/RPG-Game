from classes.game import Person, bcolors

magic = [{
    "name": "Fire", "cost": 10, "damage": 60,
    "name": "Thunder", "cost": 10, "damage": 80,
    "name": "Blizzard", "cost": 10, "damage": 90,
}]

player = Person(450, 65, 60, 85, magic)
enemy = Person(1200, 76, 67, 88, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy Attack!" + bcolors.ENDC)

while running:
  