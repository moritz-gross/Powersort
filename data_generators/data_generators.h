//
// Created by Moritz Groß on 06.04.25.
//

#ifndef DATA_GENERATORS_H
#define DATA_GENERATORS_H
#include <random>

void generateRandomPermutation(std::vector<long long>& data, std::mt19937& rng);
void generateRandomRuns(std::vector<long long>& data, std::mt19937& rng, double lambda);

#endif //DATA_GENERATORS_H
