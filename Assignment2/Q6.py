'''Create two sets, one with numbers [1, 2, 3, 4] and the other [3, 4, 5, 6]. 
Perform both union() and update() operations and explain the difference in comments.'''

# create set 1
set1 = {1, 2, 3, 4}
print("Set 1:", set1)

# create set 2
set2 = {3, 4, 5, 6}
print("Set 2:", set2)

# perform union() operation
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# perform update() operation
set1.update(set2)
print("Set 1 after update():", set1)

# Explanation:
# The union() operation creates a new set that contains all unique elements from both sets.
# The update() operation modifies the original set (set1) by adding all unique elements from set2 to it.