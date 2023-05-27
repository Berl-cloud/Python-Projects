# Prompt user for student name and subject
name = input('Enter name of student: ')
subject = input('Enter subject: ') 
subject = subject.capitalize()

# Print student name and subject
print('Name:', name.upper())
print('Subject:', subject)

# Initialize lists to store scores and average scores
scores = []
average_scores = []

# Function to calculate yearly cumulative average scores
def yearly_cum():
    while True:
        # Prompt user for class
        level = input('Enter class: ')
        # Break loop if user enters 'done'
        if level == 'done':
            break
        
        # Convert class name to uppercase
        level = level.upper()
        
        # Prompt user for total marks for each term
        term1 = float(input('Enter total marks: '))
        term2 = float(input('Enter total marks: '))
        term3 = float(input('Enter total marks: '))
        
        # Append scores for each term to the scores list
        scores.append(term1)
        scores.append(term2)
        scores.append(term3)
        
        # Remove any zero scores from the scores list
        for i in scores:
            if i == 0:
                scores.remove(i)
        
        # Calculate the average score for the class
        average_score = round(sum(scores) / len(scores))
        
        # Append the average score to the average_scores list
        average_scores.append(round(average_score))
        
        # Print class, scores for each term, and average score for the class
        print('Class:', level)
        print('First Term Score:', term1)
        print('Second Term Score:', term2)
        print('Third Term Score:', term3)
        print('Average score for', subject, 'at', level + ':', average_score)
    
    # Call overall_cum function to calculate overall cumulative average
    overall_cum()

# Function to calculate overall cumulative average and assign grade
def overall_cum():
    for i in average_scores:
        if i == 0:
            average_scores.remove(i)
    
    # Calculate the overall cumulative average score
    overall_grade = round(sum(average_scores) / len(average_scores))
    
    # Print the overall cumulative average score
    print('Cumulative Average Score:', overall_grade)
    
    # Assign grade based on the overall cumulative average score
    if 90 <= overall_grade <= 100:
        print('Grade: A+ - Excellent Performance')
    elif 80 <= overall_grade <= 89:
        print('Grade: A - Very Good Performance')
    elif 70 <= overall_grade <= 79:
        print('Grade: B+ - Good Performance')
    elif 60 <= overall_grade <= 69:
        print('Grade: B - Advanced Performance')
    elif 50 <= overall_grade <= 59:
        print('Grade: C - Proficiency Level Performance')
    elif 40 <= overall_grade <= 49:
        print('Grade: D - Beginners Performance')
    elif 30 <= overall_grade <= 39:
        print('Grade: E - Performance Below Expectation')
    else:
        print('NGP - No Grade Possible')

# Call yearly_cum function to start the score tracking process
yearly_cum()
