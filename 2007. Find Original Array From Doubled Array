class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = Counter(changed)
        ans =[]
        if len(changed) % 2 !=0:
            return []
        for k in count: 
            if k == 0:
                if count[k] % 2 != 0:
                    return []
            if ((2 * k) not in count.keys()) and ((k/2) not in count.keys()):
                return []

        if (not(any(changed))):
            changed =  changed[:(len(changed))//2]
            return changed

        for i in count:
            if count[i] == 0:
                    continue
            if (i== 0):
                count[i] = (count[i]//2)
            elif (2 * i) in count.keys():
                if count[2 * i ] >= count[i]:
                    count[2 * i] = count[2 * i] - count[i]
                else:
                    return []

        for i in count:
            for j in range(count[i]):
                ans.append(i)
        return ans
