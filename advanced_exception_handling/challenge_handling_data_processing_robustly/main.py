def read_file_contents(filename):
    # Your code here
    pass
    try:
       with open(filename,'r') as f:
           contents = f.read()
       print(contents)
    except FileNotFoundError:   
        print("Error: The file was not found.")
    except UnicodeDecodeError:
        print("Error: Could not decode the file contents.")


# Example calls for debug
def _create_test_files():
    # Create a valid file
    with open('example.txt', 'w') as f:
        f.write('Hello, world!')
    # Create a file with invalid utf-8 bytes
    with open('invalid.txt', 'wb') as f:
        f.write(b'\xff\xfe\xfd')

if __name__ == "__main__":
    _create_test_files()
    print("Valid file:")
    read_file_contents('example.txt')
    print("Nonexistent file:")
    read_file_contents('does_not_exist.txt')
    print("Invalid encoding file:")
    read_file_contents('invalid.txt')