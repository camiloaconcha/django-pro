def check_palindome(word):
    leng = len(word)
    notWord = leng <= 1
    sameInitial = word[0] == word[leng-1]
    if notWord:
        return '> Is Palindrome'
    if (not sameInitial):
        return '> Not Palindrome'

    return check_palindome(word[1:-1])


print(check_palindome('repaper'))
print(check_palindome('rotor'))
print(check_palindome('civic'))
print(check_palindome('kayak'))
print(check_palindome('camilc'))
print(check_palindome('sagas'))
print(check_palindome('atrasa'))
