class Solution:
    def maxVowels(self, s: str, k: int) -> int:
#         maximum=0
#         counter=0
#         left=0
        
#         "abciiidef" k=3 counter=1
#            L
#              R

        vowels=['a','e','i','o','u']
        maximum=0
        counter=0
        left=0
        for right in range(len(s)):
            
            while (right-left+1)>k:
                if s[left] in vowels:
                    counter-=1
                left+=1
            if s[right] in vowels:
                counter+=1
                maximum=max(maximum,counter)
        return maximum
