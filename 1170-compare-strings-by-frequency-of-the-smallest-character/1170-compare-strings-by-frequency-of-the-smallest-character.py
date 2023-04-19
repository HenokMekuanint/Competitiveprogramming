class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        from collections import Counter
        def freq_small(word):
            freq=Counter(word)
            freq_keys=sorted(list(freq.keys()))
            return freq[freq_keys[0]]
        for i in range(len(queries)):
            queries[i]=freq_small(queries[i])
        for j in range(len(words)):
            words[j]=freq_small(words[j])
        words.sort()
        ans=[]
        for query in queries:
            left=0
            right=len(words)-1
            left_most_index=None
            while left<=right:
                mid=(left+right)//2
                if words[mid]>query:
                    left_most_index=mid
                    right=mid-1
                    
                else:
                    left=mid+1
            if left_most_index==None:
                ans.append(0)
            else:ans.append(len(words)-left_most_index)
                
        return ans
                    
                