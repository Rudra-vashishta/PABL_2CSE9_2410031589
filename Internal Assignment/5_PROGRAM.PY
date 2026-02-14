#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

def kth_element(nums,kth):
    nums.sort()
    print(nums)

    for i in range (1,len(nums)):
        if i == kth:
            return nums[i-1] 

    else:
        return -1


kth:int=5
nums= [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
result = kth_element(nums,kth)
print(f'kth element is {result}')

