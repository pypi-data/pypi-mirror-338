#include <iostream>
#include <random>
#include <algorithm>

#include "../src/mipp.h"

int main(int argc, char** argv)
{
	std::random_device rd;
	std::mt19937 g(rd());

	using type = float;

	type t_1[mipp::nElReg<type>()];
	for (auto i = 0; i < mipp::nElReg<type>(); i++) t_1[i] = i;
	std::shuffle(t_1, t_1 + mipp::nElReg<type>(), g);

	mipp::Reg<type> in_1 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
	mipp::Reg<type> in_2 = 12;
	mipp::Reg<type> in_3 = t_1;

	std::cout << "Input vectors: " << std::endl;
	std::cout << "in_1 = " << in_1 << std::endl;
	std::cout << "in_2 = " << in_2 << std::endl;
	std::cout << "in_3 = " << in_3 << std::endl;

	return 0;
}
