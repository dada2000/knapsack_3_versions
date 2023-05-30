
### Knapsack Recursive Solution ###

#Recursively finds all possible (within remaining weight limit of each new (recursive) function call) combinations along (binary) tree recursion
#Recursive implementation works independently of the order of weights/values in the lists --> Recursion always retrieves same(correct) max value for same ...
# ...weight/value list even with shuffled order of same weight/value pairs. What changes though is structure of the recursion call tree (amount of rec calls)
#Recursion has i horizontal levels == amount of items(i) in the list --> Moves from highest item index number @right end (len(weights)) -> down the item list indices until base-case i = 0 reached.
  
#Here each new recursion corresponds to the next item along the weight/value lists being considered to be either included or skipped(excluded) -> 1 incl. AND 1 excl. rec call respectively
   #*==> Since it is not clear during recursion which trail will return the max_value --> All calling/return recursive tree pathes need to be tracked inside out.
   #*==> Result should be Tuple with max_value sum AND according list of tuple-items [(i,0/1)] --> Appending i-tuples inside out recursively --> Tracing max outwards(ex or in) and i
   #*==> 1.) APPROACH: In else case create i-Tuple (i, 0/1 ) --> IN/EX: Separate KS(wc,w,v,i) return results AND unpack prev i-Tuples from List[RetTuples(),...] 
             #...--> FIRST Determine Max(value) THEN append current i-tuple to accordingly to MAX (tuple list trail) from prev recursion return result (EITHER IN or EX recu) -> (append to right)... 
             #...--> Re-Pack updated & completed i-Tuples list (from MAX_VAL) together with max_val in new Return-Tuple structure: (max_val, List[i-Tuple1, i-Tuple2, ...])
             #...--> In case of Skipping: FIRST create new i-Tuple(i, 0), store recu-call result (R-Tuple(max_val,List[i-Tuple1, i-Tuple2, ...])) separated in var ...
             #...    Return new R-Tuple (max_val, List[i-Tuple1, i-Tuple2, ...]). -> Combines max_val and max_combo(path) in return tuple.

import argparse
from collections import Counter

