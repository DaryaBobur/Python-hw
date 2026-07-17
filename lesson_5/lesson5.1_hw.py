# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може містити символ _, але не може містити два символи __ підряд.
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

# Answer
import string, keyword

possible_var = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value", "Get_value",
                "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]

reserved_word = ", ".join(keyword.kwlist)
str_punctuation = string.punctuation.replace("_", "")
check_var = True

for variable in possible_var:

    if len(variable) == 0:
        print("Incorrect data!")

    elif variable == "_":
        check_var = True
        print("Variable is correct -", check_var)

    elif any(char in str_punctuation for char in variable):
        check_var = False
        print("Variable includes punctuation -", check_var)

    elif variable.lower() in reserved_word.lower() and len(variable.lower()) > 1:
        check_var = False
        print("Variable includes reserved word -", check_var)

    elif "__" in variable:
        check_var = False
        print("Incorrect variable - ", check_var)

    elif variable[0].isdigit():
        check_var = False
        print("Number can't be first in variable -", check_var)

    elif any(char for char in variable if char.isupper()):
        check_var = False
        print("Variable can`t be with upper letters -", check_var)

    elif " " in variable:
        check_var = False
        print("Variable can`t be with space -", check_var)

    else:
        check_var = True
        print("Variable is correct -", check_var)