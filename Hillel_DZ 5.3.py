import string

hashtag = input("Enter your string: ")

hashtag = hashtag.split()
word = []

for el in hashtag:
    for symb in string.punctuation:
        el = el.replace(symb, "")
    word.append(el.capitalize())

hashtag = "#" + "".join(word)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
