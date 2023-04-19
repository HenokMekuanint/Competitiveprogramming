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
            for j in range(len(words)):
                if words[j]>query:
                    ans.append(len(words)-j)
                    break
                elif j==len(words)-1 and words[j]<=query:
                    ans.append(0)
        return ans
                    
                