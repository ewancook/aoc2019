class Planet:
	def __init__(self, name, orbiting=None):
		self.name = name
		self.orbiting = orbiting

	@property
	def depth(self):
		start, i = self, 0
		while start.orbiting is not None:
			start, i = start.orbiting, i + 1
		return i

def part_one(planets):
	return sum([p.depth for _, p in planets.items()])

def lowest_common(a, b):
	path = []
	while a.orbiting is not None:
		path.append(a.orbiting)
		a = a.orbiting
	while b.orbiting not in path:
		b = b.orbiting
	return b

def part_two(planets):
	san, you = planets["SAN"], planets["YOU"]
	lcn = lowest_common(san, you)
	return san.depth + you.depth - 2*lcn.depth

orbits = [l.rstrip("\n").split(")") for l in open("input.txt").readlines()]
planets = {p: Planet(p) for _, p in orbits}
planets["COM"] = Planet("COM", None)
for a, b in orbits:
		planets[b].orbiting = planets[a]

print("Part One:", part_one(planets))
print("Part Two:", part_two(planets))
