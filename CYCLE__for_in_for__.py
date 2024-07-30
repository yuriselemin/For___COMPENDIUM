

# Пример 1: Вложенные циклы для создания таблицы умножения
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end=" ")
    print()




# Пример 2: Вложенные циклы для рисования снежинки
for i in range(1, 6):
    for j in range(1, 6):
        if (i == 1 and j != 3) or (i == 5 and j != 2) or (j == 5 and i != 3) or (i == j):
            print("* ", end="")
        else:
            print("  ", end="")
    print()




# Пример 3: Вложенные циклы для подсчета количества вхождений каждого символа в строку
string = input("Введите строку: ")
characters = sorted(set(string))
for char in characters:
    count = 0
    for c in string:
        if c == char:
            count += 1
    print(f"Количество вхождений '{char}' в строке: {count}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list1: # Основной цикл
    for j in list2: # Вложенный цикл
        print(i, j) # Операция с элементами




# Пример 1: Сумма элементов двух списков

list1 = [1, 2, 3]
list2 = [4, 5, 6]

total = 0
for x in list1:
    for y in list2:
        total += x * y

print(total)




# Пример 2: Сумма значений словарей с одинаковыми ключами

dict1 = {"apple": 1, "banana": 2, "cherry": 3}
dict2 = {"apple": 4, "banana": 5, "melon": 6}

total = 0
for key in dict1:
    if key in dict2:
        total += dict1[key] * dict2[key]

print(total)




# Пример 3: Перемножение матриц

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

product = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        for k in range(len(matrix2[0])):
            product[i][k] += matrix1[i][j] * matrix2[j][k]

print(product)  # Вывод: [[19, 22], [43, 50]]




# Пример 4: Объединение словарей с одинаковыми ключами

dict1 = {"apple": 1, "banana": 2, "cherry": 3}
dict2 = {"apple": 4, "banana": 5, "melon": 6}

merged = {}
for dic in [dict1, dict2]:
    for key in dic:
        merged[key] = merged.get(key, 0) + dic[key]

print(merged)  # Вывод: {'apple': 5, 'banana': 7, 'cherry': 3, 'melon': 6}


















