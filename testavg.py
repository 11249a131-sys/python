
test1 = float(input("Enter marks of Test 1: "))
test2 = float(input("Enter marks of Test 2: "))
test3 = float(input("Enter marks of Test 3:"))
total = test1 + test2 + test3
lowest = min(test1, test2, test3)
best_two_total = total - lowest
best_two_average = best_two_total / 2
print("The average of the best two test marks is:", best_two_average)
