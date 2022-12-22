class Solution:
    def similarPairs(self, words: List[str]) -> int:
        coll=defaultdict(int)
        _sum=0
        for word in words:
            _str=""
            for letter in word:
                if letter not in _str:
                    _str+=letter
            _str=''.join(sorted(_str))
            coll[_str]+=1
        for w in coll:
            if coll[w]>1:
                _sum+=((coll[w])*(coll[w]-1)/2)
        return int(_sum)
                    
                
        