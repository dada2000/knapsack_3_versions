#Knapsack with Bruteforce algorithm for all possible combinations with itertools.combinations(n,r) --> Version 1.0
###### Contains value_output(), powerset(), max_finder() ,bruteforce_knapsack() --> creates 2D array and works/checks all combinations --> Returns max_value(tuple)
import itertools #For nCr combinations calculations with itertools.combinations(n,r)

### BRUTEFORCE CODEBASE (5x funcs)
def powerset_all_items(max_idx): #Called ONCE to create intitial powerset of all items (max_idx = total amount of items) --> For precise indexing throughout program
    powerset_dict = dict()
    for w in range(1, max_idx+1): #range of all items (incl.) starting from 1
        per_w = [] #list container to store powerset for current w iteration (all possible wCi combinations) for each iteration of i (increasing from 1 to w) [inner for loop]
        for i in range(1, w+1):
            combo = list(itertools.combinations(items[:w],i)) #Combinations per i=r iteration for items-number-list [1, 2, 3, 4, 5, 6, 7]
            per_w += combo #concatenates current wCi combinations list to overall per_w list for this outer w iteration.
        powerset_dict[w] = per_w #appends completed powerset for outer for loop w iteration to dict (w : combo_list)
    return powerset_dict #Returns powerset_dict with {i <from 1 to len(weights)> : combos <(1,3),(1,4,5), ...>} with i = abs. item number.

def value_output_bf(weight_cap): #CALLED FROM main program --> #Neat string representation of output --> Only function called from main --> calls actual bruteforce_knapsack() from inside.
    max_val, combo = bruteforce_knapsack(weight_cap) #max_val: int  combo: Tuple of item-numbers e.g.: (1,4,6,7) from max_val combo for total weight cap of knapsack
    print(f"\n{45*'+'}\n{' KNAPSACK BRUTEFORCE (combinatorics): '.center(45,'+')}\n{' v1.2 '.center(45,'+')}\n")
    #print(f"\nBRUTEFORCE Max value ({max_val}) combination with weight cap of {weight_cap} consists of {len(combo)}x items:")
    
    #RECU IMPORT START
    print(f"  MAX VALUE RESULTS --> WEIGHT-CAP: {weight_cap}  ".center(45, '*') + "\n")
    for idx, i in enumerate(combo):
      print(f"{idx+1}.) {name[i-1].upper():6} --> Weight: {weights[i-1]:2} - Value: {values[i-1]:2}")
    print("    " + 42*"=")
    print(f"==> MAX COMBO TOTAL WEIGHT: {sum([weights[i-1] for i in combo]):2} - VALUE: {str(max_val):4}\n")
    #RECU IMPORT END
    return (max_val, combo) #Returns max value combo tuple
  
def bruteforce_knapsack(weight_cap): #CALLED ONCE from value output() --> #Main function --> Called with weight_cap limit --> Then automatically generates 2D array --> Iterates through all index/weight combinations --> Stores max_value in 2D array cell --> Returns max_value Tuple(int, combo)
  rows = len(weights) + 1 #rows = 8 (incl 1. row at 0) #INDEX NAVI ORIENTATION ## Together define 2D Navi --> Y-Max!
  cols = weight_cap + 1 #cols = 51  (incl 1. col at 0) #COLS  NAVI ORIENTATION ## Together define 2D Navi --> X-Max!
  # Setting up 2D array with 0 defaults --> nested list
  matrix = [ [0 for _ in range(cols)] for __ in range(rows) ] #Creates initial 2D - "0"-matrix from 2x nested list comprehensions. --> rows 0-7 inclusive x 0-50 cols (e.g. 8x51)
  # Iterates through every row (outer for loop) [Functions as current Y-Axis index(row) for navigation]
  for index in range(rows): #Y-Axis: Iterates through 0-7 rows with abs matrix index --> row0 = all 0 --> row1 == index 1 == item 1
    #Iterates through every col from 0 to weight-cap [Functions as current X-Axis weight(col) for navigation]
    for weight in range(cols): #X-Axis: Within outer for loop(index/item) this inner for loop(weight) iterates for each row 51x through the weights starting from 0
      #CHECKS FOR each index[x] and weight[y] combination the conditional-case to write according value in THAT matrix[x][y] CELL.
      if weight == 0 or index == 0: #Since range(cols) = 0-50 inclusive the first element of each col starts with 0 and therefore weight = 0. --> matrix[index][weight] = 0
        matrix[index][weight] = 0
      elif weights[index-1] <= weight: #IF the weight of the element at the current index (weights[index-1]) "fits in" the currently available weight-capacity (weight) 
                                       #--> THEN the max possible value will be recalculated with max_finder() -> returns max value combination tuple (max_val, item_combo).
        max_val, combo = max_finder(weight, index) #Calls and stores max value tuple(max_value, combo)
        matrix[index][weight] = max_val #Stores new_max value in 2D array cell
      else:
        matrix[index][weight] = matrix[index-1][weight]
  #print_matrix(matrix) #TOGGLE final Matrix display output --> Uncomment
  return max_val, combo #Returns tuple(max_value, combo) --> Last iteration of outer + inner for loops returns always max_val!
  
def max_finder(weight, index): #CALLED FROM bruteforce_knapsack() --> #Abs matrix index == item no. -> Gets called for each increment of grid cell to recalculate max value combination for currently available index-1 elements (from weights and values) within weight limit.
    max_value = (0,(0,0)) #(combo_value, (item-number-combo-tuple))
    #Construct relevant powers_list
    for combo in powerset_all_items_dict[index]: # powerset_dict access to sublist of item-number-combos --> iterates through all possible tuples (incl. overweight ones) in sublist
        combo_weight = sum([weights[i-1] for i in combo]) #Creates (temp) weights combo TUPLE from item-number-tuple
        if combo_weight <= weight: #IF Combo tuple's weight SUM fits in current weight limit in matrix grid point (index, weight)
           combo_value = sum([values[i-1] for i in combo]) #Total Value of combo as sum of dictionary comprehension retrieving values through .get(weights)
           if combo_value > max_value[0]: #Check if combo value > prev max
              max_value = (combo_value, combo) 
    return max_value #Returns max_value --> Tuple#(combo_value, (combo-item-number-tuple)) for available items up to index.

def print_matrix(matrix): #CALLED FROM bruteforce_knapsack() #Prints matrix in string format for better visual representation --> 2D array as input matrix
    for rows in matrix:
        col = [f'{col:2}' for col in rows] #Transforms rows-list into new list with {str(int):2} f-strings --> Readability!
        print(col) 

###MAIN PROGRAM
#KNAPSACK START PARAMETERS: weights, values, weight_cap |--> Adjust as needed: len(weights) == len(values) !!
weight_cap = 65
name =    ["ruby", "vase", "clock", "ring", "gold", "lamp", "laptop"]
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
items = [i+1 for i in range(len(weights))] #[1, 2, 3, 4, 5, 6, 7]

powerset_all_items_dict = powerset_all_items(len(weights)) #Creates initial powerset dict for all possible item combinations.
#max_val, combo = value_output_bf(weight_cap) #Creates print output format and generates bruteforce knapsack implementation.