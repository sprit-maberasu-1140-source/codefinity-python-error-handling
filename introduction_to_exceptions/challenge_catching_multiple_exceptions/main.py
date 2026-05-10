def safe_divide_from_string(number_str, divisor):
    # Your code here
    pass
    try:
        number = int(number_str)
        result = 100 / number
        return result
    except ValueError:
        return "ValueError:invalid integer input"
    except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"

# Example calls for debugging
a = safe_divide_from_string("10", 5)
b = safe_divide_from_string("0", 5)
c = safe_divide_from_string("abc", 5)
print(a)
print(b)
print(c)