from math import ceil
import networkx as nx


def calc_ore(graph, fuel):
    graph.nodes["FUEL"]["required"] = fuel
    for node in nx.topological_sort(graph):
        for _, t in graph.edges(node):
            reactions = int(
                ceil(graph.nodes[node]["required"] / graph.nodes[node]["produced"]))
            graph.nodes[t]["required"] += reactions * graph[node][t]["weight"]
    return graph.nodes["ORE"]["required"]


def new_graph():
    graph = nx.DiGraph()
    with open("input.txt") as f:
        for line in f.readlines():
            reacted, produced = line.split("=>")
            p_amount, p_name = produced.split()
            graph.add_node(p_name, produced=int(p_amount), required=0)
            for r in reacted.split(","):
                r_amount, r_name = r.split()
                graph.add_edge(p_name, r_name, weight=int(r_amount))
    graph.add_node("ORE", required=0, produced=1)
    return graph


def calc_fuel(target, part_one):
    fuel, i = 1, 0
    while True:
        ore = calc_ore(new_graph(), fuel + 1)
        if ore > target:
            return fuel, i
        fuel, i = max(fuel + 1, int(target * (fuel + 1) // ore)), i + 1


part_one = calc_ore(new_graph(), 1)
print("Part One: {}".format(part_one))
print("Part Two: {} ({} iterations)".format(*calc_fuel(1e12, part_one)))

