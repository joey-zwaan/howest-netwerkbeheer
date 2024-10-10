camelcase = input("Voer de naam van je variable in")
snake_case = ""


for i in camelcase:
    if i.isupper() and i != camelcase[0]:
        snake_case += "_"
        snake_case += i
    else:
        snake_case += i

print(camelcase)
print(snake_case.lower())