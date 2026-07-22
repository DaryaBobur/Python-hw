# Напишіть функцію common_elements, яка згенерує два списки елементів
# з генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.

# Answer

def common_elements():
    first_list = list(range(0, 100, 3))
    second_list = list(range(0, 100, 5))

    first_set = set(first_list)
    second_set = set(second_list)

    intersection_set = first_set.intersection(second_set)
    print(intersection_set)

    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
