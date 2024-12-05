import os


print(os.system("ip a"))


# print ip address

test= os.system("ping -c 4 8.8.8.8")

if test == 0:
    print ("gelukt")
else:
    print("niet gelukt")


