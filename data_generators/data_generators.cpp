#include "data_generators.h"

#include <algorithm>
#include <random>

void generateRandomPermutation(std::vector<long long>& data, std::mt19937& rng) {
    std::iota(data.begin(), data.end(), 1);
    std::ranges::shuffle(data, rng);
}

void generateRandomRuns(std::vector<long long>& data, std::mt19937& rng, double lambda) {
    generateRandomPermutation(data, rng);
    size_t n = data.size();
    size_t i = 0;

    std::geometric_distribution geo(1.0 / lambda);  // mean = lambda
    while (i < n) {
        int run_length = geo(rng) + 1;
        if (i + run_length > n)
            run_length = n - i;
        std::sort(data.begin() + i, data.begin() + i + run_length);
        i += run_length;
    }
}