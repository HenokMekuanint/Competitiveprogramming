class Solution:
    def interpret(self, command: str) -> str:
        ans=temp=""
        for char in command:
            temp+=char
            if temp=="G":
                ans+=temp
                temp=""
            elif temp=="(al)":
                ans+="al"
                temp=""
            elif temp=="()":
                ans+="o"
                temp=""
        return ans
        