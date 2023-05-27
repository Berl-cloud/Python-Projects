# Word Count

## About Project

This project consists of a Python program that counts the number of words in a file. The program prompts the user to enter a file path, reads the file, and then counts the words in it.

## Problem Statement

Given a file, the task is to count the number of words present in the file.

## Algorithm

The algorithm used in this code is as follows:

1. Prompt the user to enter the file path.
2. Open the file specified by the user for reading.
3. Initialize an empty list `words` to store the words.
4. Iterate through each line in the file.
5. Split each line into words using the space character as the delimiter.
6. Append each word to the `words` list.
7. After processing all lines in the file, calculate the length of the `words` list, which represents the number of words.
8. Print the number of words.

## Python Skills Learned

By studying and working with this code, you can improve your understanding of the following Python skills:

- File handling
- Looping through lines in a file
- Splitting strings into words
- List manipulation and length calculation
- String formatting

## Installation

No installation is required for this project. Simply copy the code and run it in a Python environment.

## Usage

To use the word count program, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the word count program:
```bash
python word_count.py
```
4. Enter the file path when prompted.
5. The program will read the file and count the number of words.
6. The result will be printed as the total number of words.