import os
import numpy as np

if __name__ == "__main__":
    TRAIN_PERCENTAGE = 0.05

    tuning_instance_path = "../tuning/instances/"

    if not(os.path.exists(tuning_instance_path)):
        os.makedirs(tuning_instance_path)

    path = "../instances"
    for f in os.listdir(path):
        dir_path = os.path.join(path, f)
        if os.path.isdir(dir_path):
            print(f)
            instances_list = [file for file in os.listdir(dir_path)]
            n_instances_to_train = int(TRAIN_PERCENTAGE * len(instances_list))
            
            a = np.random.permutation(instances_list)

            for instance in (a[:n_instances_to_train]).tolist():
                os.popen(f"cp {os.path.join(dir_path, instance)} {tuning_instance_path}")