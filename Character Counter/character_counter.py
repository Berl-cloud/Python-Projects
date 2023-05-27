def count():
    """
        Counts the number of times a letter appears in a word.

        Parameters:
            None

        Returns:
            None: Only prints the letter's frequency in the word.
    """

    word = input("Enter a word: ")  # Prompt the user to enter a word
    letter = input("Enter a letter: ")  # Prompt the user to enter a letter
    count = 0  # Initialize a variable to keep track of the letter's frequency

    # Iterate through each character in the word
    for char in word:
        if char == letter:  # Check if the current character is equal to the specified letter
            count += 1  # Increment the count variable if the condition is true

    # Print the letter and its frequency in the word
    print(f"The letter '{letter}' appears {count} times in the word '{word}'.")

# Call the function to count the occurrences of a letter in a word
count()
