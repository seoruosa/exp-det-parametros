from multiprocessing.pool import ThreadPool
import subprocess
import os
import argparse


def work(sample):
    my_tool_subprocess = subprocess.Popen('../src/sa_backpack.py {} --alfa 0.98 --iterMaxTemp 30 --initialTemperature 250 --finalTemperature 0.1'.format(sample),shell=True, stdout=subprocess.PIPE)
    my_tool_subprocess.wait()
    line = True
    while line:
        myline = my_tool_subprocess.stdout.readline()
        if len(myline) > 0:
            line = False
        #here I parse stdout..

def run(all_samples):
    num = 3  # set to the number of workers you want (it defaults to the cpu count of your machine)
    tp = ThreadPool(num)
    
    for sample in all_samples:
        tp.apply_async(work, (sample,))

    tp.close()
    tp.join()

def list_test_instances(trainFolderPath, testFolderPath):
    filesList = lambda path: [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]

    train_instances = set(filesList(trainFolderPath))

    test_instances = filesList(testFolderPath)
    
    return [instance for instance in test_instances if instance not in train_instances]

# https://stackoverflow.com/questions/38834378/path-to-a-directory-as-argparse-argument        
def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("trainedPath", type=dir_path)
    parser.add_argument("testPath", type=dir_path)
    parser.add_argument("-n", "--nRuns", type=float, required=True, help="Select the number of runs per instance")
    args = parser.parse_args()

    RUNS_PER_INSTANCE = int(args.nRuns)
    trainedPath = args.trainedPath
    testPath = args.testPath

    # print(trainedPath)
    # print(testPath)

    test_instances = list_test_instances(trainedPath, testPath)

    # runned_instances = set(['knapPI_16_50_1000_4.txt', 'knapPI_16_50_1000_92.txt', 'knapPI_16_50_1000_82.txt', 'knapPI_16_50_1000_33.txt', 'knapPI_16_50_1000_50.txt'])

    # all_runs = [os.path.join(testPath, instance) for instance in test_instances for i in range(RUNS_PER_INSTANCE) if instance not in runned_instances]
    
    all_runs = [os.path.join(testPath, instance) for i in range(RUNS_PER_INSTANCE) for instance in test_instances]
    
    run(all_runs)

    