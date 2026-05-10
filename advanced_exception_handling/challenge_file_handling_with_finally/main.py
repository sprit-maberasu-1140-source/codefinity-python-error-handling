def read_file_contents(filename):
    # Your code here
    pass
    file = None
    conents = None
    try:
        file = open(filename,'r')
        contents = file.read()
    except Exception:
       print("An error occurred while reading the file.")
       contents = None
    finally:
        if file is not None:
            file.close()
    return contents
# Example usage for your testing:
with open('example.txt', 'w') as f:
    f.write('Hello, world!')
print(read_file_contents('example.txt'))
print(read_file_contents('nonexistent.txt'))