def recursive_knapsack(weight_cap, weights, values, i): #CAREFUL: i represents abs item number (1-3) while indices work with i-1 --> e.g. Weight of item i = weights[i-1] !!
  global call_counter
  call_counter += 1
  caller = f"{'*' + '---'*(len(weights)-i)}> CALLING[No.{call_counter}] recu[{(len(weights)-i)}] from i:{i} and wc:{weight_cap} for NAME {name[i-1].upper()} - w: {weights} v: {values}"
  call_strings.append(caller) #Toggle to append all call strings to call_strings global list --> FOR DEBUGGING PURPOSES
  print(caller)
  if weight_cap == 0 or i == 0: #BC condition can be seen as "in between" 2 subsequent recursive calls bounce back: Prevents preparation of next recursive functions --> Instead directly returns 0!
    print(f"{'   '*(len(weights)-i) + ' ='} BASE case reached --> wc: {weight_cap} i: {i} w: {weights} v: {values}")
    return (0,[(i,0)]) #Return Tuple = (MaxVal, [(i, 0/1 )]) --> i tuple incl: (i,1), excluded (i,0)
  elif weights[i - 1] > weight_cap:
    print(f"{'S' + '   '*(len(weights)-i)}  SKIPPING! weight {weights[i-1]} > wc: {weight_cap} for i:{i} and NAME {name[i-1]} ==> NEXT CALL: i:{i-1}")
    prev_max, prev_tuples = recursive_knapsack(weight_cap, weights, values, i - 1) #Equivalent to exclusive recursive call from ELSE: case --> Skips current item i
    #cum.val, [list of tup]
    prev_tuples.append((i,0)) #Since current item i is always skipped in elif skip case --> appends to right
    print(f"{'R' + '   '*(len(weights)-i)}  <SKIP-RETURN case from i:{i} NAME {name[i-1].upper()} with prev_max value {prev_max} and tuples list: {prev_tuples}")
    return (prev_max, prev_tuples) #returns Tuple(max_val, [(i-2, 0), (i-1,1), (i,0)])
  
  else: #2 alternative recursions called both after another --> incl / excl current item i
    print(f"{'E' + '   '*(len(weights)-i)}  ELSE case from i:{i} and NAME {name[i-1].upper()} --> Loading IN and EX recursions...")
    
    print(f"{'-N' + '   '*(len(weights)-i)} -NEXT INCL case: Keeping item i:{i} {name[i-1].upper()} -> value:{values[i-1]} and calling INCL with i:{i-1}")
    current_val = values[i - 1] #Stores current value for i to conserve it for INCL recu call return. Since recu returns Tuple capsule that cannot be added directly. 
    in_prev_max, in_prev_tuples = recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1) #Extracts prev_max and prev_tuples
    in_prev_max += current_val #Combines prev_max for INCL case with previously stored value for i --> In order to prepare for max call.
    print(f"{'CI' + '   '*(len(weights)-i)} -CALCulated from i:{i} inclusive value = {in_prev_max} --> Calling EX recursion next...")
    
    print(f"{'-N' + '   '*(len(weights)-i)} -NEXT EXCL case: WITHOUT item i:{i} {name[i-1].upper()} and calling EXCL with i:{i-1}")
    ex_prev_max, ex_prev_tuples  = recursive_knapsack(weight_cap, weights, values, i - 1)
    print(f"{'CE' + '   '*(len(weights)-i)} -CALCulated from i:{i} exclusive value = {ex_prev_max} --> Calling MAX function: {in_prev_max}(INCL) VS. {ex_prev_max}(EXCL)")
    
    if in_prev_max > ex_prev_max:
      in_prev_tuples.append((i,1))
      maxi = (in_prev_max, in_prev_tuples)
      print(f"{'R' + '   '*(len(weights)-i)}  <RETURNING <INCL case> from i:{i} NAME {name[i-1].upper()}(val:{values[i-1]}) --> Max Value {maxi[0]} --> Tuple List:{maxi[1]}")
    else:
      ex_prev_tuples.append((i,0))      
      maxi = (ex_prev_max,ex_prev_tuples)
      print(f"{'R' + '   '*(len(weights)-i)}  <RETURNING <EXCL case> from i:{i} WITHOUT NAME {name[i-1].upper()} --> Max Value {maxi[0]} -->Tuple List:{maxi[1]}")
    return maxi #Maxi-Tuple for either IN or EX trail: Tuple(max_val, [(i-2, 0), (i-1,1), (i,0)])
  
