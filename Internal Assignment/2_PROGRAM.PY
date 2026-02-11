# Given an array arr[]. Your task is to find the minimum and maximum elements in the array

def find_min_max(arr):
    return [min(arr), max(arr)]

arr = list(map(int, input("Enter numbers separated by space: ").split()))

result = find_min_max(arr)
print("Minimum and Maximum values are:", result)