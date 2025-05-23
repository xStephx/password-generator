import random
import string
import sys

# --------------------------- HELP MENU ---------------------------

# Check if user passed '--help' or '-h'
if sys.argv[1:] == ["-h"] or sys.argv[1:] == ["--help"]:
    print("\nPassword Generator Help Menu")
    print("\nUsage: Just run the script and follow the prompts.")
    print("You will be asked what kind of characters to include in your password(s),")
    print("and how many passwords you want to generate.\n")
    print("Options:")
    print("  - Lowercase letters (a-z)")
    print("  - Uppercase letters (A-Z)")
    print("  - Numbers (0-9)")
    print("  - Symbols (e.g., !, @, #, $)")
    print("You can generate multiple passwords of any length.\n")
    print("To exit the script, simply type 'exit' when prompted to generate more passwords.")
    sys.exit()

# Warn if unexpected argument(s) are passed
if sys.argv[1:]:
    print(f"\nWarning: Unexpected argument(s): {' '.join(sys.argv[1:])}")
    print("Please run the script without extra arguments or use '--help' for usage instructions.")
    sys.exit()

# ------------------------ MAIN PROGRAM --------------------------

# Function for welcome message
def welcome_message():
    logo = r"""
    	 \ | /         
    	 - * -      
    	  /|\        
     	 /\|/\      
     	/  |  \      
       /\/\|/\/\    
      /    |    \   
     -     -     -
  Password Generator v1.0 
    """
    print(logo)
    print("\nWelcome to the Password Generator! v1.0\n")
    
welcome_message()

# Function to ask the user a yes/no question
def get_yes_no(prompt):
    while True:
        response = input(prompt + " (Y/n): ").strip().lower()
        if response in ["y", "yes", "", "n", "no"]:  # Accept short or full responses
            return response in ["y", "yes", ""]  # Return True for yes
        else:
            print("Please enter 'y', 'n', or press Enter for yes.")

# Function to get a positive integer input from the user
def get_positive_integer(prompt):
    while True:
        value = input(prompt).strip()
        if not value.isdigit() or value.startswith("0"):
            print("Please enter a valid positive number.")
            continue
        value = int(value)
        return value

# Function to generate passwords based on user's input
def generate_passwords():
    # Ask the user what character types to include
    include_lowercase = get_yes_no("Include lowercase letters?")
    include_uppercase = get_yes_no("Include uppercase letters?")
    include_digits = get_yes_no("Include digits?")
    include_symbols = get_yes_no("Include symbols?")
    
    # Build a string of all allowed characters
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase  # a-z
    if include_uppercase:
        characters += string.ascii_uppercase  # A-Z
    if include_digits:
        characters += string.digits  # 0-9
    if include_symbols:
        characters += string.punctuation  # All special characters

    # Ask how many passwords to generate and their length
    num_passwords = get_positive_integer("\nHow many passwords do you want to generate? ")
    length = get_positive_integer("Length of each password: ")

    # Display the generated passwords
    print("\nGenerated Passwords:\n")
    for i in range(num_passwords):
        # Create one password by randomly choosing characters from the allowed set
        password = ''.join(random.choice(characters) for i in range(length))
        print(password)

# Main loop to allow generating passwords again without restarting the program
while True:
    generate_passwords()
    again = input("\nPress Enter to generate more passwords or type 'exit' to quit: ").strip().lower()
    if again == "exit":
        print("Goodbye!")
        break  # Exit the loop and end the program
