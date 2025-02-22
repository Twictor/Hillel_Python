import string


def is_palindrome(text):
    text_rev = ""
    for el in text:
        if el not in string.punctuation and el != " ":
            text_rev += el.lower()
    return text_rev == text_rev[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
