# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма,
# виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

# Answer
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operator = input("Enter operation on numbers: ")

match operator:
    case "+":
        print(num_1 + num_2)
    case "-":
        print(num_1 - num_2)
    case "*":
        print(num_1 * num_2)
    case "/" if num_2 != 0:
        print(num_1 / num_2)
    case "/" if num_2 == 0:
        print("Error! You can't divide by zero!")
    case _:
        print("Invalid input value! Enter correct data!")
