#!/usr/bin/env python3

from backpackInstance import BackpackInstance
from backpack_util import read_backpack_instances

import sys
import os

def separate_instances(instances_path, output_path):
    instances = read_backpack_instances(instances_path)

    for instance in instances:
        with open(os.path.join(output_path, f"{instance.name}.txt"), mode='x', encoding='utf-8') as f:
            print_instance(instance, f)
        print("*"*10, end='')
        print(f" {instance.name}")

def print_instance(instance : BackpackInstance, file=sys.stdout):
    print(f"{instance.name}", file=file)
    print(f"n {instance.n}", file=file)
    print(f"c {instance.capacity}", file=file)
    print(f"z {instance.getProfitSolution()}", file=file)
    for i in range(instance.n):
        print(f"{instance.getProfit()[i]}, {instance.getWeight()[i]}", file=file)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        instances_path = sys.argv[1]
        outputFolderPath = './'
    elif len(sys.argv) == 3:
        instances_path = sys.argv[1]
        outputFolderPath = sys.argv[2]
    else:
        print("\nUsage ./separate_instances <instances_path> <outputFolderPath>")
        sys.exit(1)
    
    separate_instances(instances_path, outputFolderPath)

