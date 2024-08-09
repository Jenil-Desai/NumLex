def is_vowel(l: str) -> bool:
    if l.lower() in ['a','e','i','o','u']:
        return True
    else:
        return False

def is_consonant(l: str) -> bool:
    if l.lower() not in ['a','e','i','o','u']:
        return True
    else:
        return False
    
def find_char(string: str, char: str) -> list[int] :
    res = []
    cnt = 0
    for i in string:
        if i == char:
            res.append(cnt)
        cnt += 1
    return res

def is_palindrom(string: str) -> bool:
    if string == string[::-1]:
        return True
    else:
        return False

def cnt_char(string: str, char: str) -> int:
    cnt = 0
    for i in string:
        if i == char:
            cnt += 1
    return cnt