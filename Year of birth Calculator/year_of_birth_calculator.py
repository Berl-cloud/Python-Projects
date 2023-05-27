import datetime

def calculate_year_of_birth():
    """
    Calculates the year of birth based on the user's age.

    Parameters:
        None

    Returns:
        None: Only prints the calculated year of birth.
    """

    # Prompt the user to enter their age
    age = int(input("Enter your age: "))

    # Calculate the year of birth
    current_year = datetime.datetime.now().year
    year_of_birth = current_year - age

    # Display the calculated year of birth
    print("Your year of birth is:", year_of_birth)

# Call the function to calculate the year of birth
calculate_year_of_birth()
