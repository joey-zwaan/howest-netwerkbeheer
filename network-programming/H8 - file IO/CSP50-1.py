names = [] # We maken een lege list

for _ in range(3):  # We vragen om dit 3x te doen want we willen 3 namen bekomen
    name = input("Enter your name: ")
    names.append(name)

for name in sorted(names): # gesorteerd op alfabet
    print(f"{name}") # voor elke loop printen we de variable name

