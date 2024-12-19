import itertools;


x = int(input("X: "))
y = int(input("y: "))
z = int(input("Z: "))
n = int(input("N: "))

permutations = list(itertools.permutations([x, y, z]))

# sum_permutations = list(map(sum, list(permutations)))

print(permutations)
    