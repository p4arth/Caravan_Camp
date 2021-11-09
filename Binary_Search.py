'''
Given a sortel list find a number in the list using binary search
'''

import random

def binary_search(array, target):
    '''
    Binary search algorithm
    '''
    start = 0
    end = len(array) - 1

    while (start <= end):

        mid = (start + end) //2

        if array[mid] == target:
            return mid

        if target < array[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return -1
    

# Generate a list of 10 elements with random numbers in range 100
l = random.sample(range(100), 10)

# Inbuilt sort function
l.sort()

# number to be searched
target = int(input("Enter a number to search: "))

index = binary_search(l, target)

if index != -1:
    print("Found at index: ", index)
else:
    print("Number not found")
