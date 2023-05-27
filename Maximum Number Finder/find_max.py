def find_max(numbers):
    """
    Finds the maximum number in a given list of numbers.

    Parameters:
        numbers (list): A list of numbers.

    Returns:
        int: The maximum number from the list.
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def main():
    """
    Main function to prompt the user for a list of numbers and find the maximum number.
    """
    numbers_input = input("Enter a list of numbers, separated by commas: ")
    numbers_list = [int(num) for num in numbers_input.split(",")]
    max_num = find_max(numbers_list)
    print("The largest number is", max_num)


# Call the main function
if __name__ == "__main__":
    main()
