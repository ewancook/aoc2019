#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

int main() {
        auto part_one{0}, part_two{0};

        for (auto i = 109165; i <= 576723; i++) {
            std::string value = std::to_string(i);
             if (!std::is_sorted(value.begin(), value.end())) {
                 continue;
             }
             std::vector<int> ints(value.length());
             std::transform(value.begin(), value.end(), ints.begin(), [](char const& v) {
                 return v - '0';
             });
             auto ints_set = std::set<int>(ints.begin(), ints.end());
             if (ints_set.size() == ints.size()) {
                 continue;
             }
             part_one++;
             if (std::any_of(ints_set.begin(), ints_set.end(), [&ints](int const& v) {
                 return std::count(ints.begin(), ints.end(), v) == 2;
             })) {
                 part_two++;
             }
        }
        std::cout << "Part 1: " << part_one << '\n';
        std::cout << "Part 2: " << part_two << std::endl;
    }
