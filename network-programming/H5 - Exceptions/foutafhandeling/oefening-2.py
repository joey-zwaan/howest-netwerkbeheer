# dit stukje kan fout gaan.
# in plaats van error dan foutje drukken

while True:
    try:
        age = int(input("Leeftijd:"))
        print(age)
        if age == 0:
            break

    except:
        print("foutje")



    port = [1,2,3, "127.0.0.1", 4, 5]
    for ports in port:
        try:
            print(ports/3)
        except:
            print("FOUTJE")


    try:
        age = int(input("Leeftijd:"))
        print(age)
        if age == 0:
            break
    except ValueError as v:
        print(v)
    except Exception as e:
        print("Foutje")
        print(e)
    finally:
        print("gedaan")
# om af te sluiten

