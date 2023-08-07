#User function Template for python3
from collections import *

class Solution:
    def findOrder(self,alien_dict, N, K):
        
    # code here
        graph = defaultdict(list)
        in_degree = {ch : 0 for word in alien_dict for ch in  word}
        
        for i in range(N-1):
            
            first_word = alien_dict[i]
            second_word = alien_dict[i+1]
            small = min(len(first_word),len(second_word))
            
            for j in range(small):
                if first_word[j] != second_word[j]:
                    graph[first_word[j]].append(second_word[j])
                    in_degree[second_word[j]] += 1
                    break
        
        arr = [ch for ch in in_degree if in_degree[ch] == 0]
        
        queue = deque(arr)
        ans = []
        while queue:
            
            node  = queue.popleft()
            ans.append(node)
            
            for edge in graph[node]:
                
                in_degree[edge] -= 1
                if in_degree[edge] == 0:
                    
                    queue.append(edge)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends