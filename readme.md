# Knapsack Problem: 
## Benchmarking runtime performance of 3 different implementations

### GENERAL:
* Bruteforce, recursive and dynamic solutions in Python in separate files.
* The main benchmark file is calling all 3 python files and prints their execution time statistics.
* Unified starting conditions (weight_cap, items, weights, values) can be adjusted centrally in the benchmarking file:
```
weight_cap = 65
name =    ["ruby", "vase", "clock", "ring", "gold", "lamp", "laptop"]
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
```
* All 3 python program implementations will then execute with those centrally defined starting conditions.
* Alternatively each Python program version can also be run independently by executing the file directly.

### BACKGROUND DETAILS:
* All Python files are annotated with detailed comments throughout all critical program passages.
* RECURSIVE IMPLEMENTATION: Recursively calls main function until basecase (either i == 0 or weight-cap == 0) is reached and then starts returning a tuple data structure with item_value and list of collected items. It decides on each recursive step (item i) if the returned value is higher with current item i included or excluded. --> Returns max_value, combination tuple and total amount of recursions called to retrieve max value.
* BRUTEFORCE IMPLEMENTATION: First creates superset dictionary for all possible combination sets for each set size i. Then iterates through 2D matrix array and bruteforces max value based on currently available weight capacity and available items. MAx value will always stored in last iterated bottom right matrix cell.
* DYNAMIC IMPLEMENTATION: Similar to bruteforce approach creates empty 2D matrix array (items X available_weight). But instead of checking all available combinations per cell iteration it compares the last row of max values VS. adding its own value instead. That way it also returns the max value by doing only 2 comparisons per cell iteration.

### RESULTS:
* As expected the bruteforce implementation is the slowest implementation and surprisingly the recursive and dynamic versions have similar execution times.
* On the other hand bruteforce is the most intuitive and probably easiest to follow version, since it basically iterates a 2D grid and runs the same max_combination retrieval algorithm each time.