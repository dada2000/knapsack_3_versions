# KNAPSACK SOLUTION:
## BENCHMARKING 3 DIFFERENT IMPLEMENTATIONS
### GENERAL:
* Bruteforce, recursive and dynamic solutions for Knapsack problem in Python in 3 separate files.
* The main benchmark file is calling all 3 python files --> Each implementation prints their own result summary followed by the general benchmark statistics output.
* Unified starting conditions (weight_cap, items, weights, values) can be adjusted centrally in the benchmarking file:
```
weight_cap = 65
name =    ["ruby", "vase", "clock", "ring", "gold", "lamp", "laptop"]
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
```
* All 3 python program implementations will then execute using those centrally defined starting conditions.
* Alternatively each Python program version can also be run directly by executing the respective Python file.
* O(N) runtimes (approx.) can be found in the table below:

| Bruteforce    | Recursive   | Dynamic  XX |
| ---------------------- | ----------- | ------------- |
| *O(N^2 * weight_cap)*  | Content Cell  | Content Cell  |

### BACKGROUND DETAILS:
* All Python files are annotated with detailed comments throughout all critical program passages.
* RECURSIVE IMPLEMENTATION: Recursively calls main function until basecase (either i == 0 or weight-cap == 0) is reached and then starts returning a tuple data structure with item_value and list of collected items. It decides on each recursive step (item i) if the returned value is higher with current item i included or excluded. --> Returns max_value, combination tuple and total amount of recursions called.
* BRUTEFORCE IMPLEMENTATION: First creates superset dictionary for all possible combination sets for each all set sizes of i. Then iterates through 2D matrix array and bruteforces max value based on currently available weight capacity and available items from superset dictionary. Max value will always be stored in last iterated (bottom right) matrix cell.
* DYNAMIC IMPLEMENTATION: Similar to bruteforce approach an empty 2D matrix array is created (items X available_weight). But instead of checking *ALL* available combinations per cell iteration it only compares the last row of max values VS. adding its own value instead. That way it also returns the max value by doing only *2 comparisons* per cell iteration.

### RESULTS:
* As expected the bruteforce implementation is the *slowest* implementation and surprisingly the recursive and dynamic versions have similar execution times (~50x faster than bruteforce).
* On the other hand bruteforce is the most intuitive and probably *easiest* to follow version, since it basically iterates a 2D grid and runs the same max_combination retrieval algorithm each time.