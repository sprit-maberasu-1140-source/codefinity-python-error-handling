def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# 使い方の例
print(safe_divide(10, 2))  # 5.0 と出るよ
print(safe_divide(5, 0))   # Cannot divide by zero. と出るよ