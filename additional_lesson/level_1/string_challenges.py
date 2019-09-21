# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

print("++++")
# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))

print("++++")
# Вывести количество гласных букв в слове
word = 'Архангельск'
print(word.lower().count("а") + word.lower().count("е"))


print("++++")
# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

print("++++")
# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
[print(i[0]) for i in sentence.split()]

print("++++")
# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

# avg = total_sum / total_num 
sum_length = sum([len(i) for i in sentence.split()])
print(sum_length / len(sentence.split()))