import math
print ("To determine the amount of paint you need, answer the following questions (assume that one can of paint covers 100 square feet)")
print ("Enter length of long walls:")
longLength = int(input ())
print ("Enter length of short walls:")
shortLength = int(input ())
print ("Enter height of walls:")
wallHeight = int(input ())
print ("Enter length of window 1:")
win1Length = int(input ())
print ("Enter height of window 1:")
win1Height = int(input ())
print ("Enter length of window 2:")
win2Length = int(input ())
print ("Enter height of window 2:")
win2Height = int(input ())
longWalls = 2 * (longLength * wallHeight)
shortWalls = 2 * (shortLength * wallHeight)
window_1 = win1Length * win1Height
window_2 = win2Length * win2Height
roomArea = (longWalls + shortWalls) - (window_1 + window_2)
totalPaint = roomArea / 100
print ("You need " +str(math.ceil(totalPaint)) + " cans of paint.")
