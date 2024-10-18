"""
Area Sum

Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

The function will calculate the area of each rectangle, then sum them all up and return the result.
"""

def area_sum(rectangles):
    sum = 0
    
    for measurements in rectangles:
        height = measurements['height']
        width = measurements['width']
    #calc area of each rec
        area = width * height
        sum += area

    return sum


"""
---------------------------------
Inputs: [{'height': 4, 'width': 5}]
Expecting: 20
Actual: 20
Pass
---------------------------------
Inputs: [{'height': 4, 'width': 5}, {'height': 4, 'width': 9}]
Expecting: 56
Actual: 56
Pass
---------------------------------
Inputs: [{'height': 4, 'width': 5}, {'height': 18, 'width': 5}]
Expecting: 110
Actual: 110
Pass
---------------------------------
Inputs: [{'height': 2, 'width': 3}, {'height': 4, 'width': 5}]
Expecting: 26
Actual: 26
Pass
---------------------------------
Inputs: [{'height': 6, 'width': 7}, {'height': 8, 'width': 9}]
Expecting: 114
Actual: 114
Pass
---------------------------------
Inputs: [{'height': 10, 'width': 11}, {'height': 12, 'width': 13}]
Expecting: 266
Actual: 266
Pass
---------------------------------
Inputs: [{'height': 0, 'width': 0}]
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: []
Expecting: 0
Actual: 0
Pass
============= PASS ==============
8 passed, 0 failed
"""