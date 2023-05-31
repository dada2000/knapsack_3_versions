import time, datetime
import python_files.Knapsack_Bruteforce, python_files.Knapsack_Dynamic, python_files.Knapsack_Recursive

def benchmark(weight_cap): #Final comparison summary between normal and optimized Pascal triangle algorithms:
    
    ### FUNCTION CALLS - incl. print-out and stop-watch timings for each implementation type.
    start_time_bf = time.time()
    python_files.Knapsack_Bruteforce.value_output_bf(weight_cap) #Bruteforce knapsack implementation.
    end_time_bf = time.time()
    delta_bf = end_time_bf - start_time_bf

    start_time_dyn = time.time()
    python_files.Knapsack_Dynamic.value_output(weight_cap)
    end_time_dyn = time.time()
    delta_dyn = end_time_dyn - start_time_dyn

    start_time_recu = time.time()
    python_files.Knapsack_Recursive.commented_recu_ks(weight_cap, weights, values, len(weights), name)
    end_time_recu = time.time()
    delta_recu = end_time_recu - start_time_recu

    #TESTLINE

    ### FORMATTED BENCHMARK OUTPUT:
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f"\n{45*'*'}\n{' BENCHMARK RESULTS (Knapsack): '.center(45,'*')}\n{45*'*'}\n")
    print(f"START TIME: {time_now} \n--> {'Bruteforce':10}: {delta_bf*1000:.3f} ms\n--> {'Dynamic':10}: {delta_dyn*1000:.3f} ms\n--> {'Recursive':10}: {delta_recu*1000:.3f} ms\n")
    
    #print("\n" + f"{tri_width * '*'}" + "\n" + " BENCHMARKING ".center(tri_width, "*") + "\n" + f"{tri_width * '*'}")

    #std_time = print_pascal_triangle(num_rows, std_triangle, False) #Generates, prints STANDARD pascal triangle algorithm --> Returns delta execution time
    #opt_time = print_pascal_triangle(num_rows, opt_triangle, True) #Generates, prints OPTIMIZED pascal triangle algorithm --> Returns delta execution time
    
    #print(">>> RESULT: ", end = "")
    #if opt_time < std_time:
    #    print(f"OPTIMIZED algorithm ({opt_time * 1000 :.4f}ms) is about {round((std_time/opt_time),1)}x faster than STANDARD algorithm ({std_time * 1000 :.4f}ms)")
    #else:
    #    print(f"STANDARD algorithm ({std_time * 1000 :.4f}ms) is about {round((opt_time/std_time),1)}x faster than OPTIMIZED algorithm ({opt_time * 1000 :.4f}ms)")
    #print()

#KNAPSACK START PARAMETERS: weights, values, weight_cap |--> Adjust as needed: len(weights) == len(values) !!
weight_cap = 65
name =    ["ruby", "vase", "clock", "ring", "gold", "lamp", "laptop"]
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
items = [i+1 for i in range(len(weights))] #[1, 2, 3, 4, 5, 6, 7]

#print(Knapsack_Bruteforce.powerset_all_items_dict)

if __name__ == "__main__":
    benchmark(weight_cap)

#Track
#Changes in github