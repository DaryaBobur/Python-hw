# 1. Необхідно створити список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# 2. Створить інший список з 3 елементів зі списку з п.1 - першим, третім і другим з кінця.
# Приклад того, як має виглядати фінальний список:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

# Answer
import random

numbers = int(random.randint(3, 10))
num_lst = []
for _ in range(numbers):
    num_lst.append(random.randint(3, 10))

print(num_lst)

new_list = [num_lst[0], num_lst[2], num_lst[-2]]
print(new_list)