def recursive_knapsack_silent(weight_cap, weights, values, i): #CAREFUL: i represents abs item number (1-3) while indices work with i-1 --> e.g. Weight of item i = weights[i-1] !!
  global call_counter
  call_counter += 1
  #print(f"{'*' + '---'*(len(weights)-i)}> CALLING[No.{call_counter}] recu[{(len(weights)-i)}] from i:{i} and wc:{weight_cap} for NAME {name[i-1].upper()} - w: {weights} v: {values}")
  if weight_cap == 0 or i == 0: #BC condition can be seen as "in between" 2 subsequent recursive calls bounce back: Prevents preparation of next recursive functions --> Instead directly returns 0!
    #print(f"{ '   '*(len(weights)-i) + ' ='} BASE case reached --> wc: {weight_cap} i: {i} w: {weights} v: {values}")
    return (0,[(i,0)])
  elif weights[i - 1] > weight_cap:
    #print(f"{'S' + '   '*(len(weights)-i)}  SKIPPING weight {weights[i-1]} for i:{i} and NAME {name[i-1]} ==> NEXT CALL: i:{i-1}")
    prev_max, prev_tuples = recursive_knapsack_silent(weight_cap, weights, values, i - 1) #Equivalent to exclusive recursive call from ELSE case --> Skips current item i
    #print(f"{'R' + '   '*(len(weights)-i)}  <SKIP-RETURN case from i:{i} NAME {name[i-1].upper()} with prev_max value {prev_max} and tuples list: {prev_tuples}")
    return (prev_max, prev_tuples + [(i,0)]) #returns Tuple(max_val, [(i-2, 0), (i-1,1), (i,0)]) and adds i-tuple to list
  else: #2 alternative recursions called both after another --> with / without current item i
    #print(f"{'E' + '   '*(len(weights)-i)}  ELSE case from i:{i} and NAME {name[i-1].upper()} --> Loading IN and EX recursions...")
    
    #print(f"{'-N' + '   '*(len(weights)-i)} -NEXT INCL case: Keeping item i:{i} {name[i-1].upper()} -> value:{values[i-1]} and calling INCL with i:{i-1}")
    current_val = values[i - 1] #Stores current value for i to conserve it for INCL recu call return. Since recu returns Tuple capsule that cannot be added directly. 
    in_prev_max, in_prev_tuples = recursive_knapsack_silent(weight_cap - weights[i - 1], weights, values, i - 1) #Extracts prev_max and prev_tuples
    in_prev_max += current_val #Combines prev_max for INCL case with previously stored value for i --> In order to prepare for max call.
    #print(f"{'CI' + '   '*(len(weights)-i)} -calculated from i:{i} inclusive value = {in_prev_max} --> Calling EX recursion next...")
    
    #print(f"{'-N' + '   '*(len(weights)-i)} -NEXT EXCL case: WITHOUT item i:{i} {name[i-1].upper()} and calling EXCL with i:{i-1}")
    ex_prev_max, ex_prev_tuples  = recursive_knapsack_silent(weight_cap, weights, values, i - 1)
    #print(f"{'CE' + '   '*(len(weights)-i)} -calculated from i:{i} exclusive value = {ex_prev_max} --> Calling MAX function: {in_prev_max}(INCL) VS. {ex_prev_max}(EXCL)")
    
    if in_prev_max > ex_prev_max:
      in_prev_tuples.append((i,1)) #Update path tuple list with current element i
      maxi = (in_prev_max, in_prev_tuples) #Build maxi tuple with max_val and tuple path list
      #print(f"{'R' + '   '*(len(weights)-i)}  <RETURNING <INCL case> from i:{i} NAME {name[i-1].upper()}(val:{values[i-1]}) --> Max Value {in_prev_max} --> Tuple List:{in_prev_tuples}")
    else:
      ex_prev_tuples.append((i,0))      
      maxi = (ex_prev_max,ex_prev_tuples)
      #print(f"{'R' + '   '*(len(weights)-i)}  <RETURNING <EXCL case> from i:{i} WITHOUT NAME {name[i-1].upper()} --> Max Value {maxi[0]} -->Tuple List:{ex_prev_tuples}")
    return maxi #Maxi-Tuple for either IN or EX trail: Tuple(max_val, [(i-2, 0), (i-1,1), (i,0)])

def value_output(max_value_tuple, weight_cap, weights, values, name): #Max_Tuple(max_val, [i=0, 0), (i=1,1), (i=2,1), ... , (i=len(weights),1)])
    max_val, max_tuples = max_value_tuple
    incl_tuples = filter(lambda x : x[1], max_tuples) #Creates FilterObject --> iterable ONLY ONCE! 
    max_weight = 0
    print(f"  MAX VALUE RESULTS --> WEIGHT-CAP: {weight_cap}  ".center(45, '*') + "\n")
    for idx,tuple in enumerate(incl_tuples):
      i = tuple[0]
      max_weight += weights[i-1]
      print(f"{idx+1}.) {name[i-1].upper():6} --> Weight: {weights[i-1]:2} - Value: {values[i-1]:2}")
    print("    " + 42*"=")
    print(f"==> MAX COMBO TOTAL WEIGHT: {max_weight:2} - VALUE: {str(max_val):4}")
    print(f"==> Retrieved in {call_counter}x total recursive calls.\n")

