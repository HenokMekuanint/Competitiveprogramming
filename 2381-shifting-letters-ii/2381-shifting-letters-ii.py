class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp=[0 for i in range(len(s) + 1)]
        
        for start, end, state in shifts:
            temp[start] += [1, -1][1 - state]
            temp[end + 1] -= [1, -1][1 - state]
                
        total = 0
        for i in range(len(temp)):
            total += temp[i]
            temp[i] = total
        
        ans=""
        for i in range(len(s)):
            temp[i]= ((ord(s[i]) - ord('a')) + temp[i]) % 26 + ord('a')
            ans += chr(temp[i])
        
        return ans
        