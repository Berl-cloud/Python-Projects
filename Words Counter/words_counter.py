# Prompt the user to enter the file path
file = input('Enter file path: ')

# Open the file specified by the user for reading
handle = open(file)

# Initialize an empty list to store the words
words = []

# Iterate through each line in the file
for line in handle:
    # Split each line into words using the space character as the delimiter
    for word in line.split(' '):
        # Append each word to the words list
        words.append(word)

# Print the total number of words
print(f'There are {len(words)} words in the file')
