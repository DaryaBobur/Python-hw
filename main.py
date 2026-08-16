# print("Hello World")

def closure_example(x):
    """
    Реалізує функцію, яка використовує замикання для збереження значення.

    :param x: Початкове значення.
    :return: Функція, яка використовує замикання для збереження значення x.
    """
    c = x
    def inner_function(y):
        print(x+y)
        return x + y
    return inner_function


closure_instance = closure_example(-8)
closure_instance(10)
# Перевірка
# assert closure_instance(3) == 8


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(7)
print(result)