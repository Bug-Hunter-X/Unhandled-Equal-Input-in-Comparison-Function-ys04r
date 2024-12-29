def my_function(a, b):
    if a > b:
        return a
    return b

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-3, 0)
print(result)  # Output: 0

# Bug: The function does not handle the case where both inputs are equal
result = my_function(5, 5)
print(result) # Output: 5 (Incorrect, should ideally return one of them)