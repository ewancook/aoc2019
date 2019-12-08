height, width = 6, 25
area = height*width

pixels = [int(i) for i in open("input.txt").readline().strip()]
flat_layers = [pixels[i:i+area] for i in range(0, len(pixels), area)]
layers = [[l[i:i+width] for i in range(0, len(l), width)] for l in flat_layers]

counted = [l.count(0) for l in flat_layers]
min_layer = flat_layers[counted.index(min(counted))]

row = []
for y in range(height):
    for x in range(width):
        pixels = [l[y][x] for l in layers]
        row.append([p for p in pixels if p != 2][0])

coloured = {
    0: '\x1b[0;30;40m]0\x1b[0m',
    1: '\x1b[6;37;47m]1\x1b[0m',
}

print("Part One: {}".format(min_layer.count(1)*min_layer.count(2)))
for i in range(0, len(row), width):
    print("".join([coloured[v] for v in row[i:i+width]]))
