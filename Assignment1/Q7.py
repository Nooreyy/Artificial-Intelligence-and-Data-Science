#Write a program to calculate the sum of all even numbers between 1 and 50.

sum = 0
for num in range(1, 51):
    if num % 2 ==0:
        sum += num
print(f"The sum of all even numbers between 1 and 50 is: {sum}")