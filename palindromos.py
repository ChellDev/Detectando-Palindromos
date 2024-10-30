
"ARARA"

def is_palindromo(word):
    j = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result + 1
            