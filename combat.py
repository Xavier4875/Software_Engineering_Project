from classes import *


def combat(fighter1, fighter2):
    if fighter1.current_health > 0 and fighter2.current_health > 0:
        attack_other(fighter1, fighter2)

        if fighter2.current_health > 0:
            attack_other(fighter2, fighter1)
        else:
            return 0

        if fighter1.current_health > 0:
            return 1
        else:
            return 2


def attack_other(attacker, other):
    other.current_health -= max((attacker.attack - other.defense), 0)
    if other.current_health <= 0:
        other.current_health = 0



