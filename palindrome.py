num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is NOT a Palindrome number.")
print("\nDigit Occurrences:")
for digit in sorted(set(num)):
    print(f"Digit {digit} occurs {num.count(digit)} time(s).")
