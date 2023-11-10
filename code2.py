#not supported between instances of 'str' and 'int' 
def get_age():
    age_str = input("Please enter your age: ")
    if age_str.isnumeric() and int(age_str) >= 18:
        return int(age_str)
    else:
        return None

def main():
    age = get_age()
    if age is not None:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
