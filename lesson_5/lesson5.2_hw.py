# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора
# після кожного обчислення - якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.

# Answer
while True:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    operator = input("Enter operation on numbers: ")

    if operator == "+":
        print(num_1 + num_2)
    elif operator == "-":
        print(num_1 - num_2)
    elif operator == "*":
        print(num_1 * num_2)
    elif operator == "/" and num_2 != 0:
        print(num_1 / num_2)
    elif operator == "/" and num_2 == 0:
        print("Error! You can't divide by zero!")
    else:
        print("Invalid input value! Enter correct data!")

    user_choice = input("Do you want to continue? Enter -y to continue: ")

    if user_choice == "y":
        continue
    else:
        break






