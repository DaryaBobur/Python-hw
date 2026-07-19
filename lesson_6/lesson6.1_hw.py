# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

#Answer
import string
user_letters = input("Enter two letters separated by a hyphen: ")
all_letters = string.ascii_letters


for _ in user_letters:
    if len(user_letters) == 3 and user_letters[0].isalpha() and "-" in user_letters[1] and user_letters[2].isalpha():
        first_num = all_letters.index(user_letters[0])
        second_num = all_letters.index(user_letters[2])
        result = all_letters[first_num:second_num + 1]
        print(result)
    else:
        print("Error")






