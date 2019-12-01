def fuel_mass(mass):
    return mass//3 - 2

def masses_iterator(masses):
    for m in masses:
        fuel = fuel_mass(m)
        while fuel > 0:
            yield fuel
            fuel = fuel_mass(fuel)

masses = [int(l.rstrip("\n")) for l in open("input.txt").readlines()]

print("Part 1:", sum([fuel_mass(m) for m in masses]))
print("Part 2:", sum(masses_iterator(masses)))
