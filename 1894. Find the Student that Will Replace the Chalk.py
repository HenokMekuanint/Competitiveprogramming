class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total=sum(chalk)
        maximum=k%total
        i=0
        while i<len(chalk):
            if maximum-chalk[i]>=0:
                maximum-=chalk[i]
            else:
                return i
            i+=1
        return i
