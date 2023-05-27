def bmi():

    """

        Function that calculates for the BMI of an individual

        Parameters:
            None

        Returns:
            None: Only prints output to the screen

    """


    # handle exceptions
    try:

        # Prompt the user to enter their weight in kilograms
        weight = float(input('Enter your weight(kg): '))

        # Prompt the user to enter their height in meters
        height = float(input('Enter your height(m): '))

        # Compute for the BMI using: bmi = weight / (height ** 2)
        bmi = weight / (height ** 2)

        # Round the value of the BMI to 2 decimal places
        bmi = round(bmi, 2)


        # Categorize the BMI value into different weight categories based on standard thresholds
        if bmi < 18.5:
            category = 'underweight'
            issue = 'Beight underweight can result in health issues like Anaemia and Osteoporosis'
        elif 18.5 <= bmi <= 24.9:
            category = 'healthy weight'
            issue = 'Keep it up'
        elif 25 <= bmi <= 29.9:
            category = 'overweight'
            issue = 'If not controlled, can lead to high blood pressure and diabetes'
        else:
            category = 'obese'
            issue = 'If not checked, can lead to cardiovascular disease and heart problems'
    except:
        print('Please enter valid inputs.')
        

    # Display the entered weight and height of the individual
    print('Weight:', weight)
    print('Height:', height)

    # Display results of BMI, weight category and it's associated health risks
    print(f'Your BMI is ' + str(bmi) + ' so you are in the ' + category + ' range')
    print(issue)



# Call the function to calculate and display the BMI
bmi()