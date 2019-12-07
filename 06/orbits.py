class Planet:
	def __init__(self, orbiting=None):
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

def part_two(san, you):
	return san.depth + you.depth - 2*lowest_common(san, you).depth

orbits = [l.strip().split(")") for l in open("input.txt").readlines()]
planets = {p: Planet() for _, p in orbits}
planets["COM"] = Planet(None)
for a, b in orbits:
		planets[b].orbiting = planets[a]

print("Part One:", part_one(planets))
print("Part Two:", part_two(planets["SAN"], planets["YOU"]))
