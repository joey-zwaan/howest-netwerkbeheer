servers = [{"name": "websrv", "ip": "192.168.0.100", "port": 80},
           {"name": "api-srv", "ip": "192.168.0.101", "port": 5000},
           {"name": "db-srv", "ip": "192.168.0.102", "port": 3999}
]

for server in servers:
    print(f"Name: {server['name']} - IP: {server['ip']} - Port: {server['port']}")


print("-"*21)


for server in servers:
    for k, v in server.items():
        print(k, v)