#!../src/env_exp_irace/bin/pypy3

import argparse
from backpackInstance import BackpackInstance
from backpack_util import read_backpack_instance
from sa import SA

# import time
import numpy as np
from time import monotonic, asctime
import sys

OUTPUT_FILE_PATH = "../tuning/sa_backpack.log"
CSV_FILE_PATH = "../tuning/sa_backpack_results.csv"

def solve(instance:BackpackInstance, alfa, iter_max_temp, temp_ini, temp_end):
    w = instance.getWeight()
    p = instance.getProfit()
    capacity = instance.capacity

    vector_calc = lambda x, vector: sum([vector[i] for i, el in enumerate(x) if el])
    
    objective = lambda x, profit, weight, capacity: -(vector_calc(x, profit) - 10*max(0, vector_calc(x, weight) - capacity))

    f = lambda x: objective(x, p, w, capacity)

    def N(x):
        mod_idx = np.random.randint(0, len(x) - 1)
        return [(el if mod_idx != i else (el + 1)%2) for i, el in enumerate(x)]

    
    sol_ini = [0 for i in range(len(w))]
    
    sol_is_feasible = lambda x: vector_calc(x, w) < capacity

    s = SA(f, N, alfa, iter_max_temp, temp_ini, sol_ini, temp_end, sol_is_feasible)
    
    # print(f(s))
    return f(s)

def print_config(instance, alfa, iter_max, t0, tf, out_file=sys.stderr):
    print(f"name:  {instance.name}", file=out_file)
    print(f"n   {instance.n}", file=out_file)
    print(f"best_sol   {instance.getProfitSolution()}", file=out_file)
    print(f"{asctime()}", file=out_file)
    print(f"alfa:  {alfa}   itMax: {iter_max}   t0: {t0}    tf: {tf}", file=out_file)

def print_table(instance, alfa, iter_max, t0, tf, sol, duration, out_file=sys.stderr):
    print(f"{asctime()}, {instance.name}, {instance.n}, {alfa}, {iter_max}, {t0}, {tf}, {sol}, {instance.getProfitSolution()}, {duration}", file=out_file)    
    # print(f"", file=out_file)
    # print(f"", file=out_file)
    


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=argparse.FileType('r'))
    parser.add_argument("-a", "--alfa", type=float, required=True, help="Select alfa value")
    parser.add_argument("-itMax", "--iterMaxTemp", type=int, required=True, help="Maximum number of iterations on temp (multiplier in relation of number of elements)")
    parser.add_argument("-t0", "--initialTemperature", type=float, required=True, help="Initial temperature")
    parser.add_argument("-tf", "--finalTemperature", type=float, required=True, help="Initial temperature")
    args = parser.parse_args()
    
    instance = read_backpack_instance(args.instance.name)

    alfa = args.alfa
    iterMaxTemp = args.iterMaxTemp*instance.n

    initialTemperature = args.initialTemperature
    finalTemperature = args.finalTemperature
    
    with open(OUTPUT_FILE_PATH, mode='a') as f:
        print_config(instance, alfa, iterMaxTemp, initialTemperature, finalTemperature, f)

        tic = monotonic()
        sol = solve(instance, alfa, iterMaxTemp, initialTemperature, finalTemperature)
        toc = monotonic()

        print(f"sol:    {sol}   ", end='', file=f)
        print(f"duration:   {(toc - tic)}", file=f)
        print(f"*"*50, file=f)
        print(f"\n", file=f)

        print(sol)

    with open(CSV_FILE_PATH, mode='a') as f:
        print_table(instance, alfa, iterMaxTemp, initialTemperature, finalTemperature, sol, (toc - tic), f)
    