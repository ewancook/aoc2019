#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <algorithm>

std::vector<std::pair<int, int>> pairs_from_step(char dir, int dist, const std::pair<int, int>& pos) {
    int x = pos.first, y = pos.second;
    std::vector<std::pair<int, int>> steps;
    for (auto i = 0; i < dist; i++) {
        if (dir == 'U' || dir == 'D') {
            steps.emplace_back(std::make_pair(x, dir == 'U' ? ++y: --y));
            continue;
        }
        steps.emplace_back(std::make_pair(dir == 'R' ? ++x: --x, y));
    }
    return steps;
}

std::vector<std::pair<int, int>> create_pairs(const std::string& line) {
    std::istringstream iss(line);
    std::string value;
    std::vector<std::pair<int, int>> steps;
    std::pair<int, int> last_step = std::make_pair(0, 0);
    while(std::getline(iss, value, ',')) {
        auto dist = std::stoi(value.substr(1, value.length()-1));
        auto dir = value.front();
        auto new_steps = pairs_from_step(dir, dist, last_step);
        steps.insert(steps.end(), new_steps.begin(), new_steps.end());
        last_step = steps.back();
    }
    return steps;
}

int manhattan_distance(const std::pair<int, int>& pair) {
    return abs(pair.first) + abs(pair.second);
}

int main() {
    std::ifstream f("input.txt");
    std::string first_wire, second_wire;

    std::getline(f, first_wire);
    std::getline(f, second_wire);

    auto first_pairs = create_pairs(first_wire);
    auto second_pairs = create_pairs(second_wire);

    std::vector<std::pair<int, int>> first_sorted{first_pairs.size()}, second_sorted(second_pairs.size());

    std::partial_sort_copy(first_pairs.begin(), first_pairs.end(), first_sorted.begin(), first_sorted.end());
    std::partial_sort_copy(second_pairs.begin(), second_pairs.end(), second_sorted.begin(), second_sorted.end());

    std::vector<std::pair<int, int>> common;
    std::set_intersection(first_sorted.begin(), first_sorted.end(), second_sorted.begin(), second_sorted.end(), std::back_inserter(common));
    std::sort(common.begin(), common.end(), [&](std::pair<int, int> first, std::pair<int, int> second) {
        return manhattan_distance(first) < manhattan_distance(second);
    });
    std::cout << "Part 1: " << manhattan_distance(common.front()) << std::endl;

    std::vector<int> steps;
    steps.reserve(common.size());

    for (auto const& pos: common) {
        auto first = std::find_if(first_pairs.begin(), first_pairs.end(), [&](std::pair<int, int> pair) {
            return pair.first == pos.first && pair.second == pos.second;
        });
        auto second = std::find_if(second_pairs.begin(), second_pairs.end(), [&](std::pair<int, int> pair) {
            return pair.first == pos.first && pair.second == pos.second;
        });
        steps.push_back(2 + first - first_pairs.begin() + second - second_pairs.begin());
    }
    std::cout << "Part 2: " << *std::min_element(steps.begin(), steps.end()) << std::endl;
}
