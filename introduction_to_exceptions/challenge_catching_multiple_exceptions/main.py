def safe_divide_from_string(number_str, divisor):
    try:
        number = int(number_str)             # 文字を数字に変えるよ
        result = 100 / number                 # 100をその数字で割るよ
        return result                         # うまくいったら結果を返すよ
    except ValueError:
        return "ValueError: invalid integer input"   # 数字じゃなかったときのこたえ
    except ZeroDivisionError:
        return "ZeroDivisionError: division by zero" # 0で割ろうとしたときのこたえ

# デバッグ用の呼び出し
a = safe_divide_from_string("10", 5)
b = safe_divide_from_string("0", 5)
c = safe_divide_from_string("abc", 5)
print(a)  # 10で割れば10.0 が出るよ
print(b)  # 0で割れないからエラーの文字が出るよ
print(c)  # abcは数字じゃないからエラーの文字が出るよ