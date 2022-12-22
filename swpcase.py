def swap_case(s):
    _res=""
    for char in s:
        if ord(char)<=90 and ord(char)>=65:
            _res+=chr(ord(char)+32)
        elif ord(char)<=122 and ord(char)>=97:
            _res+=chr(ord(char)-32)
        else:
            _res+=char
            
    return _res

if __name__ == '__main__':
