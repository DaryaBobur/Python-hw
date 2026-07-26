# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво
# без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False

# Answer
import string
def is_palindrome(text):
    correct_text = text.lower().replace(string.punctuation, "").replace(" ", "")
    new_text = ""

    for i in correct_text:
        if i not in string.punctuation:
            new_text += i
    result = new_text[::-1]

    if new_text == result:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
