
import numpy as np
import pandas as pd

def find_two_numbers_sum_to_target(file_path, target):
    # Read the dataset
    ll = pd.read_csv(file_path, names=['nums'])

    # Sort the numbers , this is crucial step to search in the given scenario
    ll = np.sort(ll.nums)

    i = 0
    j = len(ll) - 1
    #### use the two pointer search method to traverse left or right depending on the amplitude of sum
    while i < j:
        if ll[i] + ll[j] == target:
            return ll[i], ll[j], ll[i] * ll[j]
        elif ll[i] + ll[j] < target:
            i += 1
        elif ll[i] + ll[j] > target:
            j -= 1

    return None, None, None


file_path = './dataset'
target = 2020
num1, num2, product = find_two_numbers_sum_to_target(file_path, target)


print(f"The two numbers that sum up to {target} are: {num1} and {num2}")
print(f"Product: {product}")
