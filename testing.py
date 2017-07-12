# Тест прошел  12.07.2017 22:33

# Ответ на 10 вопрос

mass = range(1, 100)
new_list = [x**2 for x in mass if (x**2 % 3 == 0 and x**2 % 4 == 0)]
print(new_list)