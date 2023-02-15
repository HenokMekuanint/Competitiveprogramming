class Solution:
    def compress(self, chars: List[str]) -> int:
        left=0
        count=1
        for right in range(1,len(chars)+1):
            if right<len(chars) and chars[right]==chars[right-1]:
                count+=1
            else:
                chars[left]=chars[right-1]
                left+=1
                if count>1:
                    for k in str(count):
                        chars[left]=k
                        left+=1
                    count=1
        chars=chars[:left]
        return left
                
                
        