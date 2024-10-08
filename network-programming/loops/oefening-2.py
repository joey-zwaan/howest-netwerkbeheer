from operator import truediv

light= "rood"
drive = False


while drive == False:
    light= input("Verkeerslicht: ")
    if light == "rood" or light == "oranje":
        print("Wacht!")
    elif light =="groen":
        drive = True
        print("gas!")
    else:
        drive = True
        print("gas!")