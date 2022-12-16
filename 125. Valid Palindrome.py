class Solution:
    def isPalindrome(self, s: str) -> bool:
        variable=""
        for character in s:
            if character.isalpha() or character.isdigit():
                if character.isalpha() and ord(character)<91:
                    variable+=chr(ord(character)+32)
                else:
                    variable+=character
        return variable==variable[::-1]
        
