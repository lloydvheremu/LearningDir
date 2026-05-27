#include <iostream>
#include <vector>


int main() {
	std::vector<std::string> messages = {"Hello", "from", "Kickstart", "Neovim!"};
	for (const auto& word :messages) {
      		std::cout << word << " ";
	}
	std::cout << std::endl;
	return 0;
}
