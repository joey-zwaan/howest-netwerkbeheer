import time
#Maak een script dat de aftelling van de Space ShuttleLinks to an external site. nabootst:

#Te beginnen vanaf 10
#In plaats van 6 druk je "Main engine start" af
#Na 0 volgt "lift-off"
countdown = int(input("From what number would you like to countdown from?"))

while countdown != 0:
    if countdown > 60:
        countdown -= 10
        time.sleep(10)
        print(countdown)

    elif countdown == 60 or  countdown <60 :
        countdown -= 1
        time.sleep(1)
        print(countdown)

else :
    print("lift off!")


