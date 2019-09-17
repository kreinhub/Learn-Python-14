import csv


user_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

with open("output.csv", "w") as file:
    fields = ["name","age","job"]
    writer = csv.DictWriter(file, fields, delimiter=";")
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)
