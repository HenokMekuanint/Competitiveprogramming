class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        _dict=defaultdict(int)
        for i in range(len(order)):
            _dict[order[i]]=i
        for r in range(len(words)-1):
            cur,nxtwrd,pointer=words[r],words[r+1],0
            if nxtwrd in cur and len(cur)>len(nxtwrd):return False
            while pointer<min(len(cur),len(nxtwrd)):
                if _dict[cur[pointer]]<_dict[nxtwrd[pointer]]:
                    break
                elif _dict[cur[pointer]]==_dict[nxtwrd[pointer]]:
                    pointer+=1
                else:
                    return False
        return True