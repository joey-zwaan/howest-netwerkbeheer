from os import linesep

name = input("Enter your name: ")


with open("names.txt", "a") as file: # file = variabele je kan zelf kiezen welke.
    file.write(f"{name}\n")



with open("names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip()) # rstrip verwijderd any whitespaces , tabs , newline characters van de rechterkant van de string

#for line in lines:
 #   print("hello,", line.rstrip())