def string_eval(calll_strings, items = 7): #Used for debugging to analyze call strings i,wc parameters
  ###!!! ONLY !!! works when --comments version was run --> appended call-prints() to call_strings list.
  print("##############################################")
  print("### CODE BLOCK - CALLING STRING EVALUATION ###")
  print("##############################################\n")
  #  
  ### START CONDITIONS CODE BLOCK ### --> Create {i:[wc1, wc2, ...]} dict. Crops rec level indicator arrows
  iwc_dict = {i:[] for i in range(items+1)} #Default 0 - 7 incl.

  for list_idx, test_string in enumerate(calll_strings): #Iterate by index
    ### REMOVE "*---->"" CODE BLOCK ### --> Removes arrow from string and updates same in original list
    calll_strings[list_idx] = test_string[test_string.find("CALL"):]
    
    ### i-FINDER CODE BLOCK ### --> Finds entire multidigit i-number --> Input: CALLING string("test_string") --> Output: converts i-number "i_string" to i_int
    i_idx = test_string.find("i:")+2 #Shifts idx to first i-digit
    i_string = ""
    while test_string[i_idx].isdecimal():
      i_string += test_string[i_idx]
      i_idx += 1
    i_int =  int(i_string)
    #print("i",i_int)

    ### wc-FINDER CODE BLOCK ### --> Finds entire multidigit wc-number --> Input: CALLING string("test_string") --> Output: converts wc-number "wc_string" to wc_int
    wc_idx = test_string.find("wc:")+3 #Shifts idx to first i-digit
    wc_string = ""
    while test_string[wc_idx].isdecimal():
      wc_string += test_string[wc_idx]
      wc_idx += 1
    wc_int = int(wc_string)
    #print("wc",wc_int)

    ### iwc-DICT-APPENDER CODE BLOCK ### --> Appends wc_int from current for iteration to iwc[i_int].append(wc_int)
    iwc_dict[i_int].append(wc_int)
  # Dict sorting and printer
  print("IWC_DICT Output:")
  for k,v in iwc_dict.items():
    v.sort()
    v = Counter(v)
    print(f"i = {k} --> wc's = {v}\n")
  return iwc_dict
  # Sort dict value lists in asc order for quick visual inspection TBC

call_counter = 0 #Set to global from within function to updated call_counter from inner namespace.
call_strings = []

#SMALLER TEST DATA SET --> Uncomment if needed
#name = ["ruby", "vase", "clock", "BASECASE"] #IMPORTANT: Base-Case needs to remain on name[-1] last position!!!
#weight_cap = 6
#weights = [1,5,3]
#values = [250, 500, 300]

#ALL 7 ITEMS DATA SET
#weight_cap = 65
#name =    ["ruby", "vase", "clock", "ring", "gold", "lamp", "laptop", "BASECASE"]
#weights = [31, 10, 20, 19, 4, 3, 6]
#values =  [70, 20, 39, 37, 7, 5, 10]

parser = argparse.ArgumentParser(prog="Recursive Knapsack")
parser.add_argument("-c", "--comments", action="store_true") 
args = parser.parse_args()

def commented_recu_ks(weight_cap,weights, values, i, name):
  ### ARGS CONDITIONAL FOR SILENT/COMMENTED MODE --> Initial REC[0] call:
  if not args.comments: #Process to create and return max value tuple through recursion either with comments&tree or compact.
    print(f"\n{45*'+'}\n{' KNAPSACK RECURSIVE (uncommented): '.center(45,'+')}\n{' v1.5 '.center(45,'+')}\n")
    max_value_tuple = recursive_knapsack_silent(weight_cap, weights, values, i) #Calls SILENT VERSION with start-conditions: e.g. with 3 items --> amount_items != index (idx = item -1)
  else: #When program is called with -c argparse --> Mainly to see complete recursion details and stats for bugfixing.
    print(f"\n{45*'+'}\n{' KNAPSACK RECURSIVE (with tree): '.center(45,'+')}\n{' v1.5 '.center(45,'+')}\n")
    max_value_tuple = recursive_knapsack(weight_cap, weights, values, i) # Calls COMMENTED VERSION with start-conditions: e.g. with 3 items --> amount_items != index (idx = item -1)
    iwc_dict = string_eval(call_strings, len(weights)) #ONLY works when --comments version was run --> appended call-prints() to call_strings list.
  value_output(max_value_tuple, weight_cap, weights, values, name) #Prints out previously created max tuple data --> Nice representation in CLI

#commented_recu_ks()