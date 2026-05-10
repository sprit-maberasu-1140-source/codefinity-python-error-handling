def convert_and_report(s):
    # Your code here
    pass
    try:
        value = int(s)
    except ValueError:
        print("Conversion failed: invalid integer")
    else:
        print(f"Conversion successful:{value}")

convert_and_report('42')
convert_and_report('abc')
