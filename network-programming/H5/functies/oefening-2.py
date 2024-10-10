def test():
    print("hoi")

def test_1():
    print(f"hoi {name}")

def test_2(name): # lokale variabele
    print(f"hoi {name}")

def test_3(name, age): # lokale variabele
    print(f"hoi {name}, {age}")

def test_4(age = 1): # Als er geen parameter word gegeven gaat hij standaard 1 gebruiken.
    age += 1
    return age



test()
name = "jos"
test_1()


blablabla = "Jose"
# name = blablabla
test_2(blablabla)
test_2("Jos")
test_2("Omer")
test_2(name)
test_3(13 , "omer")
age = test_4(16)
print(age)

age = test_4()
print(age)
age = test_4(16)

print(age)