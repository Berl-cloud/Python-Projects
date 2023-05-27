''''
    This is a python function that can be used to find the maximum number in a given list of numbers. 
    We used pep 8 style of writing python codes.


    This code will help improve your knowledge of function declarations, loops and list indexes.
'''

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

max_num = find_max([4,8,20,10,6])
print('The largest number is', max_num)


