#logical error in the program  the code will raise a FileNotFoundError
#o handle this, you can add a check to see if the file exists before attempting to read it. 
def read_and_write_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Convert content to uppercase
        uppercase_content = content.upper()

        with open(filename, 'w') as file:
            file.write(uppercase_content)

        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()
