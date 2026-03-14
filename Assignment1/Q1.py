# Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0 & num != 0:
    print(f"{num} is an even number.")
elif num % 2 != 0 & num != 0:
    print(f"{num} is an odd number.")
else:
    print("Number is zero, which is considered even.")