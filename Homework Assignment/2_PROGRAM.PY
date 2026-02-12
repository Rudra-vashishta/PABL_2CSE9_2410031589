
# You are given two arrays a[] and b[], return the Union of both the arrays in any order. 

def find_union(a, b):
    union = []
    
    for num in a:
        if num not in union:
            union.append(num)
            
    for num in b:
        if num not in union:
            union.append(num)
    
    return union

# Example
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

result = find_union(a, b)
print("Union of arrays:", result)