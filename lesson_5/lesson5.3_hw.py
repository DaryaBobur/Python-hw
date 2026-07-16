# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

# Answer

import string

user_text = input("Enter your string: ")
new_text = ""

for i in user_text:
    if i not in string.punctuation:
        new_text += i

first_letters = new_text.title()
edited_text = first_letters.replace(" ", "")
hashtag = f"#{edited_text}"
print(hashtag)

if len(hashtag) > 140:
    print(hashtag[:140])






