with open("input1.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0

for module in content:
    fuel = int((int(module) / 3)) - 2
    part1 += fuel
    part2 += fuel

    while fuel > 0:
        new_fuel = int((int(fuel) / 3)) - 2
        if new_fuel < 0:
            break
        part2 += new_fuel
        fuel = new_fuel

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))
