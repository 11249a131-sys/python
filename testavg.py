//Aim:
    To write a Python program that accepts three test marks from the user and calculates the average of the best two test marks.

//Agorithm:

Start the program.
Input three test marks from the user — say test1, test2, and test3.
Find the smallest mark among the three.
Add the other two (best) marks and divide by 2 to get the average.
Display the best two test average.
End the program.

  //Program:
  
test1 = float(input("Enter marks of Test 1: "))
test2 = float(input("Enter marks of Test 2: "))
test3 = float(input("Enter marks of Test 3:"))
total = test1 + test2 + test3
lowest = min(test1, test2, test3)
best_two_total = total - lowest
best_two_average = best_two_total / 2
print("The average of the best two test marks is:", best_two_average)

//Result:

