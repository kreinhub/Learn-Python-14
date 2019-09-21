# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print("Task #1:")
# решение:
key = "".join(list(students[0].keys()))
repeats = set([f"{name[key]}: {students.count(name)}" for name in students])
[print(i) for i in repeats]

print("+++++++")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

# Пример вывода:
# Самое частое имя среди учеников: Маша

print("Task #2:")
# решение:
key = "".join(list(students[0].keys()))
nums = [students.count(name) for name in students]
max_num = nums.index(max(nums))
names = [name[key] for name in students]
print(f"Самое частое имя среди учеников: {names[max_num]}")
print("+++++++")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print("Task #3:")
# решение
keys = [list(i.keys()) for i in school_students[0]]
key = "".join(keys[0])

result = {}
for clas in school_students:
  for student_number, student in enumerate(clas):
    if student[key] == clas[student_number-1][key]:
      if result.get(student[key]) is None:
        result[student[key]] = clas.count(student)

[print(f"Самое частое имя в классе {num+1}: {name}") for num, name in enumerate(result)]
print("+++++++")
              
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print("Task #4:")
# решение:
school_values = [list(val.values()) for val in school]

for lists in school_values:
  for data in lists:
    male_count = 0
    female_count = 0
    if type(data) == str:
      class_name = data
    else:
      students_count = len(data)
      key_name = list(data[0].keys())[0]
      student_names = [data[i][key_name] for i in range(students_count)]
      for student_name in student_names:
        if is_male[student_name]:
          male_count += 1
        else:
          female_count += 1
      print(f"В классе {class_name} {female_count} девочки и {male_count} мальчика")
print("+++++++")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print("Task #5:")
# решение:
from operator import itemgetter

school_values = [list(val.values()) for val in school]
genders_count_by_class = []

for idx, classes in enumerate(school_values):
  for data in classes:
    if type(data) == str:
      class_name = data
      genders_count_by_class.append({"class": class_name,"males": 0, "females": 0})
    else:
      students_count = len(data)
      key_name = list(data[0].keys())[0]
      student_names = [data[i][key_name] for i in range(students_count)]
      for student_name in student_names:
        if is_male[student_name]:
          genders_count_by_class[idx]['males'] += 1
        else:
          genders_count_by_class[idx]['females'] += 1

classes_sorted_by_male = sorted(genders_count_by_class, key=itemgetter('males'), reverse=True)
classes_sorted_by_female = sorted(genders_count_by_class, key=itemgetter('females'), reverse=True)
print(f"Больше всего мальчиков в классе {classes_sorted_by_male[0]['class']}")
print(f"Больше всего девочек в классе {classes_sorted_by_female[0]['class']}")