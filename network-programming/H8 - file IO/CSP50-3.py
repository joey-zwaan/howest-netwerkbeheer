names = []

with open("names.txt") as file: # geen R nodig default = read
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True): # Als je wil reversen is dit mogelijk
    print(f"hello, {name}")