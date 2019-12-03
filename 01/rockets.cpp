#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

int calculate_fuel(int mass) {
	return std::floor((float)mass/3-2);
}

int main() {
	std::ifstream f("input.txt");
	std::vector<int> masses;
	std::string line;
	while(std::getline(f, line)) {
		if (line.size() > 0) {
			masses.push_back(std::stoi(line));
		}
	}

	int part_one{}, part_two{}, fuel{};
	for (auto const& mass: masses) {
		fuel = calculate_fuel(mass);
		part_one += fuel;
		while (fuel > 0) {
			part_two += fuel;
			fuel = calculate_fuel(fuel);
		}
	}
	std::cout << "Part 1: " << part_one << '\n';
	std::cout << "Part 2: " << part_two << std::endl;
}
