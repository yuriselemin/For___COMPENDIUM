
# Вложенный цикл for в программировании представляет собой структуру управления,
# которая позволяет выполнять набор команд несколько раз в рамках одного основного цикла.
# Это достигается путем размещения одного цикла for внутри другого.
#
# Давайте рассмотрим алгоритм действия вложенного цикла for на примере.
# Допустим, у нас есть два списка: list1 и list2. Мы хотим пройтись по каждому элементу
# первого списка и для каждого элемента выполнить некоторые операции с каждым элементом второго списка.
#
# Вот как это будет выглядеть на Python:
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# for i in list1: # Основной цикл
#     for j in list2: # Вложенный цикл
#         print(i, j) # Операция с элементами


# Теперь давайте разберем этот код шаг за шагом:
#
# list1 = [1, 2, 3] - объявляем первый список с тремя элементами.
# list2 = [4, 5, 6] - объявляем второй список с тремя элементами.
# for i in list1: - начинаем основной цикл, который будет проходить по каждому элементу списка list1.
# Переменная i будет принимать значение каждого элемента в list1.
# for j in list2: - внутри основного цикла начинаем вложенный цикл,
# который будет проходить по каждому элементу списка list2.
# Переменная j будет принимать значение каждого элемента в list2.
# print(i, j) - внутри вложенного цикла выполняем операцию,
# которая будет выполняться для каждой пары элементов i и j. В данном случае мы просто выводим эти элементы.
# Таким образом, при выполнении этого кода произойдет следующее:
#
# Сначала переменная i примет значение первого элемента списка list1, то есть 1.
# Затем начинается вложенный цикл, где переменная j принимает значение
# первого элемента списка list2, то есть 4. Выводится 1 4.
# После этого переменная j принимает значение второго элемента списка list2, то есть 5.
# Выводится 1 5.
# Этот процесс продолжается до тех пор, пока все элементы списка list2 не будут обработаны.
# После этого переменная i принимает значение следующего элемента списка list1, то есть 2.
# Процесс повторяется для всех элементов списка list2.
# Этот процесс продолжается до тех пор, пока все элементы списка list1 не будут обработаны.
# В результате выполнения этого кода будет выведено:


# Пример 1: Сумма элементов двух списков
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# total = 0
# for x in list1:
#     for y in list2:
#         total += x * y

# print(total)



# Пример 2: Сумма значений словарей с одинаковыми ключами

dict1 = {"apple": 1, "banana": 2, "cherry": 3}
dict2 = {"apple": 4, "banana": 5, "melon": 6}

total = 0
for key in dict1:
    if key in dict2:
        total += dict1[key] * dict2[key]

print(total)

#
#
# # Пример 3: Перемножение матриц
#
# matrix1 = [[1, 2], [3, 4]]
# matrix2 = [[5, 6], [7, 8]]
#
# product = [[0, 0], [0, 0]]
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         for k in range(len(matrix2[0])):
#             product[i][k] += matrix1[i][j] * matrix2[j][k]
#
# print(product)  # Вывод: [[19, 22], [43, 50]]
#
#
#
#
# # Пример 4: Объединение словарей с одинаковыми ключами
#
# dict1 = {"apple": 1, "banana": 2, "cherry": 3}
# dict2 = {"apple": 4, "banana": 5, "melon": 6}
#
# merged = {}
# for dic in [dict1, dict2]:
#     for key in dic:
#         merged[key] = merged.get(key, 0) + dic[key]
#
# print(merged)  # Вывод: {'apple': 5, 'banana': 7, 'cherry': 3, 'melon': 6}


















