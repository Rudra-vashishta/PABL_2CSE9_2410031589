#  Given an array arr[]. The task is to find the largest element and return it. 

def largest_element (list1):
    largest=0
    for num in (list1):
        if num > largest:
            largest = num 
    return largest 




list1=[1,20,3,2,56,78,92,100,60,92,105,120,200]

result=largest_element(list1)
print (f'The largest element in the array is  {result}')

