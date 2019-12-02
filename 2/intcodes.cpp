#include <iostream>
#include <fstream>
#include <vector>

int totalise_instructions(std::vector<int> codes, int noun, int verb) {
    codes[1] = noun;
    codes[2] = verb;

    for (auto i = 0; i < codes.size(); i += 4) {
        auto op = codes[i];
        auto first = codes[i+1];
        auto second = codes[i+2];
        auto pos = codes[i+3];
        if (op == 99) {
            return codes[0];
        }
        codes[pos] = (op&1) ? codes[first]+codes[second] : codes[first]*codes[second];
    }
}

int main() {
    std::ifstream f{"input.txt"};
    std::string line;
    std::vector<int> intcodes{};

    while (std::getline(f, line, ',')) {
            intcodes.push_back(std::stoi(line));
    }
    std::cout << "Part 1: " << totalise_instructions(intcodes, 12, 2) << '\n';

    for (auto a = 0; a < 100; a++) {
        for (auto b = 0; b < 100; b++) {
            if (totalise_instructions(intcodes, a, b) == 19690720) {
                std::cout << "Part 2: " << 100*a + b << std::endl;
                return 0;
            }
        }
    }
}
