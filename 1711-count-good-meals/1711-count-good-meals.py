class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        import math
        counter=0
        dicti={}
        power=[]
        for num in  deliciousness:
            dicti[num]=int(dicti.get(num,0)+1)
        for i in range(0,22):
            power.append(2**i)
        for cur_num in (dicti):
            for j in range(len(power)):
                diff=(power[j]-cur_num)
                if cur_num==diff:
                    counter+=((dicti[cur_num])*(dicti[cur_num]-1)//2) 
                elif cur_num>=diff and diff in dicti:
                    counter+=dicti[cur_num]*dicti[diff]
        counter=counter % ((10**9)+7)
        return  counter
                
            