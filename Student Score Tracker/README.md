# Student Score Tracker

## About Project

This project consists of a Python program that allows you to track and calculate the average scores of a student in different subjects and classes. The program prompts the user to enter the student's name, subject, and class, and then input the scores for each term. It calculates the average score for each class and the overall cumulative average score, and assigns a grade based on the average score.

## Problem Statement

Given the student's name, subject, and scores for each term in different classes, the task is to calculate the average scores for each class and the overall cumulative average score, and assign a grade based on the average score.

## Algorithm

The algorithm used in this code is as follows:

1. Prompt the user to enter the student's name and subject.
2. Initialize an empty list `scores` to store the scores for each term.
3. Prompt the user to enter the class.
4. Enter the total marks for each term (term1, term2, term3) for the class.
5. Append the scores for each term to the `scores` list.
6. Remove any zero scores from the `scores` list.
7. Calculate the average score for the class by summing all the scores and dividing by the number of scores.
8. Append the average score to the `average_scores` list.
9. Print the class, scores for each term, and the average score for the class.
10. Repeat steps 3-9 until the user enters 'done' for the class.
11. Calculate the overall cumulative average score by summing all the average scores and dividing by the number of average scores.
12. Print the cumulative average score.
13. Assign a grade based on the cumulative average score.
14. Print the assigned grade.

## Python Skills Learned

By studying and working with this code, you can improve your understanding of the following Python skills:

- User input and prompt
- Conditional statements
- Looping and iteration
- Lists and list manipulation
- Mathematical calculations

## Installation

No installation is required for this project. Simply copy the code and run it in a Python environment.

## Usage

To use the Student Score Tracker program, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the program:
```bash
python student_score_tracker.py
```
4. Enter the name of the student when prompted.
5. Enter the subject of the scores.
6. Enter the class for which you want to enter scores. Repeat this step for each class.
7. Enter the total marks for each term (term1, term2, term3) for the class.
8. The program will calculate the average score for each class and print the class, scores, and average score.
9. Repeat steps 6-8 for each class. To finish entering scores, enter 'done' for the class.
10. The program will calculate the overall cumulative average score and print it.
11. The program will assign a grade based on the cumulative average score and print the grade.
