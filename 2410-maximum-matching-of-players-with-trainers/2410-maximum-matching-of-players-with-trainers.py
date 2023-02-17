class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()        
        ptr1=0
        ptr2=0
        counter=0
        while ptr1<len(players) and ptr2<len(trainers):
            if players[ptr1]>trainers[ptr2]:
                ptr2+=1
            elif players[ptr1]<=trainers[ptr2]:
                counter+=1
                ptr2+=1
                ptr1+=1
        return counter
                