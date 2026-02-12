#  Given an array arr, rotate the array by one position in clockwise direction. 

def rotate_clockwise(arr):
    return [arr[-1]] + arr[:-1]


arr = [1, 2, 3, 4, 5]
result = rotate_clockwise(arr)

print("Rotated array:", result)