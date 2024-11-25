import numpy as np
import pandas as pd

ll=pd.read_csv('./dataset',  names=['nums'] )

# print(ll)
ll=np.sort(ll.nums)
target=2020

def find_three_numbers(nums, target):

    n = len(nums)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return nums[i], nums[left], nums[right], nums[i]* nums[left]* nums[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None


x,y,z,q = find_three_numbers(ll, target)

if q:
    print(f"The three numbers that sum up to {target} are and their product is : {x},{y},{z},{q}")
