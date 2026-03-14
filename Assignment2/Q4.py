'''Create a list of 6 random numbers. Sort the list in ascending and descending order.
Then, combine it with another list [10, 20, 30] using both + and extend().
Print all outputs.'''

# create a list of 6 random numbers
print("***List of random numbers***")
numbers = [5, 2, 9, 1, 5, 6]
print(numbers)

# sort the list in ascending order
print("\n***Sorted in Ascending Order***")
numbers.sort()
print(numbers)

# sort the list in descending order
print("\n***Sorted in Descending Order***")
numbers.sort(reverse=True)
print(numbers)

# combine the list with another list using +
print("\n***Combined using +***")
combined_list = numbers + [10, 20, 30]
print(combined_list)

# combine the list with another list using extend()
print("\n***Combined using extend()***")
numbers.extend([10, 20, 30])
print(numbers)