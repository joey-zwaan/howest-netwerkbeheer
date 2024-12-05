server = {"name": "websrv", "ip": "192.168.0.100", "port": 80}


print(server)

# dictionaries spreken we over sleutel + waarde

print ("-"*21)

for e in server:
    print(e, server[e])

    # standaard enkel de sleutel terugkrijgen niet de waarde
    # sleutel geburiken om waarde terug te krijgen


for key, value in server.items():
    print(key, value)