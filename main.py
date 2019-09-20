from classes.game import Person, bcolors
from classes.magic import Spell

# Black Magic
fire = Spell("fire", 10, 100, "black magic")
thunder = Spell("thunder", 10, 100, "black magic")
glizzard = Spell("glizzard", 20, 200, "black magic")
meteor = Spell("meteor", 12, 120, "black magic")

# White Magic
cure = Spell("cure", 12, 120, "white magic")
cura = Spell("cure", 18, 200, "white magic")

player = Person(450, 65, 60, 85, [fire, thunder, glizzard, meteor, cura, cure)
enemy = Person(1200, 76, 67, 88, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy Attack!" + bcolors.ENDC)

while running:
    print("====================")
    player.choose_Action()
    choice = input("Choose an action: ")
    index = int(choice) - 1
    print("You chose ", index)

    if index == 0:
        player_damage = player.generateDamage()
        enemy.takeDamage(player_damage)
        print("You attacked for", player_damage,
              "points of damage. Enemy HP: ", enemy.getHp())

    elif index == 1:
        player.choose_Magic()
        magic_choice = int(input("Choose magic:")) - 1
        magic_damage = player.generateSpellDamage(magic_choice)
        spell = player.getSpellName(magic_choice)
        cost = player.getSpellMpCost(magic_choice)

        current_mp = player.getMp()

        if cost > current_mp:
            print(bcolors.FAIL +
                  "You are unable to use magic at this time " + bcolors.ENDC)
            continue
        player.reduce_Mp(cost)
        enemy.takeDamage(magic_damage)
        print(bcolors.OKBLUE + spell + "deals", str(magic_damage),
              "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generateDamage()
    player.takeDamage(enemy_damage)
    print("Enemy attacks for ", enemy_damage,
          "player health is:", player.getHp())

    print("================================")
    print("Enemy hit points" + bcolors.FAIL +
          str(enemy.getHp) + "/" + str(enemy.getMax_hp()) + bcolors.ENDC + "\n")

    print("Player hit points" + bcolors.OKGREEN +
          str(player.getHp) + "/" + str(player.getMax_hp()) + bcolors.ENDC + "\n")

    if enemy.getHp() == 0:
        print(bcolors.OKGREEN + "You  win" + bcolors.ENDC)
        running = False

    elif player.getHp == 0:
        print(bcolors.FAIL + "You have Lost" + bcolors.ENDC)
        running = False
