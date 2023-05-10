import numpy

"""
Exercise: Grade Vector of the 1st Bimester.
-> Read grades [0, 10] of 50 Students: Final Value
-> Purpose: Display the class average 1st Bimester:
"""

# Creating empty array list
bimester1 = numpy.zeros(5)
print(bimester1)

i = 0
while (i < 5): 
    #Error handling 
    try:
        print(f"Insert the grade of student number: {i + 1} ") 
        bimester1[i] = float(input())
        if (bimester1[i] < 0 or bimester1[i] > 10):
            print("Invalid grade, put a number between or equal to 0 - 10 ")
        else:
            i += 1
    except:
        print("Input error: choose a float number Ex: 9.2") 

bimesterSum = bimester1.sum()
listSize = bimester1.shape[0]
print(f"The sum of grades is {bimesterSum}")          
print(f"Class size: {listSize}\nThe average between grades is: {numpy.mean(bimester1): .1f}")

 
