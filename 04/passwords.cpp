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
             auto values_set = std::set<int>(value.begin(), value.end());
             if (values_set.size() == value.length()) {
                 continue;
             }
             part_one++;
             if (std::any_of(values_set.begin(), values_set.end(), [&value](int const& v) {
                 return std::count(value.begin(), value.end(), v) == 2;
             })) {
                 part_two++;
             }
        }
        std::cout << "Part 1: " << part_one << '\n';
        std::cout << "Part 2: " << part_two << std::endl;
    }
