//Aim:
      To develop a Python program that checks whether a given number is a palindrome and counts the occurrences of each digit.

//Algorithm:
step 1: Start the program.
step 2: Input a number as a string.
step 3: Reverse the number using slicing ([::-1]).
step 4: Compare the reversed string with the original:
step 5: If equal → Palindrome
step 6: Else → Not a palindrome
step 7: For each unique digit, count how many times it appears using .count().
stsep 8: Display the results.
step 9: End the program.

//Program:
num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is NOT a Palindrome number.")
print("\nDigit Occurrences:")
for digit in sorted(set(num)):
    print(f"Digit {digit} occurs {num.count(digit)} time(s).")

//Result:
