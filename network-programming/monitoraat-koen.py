dieren = []
while True:
    naam = input("Geef uw favoriete dier [ stop of leeg om te stoppen]:")
    if naam ==  "stop" or naam =="":
        break
    kleur = input("Geef de kleur van het dier: ")
    dier = {"naam": naam, "kleur" : kleur}
    dieren.append(dier)

print("uw favoriete dieren zijn:")
for dier in dieren:
    print(dier, end=", ")
    print()
for dier in dieren:
    print(dier["naam"], dier["kleur"])
    print(f'de {dier["naam"]} is {dier["kleur"]}')

