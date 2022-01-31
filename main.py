import requests
from unittest import case
from openpyxl import load_workbook

file = "num.xlsx"

numbers = load_workbook(file)

sheet = numbers.active

rows = sheet.rows

header = next(rows)

headers = ["id", "groupe", "nom", "numero"]

contacts = []
code = 237
host = "https://lifelinesms.org/server.php?page=setUser"

for row in rows:
    data = {}
    cv = 19
    CHU = 20
    HGD = 21
    verify = 0
    lock = 0
    for title, cell in zip(headers, row):
        if verify == 1 and lock == 0:
            if cell.value == "CV":
                data[title] = cv
            elif cell.value == "CHU":
                data[title] = CHU
            elif cell.value == "HGD":
                data[title] =   HGD
            verify = 0
            lock = 1
        else:
            data[title] = cell.value
            verify = 1
    
    contacts.append(data)


final = []
i = 1
for num in contacts:
    req = f'INSERT INTO `users`(`name`, `surname`, `phone`, `pays_id`, `email`, `groupe_id`) VALUES ("{num.get("nom")}", "", "{num.get("numero")}", {code}, "", {num.get("groupe")});\n'
    with open("ih.txt", "a") as fil:
        fil.write(req)
    final.append(req)


