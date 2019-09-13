age = int(input('Enter your age: '))

def activity(age):
    if age < 8:
        return "You're kindergartner"
    elif age <= 18:
        return "You're schoolchild"
    elif age <= 21:
        return "You're student"
    else:
        return "You're employee"

result = activity(age)
print(result)