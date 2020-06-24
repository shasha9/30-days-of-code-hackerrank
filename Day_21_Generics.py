#Task
#Write a single generic function named printArray;this function must take an array of generic elements as a parameter.

from typing import TypeVar

Element = TypeVar("Element")

def printArray(array: [Element]):
    for element in array:
        print(element)

vInt = [1, 2, 3]
vString = ["Hello", "World"]
printArray(vInt)
printArray(vString)
