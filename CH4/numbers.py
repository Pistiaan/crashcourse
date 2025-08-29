#4-3
for n in range(1,21):
    print(n)

#4-4
# for n in range(1,1000001):
#     print(n)

#4-5
million_numbers = range(1,1000001)
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

#4-6
for n in range(1, 21, 2):
    print(n)

#4-7
for n in range(3, 31, 3):
    print(n)

#4-8&9
cubes = [n**3 for n in range(1,11)]
for cube in cubes:
    print(f"the cube of {cubes.index(cube) + 1} is {cube}")

#4-10
print(f"The first three numbers in the list are: {list(million_numbers[:3])}")
print(
    f"Three numbers in the middle of the list are: "
    f"{list(million_numbers[1000:1003])}"
)
#Trying out the line lenght limit from the style guide :)
print(f"The last thee numbers in the list are: {list(million_numbers[-3:])}")