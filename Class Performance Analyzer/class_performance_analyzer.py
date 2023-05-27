# Class Performance Analyzer

# Function to calculate class scores and performance
def computegrade():
    grades = []  # List to store grades
    while True:
        grade = input('Enter grade: ')
        if grade == 'done':
            break
        else:
            grades.append(int(grade))  # Append input grade to the list
    avg_score = sum(grades) / len(grades)  # Calculate average score
    total = sum(grades)  # Calculate total score

    # Calculate median score
    if len(grades) % 2 == 0:
        median_score = (grades[len(grades) // 2 - 1] + grades[len(grades) // 2]) / 2
    else:
        median_score = grades[len(grades) // 2 + 1]
    
    # Print calculated scores and performance
    print('The median grade of the class is', median_score)
    print('Class average score:', avg_score)
    print('Class total score:', total)

    # Evaluate class performance based on average score
    if avg_score > 80:
        print('Class did excellent!')
    elif 80 > avg_score > 70:
        print('Class did very good')
    elif 70 > avg_score > 60:
        print('Class did good')
    else:
        print('Class did bad')

# Call the computegrade function
computegrade()
