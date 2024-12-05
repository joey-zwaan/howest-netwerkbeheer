names = ["Jos", "José", "Joske"]

print(names)
index = 0
while index < len(names):
    print(names[index])
    index += 1


print("-" * 10 )


## korter schrijven

for name in names:
    print(name)

print("_"*21)


index = 0
while index < len(names):
    print(index, names[index])
    index += 1



print("_"*21)


for index, name in enumerate(names):
    print(index, name)


ages = [18, 19, 20]

for i, age in enumerate(ages):
    print(i, names[i] ,age)
