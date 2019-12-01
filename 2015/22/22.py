# boss = {"hp": 58, "d": 9, "name": "boss"}
# me = {"hp": 50, "mana": 500, "name": "me"}


boss = {"hp": 14, "d": 8, "a": 0, "name": "boss"}  # 13 hp
me = {"hp": 10, "mana": 250, "a": 0, "name": "me"}

potential_effects = [{"damage": 4, "timer": 1, "cost": 53, "name": "Magic Missle"},
                     {"damage": 2, "heal": 2, "timer": 1, "cost": 73, "name": "Drain"},
                     {"armor": 7, "timer": 6, "cost": 113, "name": "Shield"},
                     {"damage": 3, "timer": 6, "cost": 173, "name": "Poison"},
                     {"mana": 101, "timer": 5, "cost": 229, "name": "Recharge"}]


def simple_attack(p1, p2):
    damage_done = max(1, p1["d"] - p2["a"])
    do_damage(p2, damage_done)


def do_damage(pl, damage):
    new_hp = pl["hp"] - damage
    pl["hp"] = new_hp
    if new_hp <= 0:
        print(pl["name"] + " loses")
        print((me, boss))
        exit()


def magic_attack(p1, p2):
    global effects
    magic_effect = potential_effects[effects_used.pop()]
    print("using " + magic_effect["name"])
    effects = [magic_effect] + effects


effects = []


def do_effects():
    global effects
    rem = []
    for cur_effect in effects:
        if "damage" in cur_effect:
            do_damage(boss, cur_effect["damage"])
        print((me, boss))
        cur_effect["timer"] -= 1
        if cur_effect["timer"] < 1:
            rem.append(cur_effect)

    for remove_effect in rem:
        effects.remove(remove_effect)


def turn():
    do_effects()
    print((me, boss))
    magic_attack(me, boss)
    do_effects()
    print((me, boss))
    simple_attack(boss, me)


effects_used = [0, 3, 1, 2, 4]
while me["hp"] > 0 and boss["hp"] > 0:
    turn()
    print((me, boss))
