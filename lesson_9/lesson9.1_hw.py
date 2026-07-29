# На вхід функції popular_words передаються два аргументи. Текст та список слів, популярність яких необхідно визначити.
# При вирішенні цього завдання зверніть увагу на такі моменти
# Слова необхідно шукати у всіх регістрах. Тобто. якщо необхідно знайти слово "one",
# значить для нього будуть підходити слова "one", "One", "oNe", "ONE" і т.д.
# Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)
# Вхідні параметри: Текст і масив слів, що шукаються.
# Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями,
# скільки разів кожнє слово зустрічаються у орігінальному тексті.

# Answer

def popular_words(text, words):
    correct_text = text.lower().split()
    new_words = []
    number = []

    for i in words:
        count_words = correct_text.count(i)
        correct_words = i.lower()
        number.append(count_words)
        new_words.append(correct_words)

        print(dict(zip(new_words, number)))
    return dict(zip(new_words, number))



assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
