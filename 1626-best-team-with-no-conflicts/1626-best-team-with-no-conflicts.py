class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = list(zip(ages, scores))
        players.sort()  
        memo = {}

        def dp(index):
            if index == n:
                return 0

            if index in memo:
                return memo[index]

            max_score = players[index][1]

            for i in range(index + 1, n):
                if players[i][1] >= players[index][1]:
                    max_score = max(max_score, players[index][1] + dp(i))

    
            memo[index] = max_score

            return max_score

        max_team_score = 0
        for i in range(n):
            max_team_score = max(max_team_score, dp(i))

        return max_team_score
      
            
           
        
                
            
        