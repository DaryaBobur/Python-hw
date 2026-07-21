# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.
# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

# Answer

user_number = int(input("Enter your number: "))
print(user_number)

if int(user_number) <= 9 and user_number >= 0:
    print(user_number)
else:
    while user_number > 9:
        total = 1
        while user_number > 0:
            number = user_number % 10
            user_number //= 10
            total *= number
        user_number = total
        print(user_number)









