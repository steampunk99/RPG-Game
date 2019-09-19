from classes.game import Person, bcolors

magic = [{
    "name": "Fire", "cost": 10, "damage": 60,
    "name": "Thunder", "cost": 10, "damage": 80,
    "name": "Blizzard", "cost": 10, "damage": 90,
}]

player = Person(450, 65, 60, 85, magic)
print(player.generateDamage())
print(player.generateDamage())
print(player.generateDamage())
