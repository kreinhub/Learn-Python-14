names = ["John", "James", "Anna", "Markus", "Bob"]
excited_name = 'John'
for name in names[::-1]:
    if name == excited_name:
        print(f"{excited_name} is found")
        