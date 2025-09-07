# Powersort Benchmark

- This repository is used for running _TimSort_ and _Powersort_ on the data of `Track A` of https://powersort-competition.github.io/PowersortCompetitionWebsite/
- The benchmark consists of one file (`main.cpp`), which includes most content from `numpy/_core/src/npysort/timsort.cpp` as well as the other _NumPy_ code it depends on, pasted into a section at the top.
- The results are averages over multiple repetitions per array, and are saved as CSV files. The wrangling and plotting of this data is done in another repository using `Python`, `Pandas`, `matplotlib`, etc.