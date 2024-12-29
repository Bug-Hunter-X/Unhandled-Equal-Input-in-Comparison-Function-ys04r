def my_function(a, b):
    if a >= b:
        return a
    return b

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-3, 0)
print(result)  # Output: 0

# Fixed: Now handles the case where both inputs are equal
result = my_function(5, 5)
print(result)  # Output: 5