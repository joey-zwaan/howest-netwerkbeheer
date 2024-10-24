import tabulate

table = [
    ["SSH" , 22],
    ["HTTP", 80],
    ["FTP", 20]

]

header = ["Naam", "Poort"]

print(tabulate.tabulate(table, header))