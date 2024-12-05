name = input("What is jouw naam?")
# Naam gevraagd aan gebruiker


file_w = open("names.txt", "w") # Bestand gemaakt names.txt en deze openen met "write"
file_w.write(name) # We schrijven de variable name in het bestand names.txt

file_w.close() # we sluiten het bestand


file_r =open("names.txt", "r") # We openen het bestand om te lezen
lines = file_r.readlines() # Word gebruikt om alle lijnen te lezen en te returnen als een string



for line in lines:
    print(f"hallo {line}") # loopt door elke regel in de lijst lines & voegt hallo voor elke regel toe

file_r.close()
