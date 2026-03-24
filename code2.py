# Create sets

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}


print("Set 1 elements:")

for elem in set1:

  print(elem, end=" ")

print("\nSet 2 elements:")

for elem in set2:

  print(elem, end=" ") 
print()


union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

intersection_set = set1.intersection(set2)

print("Intersection of Set1 and Set2:", intersection_set)


difference_set = set1.difference(set2)

print("Difference (Set1 - Set2):", difference_set)


difference_set2 = set2.difference(set1)

print("Difference (Set2 - Set1):", difference_set2)