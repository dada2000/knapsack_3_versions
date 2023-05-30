#Knapsack with dynamic programming memoization

import time

### DYNAMIC CODEBASE (1x func only):
def value_output(weight_cap): #CALLED FROM main program --> #Neat string representation of output --> Only function called from main --> calls actual bruteforce_knapsack() from inside.
    max_val= dynamic_knapsack(weight_cap) #max_val: int  combo: Tuple of item-numbers e.g.: (1,4,6,7) from max_val combo for total weight cap of knapsack
    print(f"\n{45*'+'}\n{' KNAPSACK DYNAMIC (comparison): '.center(45,'+')}\n{' v1.7 '.center(45,'+')}\n")
    print(f"  MAX VALUE RESULTS --> WEIGHT-CAP: {weight_cap}  ".center(45, '*') + "\n")
    print(f"==> MAX COMBO TOTAL VALUE: {str(max_val):4}\n")
    #return max_val #Returns max value combo tuple

def dynamic_knapsack(weight_cap):
  rows = len(weights) + 1 #rows = 8 (incl 1. row at 0) #INDEX NAVI ORIENTATION ## Together define 2D Navi --> Y-Max!
  cols = weight_cap + 1 #cols = 51  (incl 1. col at 0) #COLS  NAVI ORIENTATION ## Together define 2D Navi --> X-Max!
  # Setting up 2D array with 0 defaults
  matrix = [ [0 for _ in range(cols)] for __ in range(rows) ] #Creates 2D - 0-matrix from 2x nested list comprehensions. --> rows 0-7 inclusive x 0-50 cols
  # Iterates through every row [Functions as current Y-Axis index(row) for navigation]
  for index in range(rows): #Y-Axis: Iterates through 0-7 rows with abs matrix index --> row0 = all 0 --> row1 == index 1 == item 1
    #Iterates through every col from 0 to weight-cap [Functions as current X-Axis weight(col) for navigation]
    for weight in range(cols): #X-Axis: Within outer for loop(index/item) this inner for loop(weight) iterates for each row 51x through the weights starting from 0
      #CHECKS FOR each index[x] and weight[y] combination the conditional-case to write according value in THAT matrix[x][y] CELL.
      if weight == 0 or index == 0: #Since range(cols) = 0-50 inclusive the first element of each col starts with 0 and therefore weight = 0. --> matrix[index][weight] = 0
        matrix[index][weight] = 0
      #MODDING !!!
      elif weights[index-1] <= weight: #As soon as the current_index element from rows (weights[index-1]) "fits in" the current_weight, the current max will be recalculates with the new element looking for the max value combination.
        include = (values[index-1] + matrix[index-1][weight - weights[index-1]])
        exclude = matrix[index-1][weight]
        matrix[index][weight] = max(include, exclude)
      else:
        matrix[index][weight] = matrix[index-1][weight]
  #print_matrix(matrix) #TOGGLE final Matrix display print output --> Uncomment to print()
  return matrix[-1][-1] #Returns tuple(max_value, combo)

def print_matrix(matrix): #CALLED FROM bruteforce_knapsack() #Prints matrix in string format for better visual representation --> 2D array as input matrix
    for rows in matrix:
        col = [f'{col:2}' for col in rows] #Transforms rows-list into new list with {str(int):2} f-strings --> Readability!
        print(col) 

###MAIN PROGRAM
#KNAPSACK START PARAMETERS: weights, values, weight_cap |--> Adjust as needed: len(weights) == len(values) !!
weight_cap = 50
name =    ["ruby", "vase", "clock", "ring", "gold", "lamp", "laptop"]
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
items = [i+1 for i in range(len(weights))] #[1, 2, 3, 4, 5, 6, 7]

#value_output(weight_cap)

