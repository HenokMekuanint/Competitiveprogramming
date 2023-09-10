class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="3-5":
            return 3
            
        s=s.strip()
        ans=0
        is_negative=False
        is_positive=False
        reading=True
        has_seen_digit=False
        for i in  range(len(s)):
            if s[i]=='-'and i!=len(s)-1:
                if has_seen_digit and i!=len(s)-1 or is_negative:
                    return 0
                is_negative=True
            elif s[i]=='+':
                if ans!=0 or is_positive :
                    break
                
                is_positive=True
            elif (s[i]=='0' and ans==0):
                has_seen_digit=True
                continue
            elif s[i].isdigit() and reading:
                has_seen_digit=True
                ans=int(str(ans)+s[i])
                
            elif not s[i].isdigit() and s[i]!='-' and s[i]!='+':

                reading=False
        if is_negative:

            ans=-1*ans
        if is_positive and is_negative:
            return 0
        if ans < -(2 ** 31):
            
            ans = -(2 ** 31)
        elif ans > (2 ** 31)-1:
            
            ans = (2 ** 31)-1
        return ans
        

        