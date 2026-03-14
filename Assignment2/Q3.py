'''Create a set of 5 numbers with some duplicates. Add a new number to the set, remove 
an existing number using discard(), and check if a specific number exists in the set. 
Print the set at each step.'''

# create a set of numbers with duplicates
print("***Set of numbers with duplicates***")
numbers_set = {1, 2, 3, 4, 5, 2, 3}
print(numbers_set)

# add a new number to the set
print("\n***Add a new number***")
numbers_set.add(6)
print(numbers_set)

# remove an existing number using discard()
print("\n***Remove an existing number using discard()***")
numbers_set.discard(3)
print(numbers_set)

# check if a specific number exists in the set
print("\n***Check if a specific number exists in the set***")
if 4 in numbers_set:
    print("4 exists in the set")
else:
    print("4 does not exist in the set")