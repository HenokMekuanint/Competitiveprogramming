class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left=0
        right=len(tokens)-1
        score=0
        maxscore=0
        while left<=right and score>=0:
            if power-tokens[left]>=0:
                power=power-tokens[left]
                score+=1
                left+=1
                maxscore=max(maxscore,score)
            elif power-tokens[left]<0:
                power=power+tokens[right]
                score-=1
                right-=1
        return maxscore
