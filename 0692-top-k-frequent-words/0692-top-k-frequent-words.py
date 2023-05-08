class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)
        list_word=[]
        for word,frequency in freq.items():
            heapq.heappush(list_word,(-1*frequency,word))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(list_word)[1])

        return result
            
        