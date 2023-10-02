class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
        self.count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            
            cur=cur.children[char]
            cur.count+=1
        cur.is_end=True

    def search(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return True
    def sum_up(self,prefix):
        cur=self.root
        sumission=0
        for char in prefix:
            cur=cur.children[char]
            sumission+=cur.count
        return sumission
class Solution:   
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie=Trie()
        for word in words:
            trie.insert(word)
        ans=[]
        for word in words:
            ans.append(trie.sum_up(word))
        return ans
            
            
            
                
        
        
        
        