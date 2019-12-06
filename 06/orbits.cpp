#include <iostream>
#include <fstream>
#include <unordered_map>
#include <algorithm>
#include <vector>

class Planet {
public:
    int depth();
    std::string name;
    std::string orbiting_name;
    Planet *orbiting;
};

int Planet::depth() {
    auto p = this;
    int i;
    for (i = 0; p != nullptr; ++i) {
        p = p->orbiting;
    }
    return i;
}

int part_one(std::unordered_map<std::string, Planet*>& planets) {
    auto count = 0;
    for (auto const& [n, p]: planets) {
        count += p->depth();
    }
    return count;
}

Planet* lowest_common(Planet* a, Planet* b) {
    std::vector<Planet*> path;
    for (auto i = 0; a->orbiting != nullptr; ++i) {
        path.emplace_back(a);
        a = a->orbiting;
    }
    for (auto i = 0; b->orbiting != nullptr; ++i) {
        if (std::find(path.begin(), path.end(), b->orbiting) != path.end()) {
            return b;
        }
        b = b->orbiting;
    }
}

int part_two(std::unordered_map<std::string, Planet*>& planets) {
    auto san = planets["SAN"], you = planets["YOU"];
    auto lcn = lowest_common(san, you);
    return san->depth() + you->depth() - 2*lcn->depth();
}

int main() {
    std::ifstream f("input.txt");
    std::string line;
    std::unordered_map<std::string, Planet*> planets;
    while (std::getline(f, line)) {
        auto bracket = line.find(')');
        auto first = std::string(line.begin(), bracket + line.begin());
        auto second = std::string(line.begin() + bracket + 1, line.end());
        auto planet = new(Planet);
        planet->name = second;
        planet->orbiting_name = first;
        planets[second] = planet;
    }
    for (auto const& [_, p]: planets) {
        p->orbiting = planets[p->orbiting_name];
    }
    planets["COM"] = nullptr;
    std::cout << "Part One: " << part_one(planets) << std::endl;
    std::cout << "Part Two: " << part_two(planets) << std::endl;
}
