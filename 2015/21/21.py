# boss = {"hp": 12, "d": 7, "a": 2, "name": "boss"}  # (109, 8, 2)
# me = {"hp": 8, "d": 5, "a": 5, "name": "me"}

boss = {"hp": 109, "d": 8, "a": 2, "name": "boss"}
me = {"hp": 100, "d": 7, "a": 3, "name": "me"}


def attack(p1, p2):
    damage_done = max(1, p1["d"] - p2["a"])
    new_hp = p2["hp"] - damage_done
    if new_hp <= 0:
        print(p2["name"] + " loses")
        exit()
    p2["hp"] = new_hp


def turn():
    attack(me, boss)
    attack(boss, me)


print((me, boss))

while me["hp"] > 0 and boss["hp"] > 0:
    turn()
    print((me, boss))
