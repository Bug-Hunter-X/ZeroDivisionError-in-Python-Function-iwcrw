def function(a, b):
    if b == 0:
        return "Division by zero"
    else:
        return a / b

result = function(10, 0)
print(result)  # Output: Division by zero
result = function(10, 2)
print(result)  # Output: 5.0