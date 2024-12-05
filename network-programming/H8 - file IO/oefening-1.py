name = input("Enter your name: ")

with open("names.txt", "a") as file: # a = append en w = write dus bij append word het extra toegevoegd en bij write overgeschreven.
    file.write(f"{name}\n") # We gebruiken new_line omdat python ze anders achter elkaar gaat plakken.

# Dit betekent dat het bestand automatisch gesloten word als we terug uit de indentatie schrijven


with open("names.txt", "r") as file:
    lines = file.readlines()

# Hier is het bestand gesloten geweest en gaan we loopen door de variable.

for line in lines:
    print(line)
