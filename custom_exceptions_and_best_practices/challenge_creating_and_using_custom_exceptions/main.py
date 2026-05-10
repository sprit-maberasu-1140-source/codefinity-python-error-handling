class NegativeNumberError(Exception):
    pass

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError("Negative number provided")
    return num

# Example usage
test_values = [5, -3]
for val in test_values:
    try:
        result = check_positive_number(val)
        print(f"Returned: {result}")
    except NegativeNumberError:
        print("You entered a negative number!")
