# BMI Calculator

## About Project

The `BMI (Body Mass Index)` Calculator is a simple Python project that calculates the BMI of an individual based on their height and weight. 
BMI is a commonly used metric to assess whether a person has a healthy weight for their height.

## Problem Statement

The problem statement for this project is to develop a BMI calculator that takes the height and weight 
of an individual as inputs and calculates their BMI. 
The goal is to provide users with a quick and easy way to determine their BMI category, 
such as underweight, normal weight, overweight, or obese. 
This information can help individuals monitor their weight and make informed decisions about their health.

## Algorithm

The algorithm implemented in this project follows a straightforward formula to calculate BMI. It can be summarized as follows:

1. Accept the input of height in meters and weight in kilograms from the user.
2. Calculate BMI using the formula: `BMI = weight / (height ** 2)`
3. Categorize the BMI value into different weight categories based on standard thresholds.
   - BMI < 18.5: Underweight
   - 18.5 <= BMI < 25: Normal weight
   - 25 <= BMI <= 29.9: Overweight
   - BMI >= 30: Obese
4. Display the calculated BMI value and the corresponding weight category to the user.

The algorithm is designed to be simple and efficient, providing users with an instant understanding of their BMI category.

## Python Skills Learnt

Throughout the development of this project, several Python skills were acquired and honed. Some of the key skills learned during this project include:

- Accepting user input using the `input()` function
- Performing mathematical calculations
- Implementing conditional statements to categorize BMI
- Displaying output to the user

These skills were crucial in successfully implementing the BMI calculator and providing accurate results to users.

## Getting Started

To get started with the BMI Calculator project, follow these steps:

1. Get Python 3 installed on your machine.
2. Open a terminal and run the following commands:
``` bash
git clone <repo-url>
```
This command will enable you clone the repository unto your local machine.

Now run:
``` bash
cd project-name
```
To navigate to the project directory

3. In the same terminal, run:
``` bash
pip install -r requirements,txt
```
To install any dependencies

## Usage

To use the BMI Calculator, follow these steps:
1. Open a terminal.
2. Navigate to the project directory.
3. Run the script below to start the calculator:
``` bash
python bmi_calculator.py
```
4. Enter your weight in kilograms.
5. Enter your height in meters.
6. The calculated BMI along with it's weight category and health risks will be displayed. 

_Make sure to provide accurate measurements to get the correct BMI calculation._

## Contribution

If you would like to contribute to the BMI Calculator project, you can follow these guidelines:

- Fork the repository and make your changes.
- Create a new branch for your modifications: 

``` bash
git checkout -b feature/your-feature
```
- Commit your changes: 

``` bash
git commit -m 'Add your feature'
```
- Push the branch to your forked repository: 

``` bash
git push origin feature/your-feature
```
- Open a pull request on the original repository.

Your contributions are highly appreciated and can help enhance the project further.

## References

[WebMD](https://www.webmd.com/diet/body-bmi-calculator)

---
