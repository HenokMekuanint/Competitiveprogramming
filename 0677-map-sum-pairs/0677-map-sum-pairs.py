class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]
        self.count={}
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def char_to_integer(self,chr):
        return ord(chr.lower())-97
    
    def insert(self,word:str,value:int)->None:
        cur=self.root
        for char in word:
            index=self.char_to_integer(char)
            if not cur.children[index]:
                cur.children[index]=TrieNode()
            cur=cur.children[index]
            cur.count[word]=value
            
            cur.is_end=True
  
        
    def search(self,prefix):
        cur=self.root
        summission=0
        cur=self.root
        
        for char in prefix:
            index=self.char_to_integer(char)
            if  not cur.children[index]:
                return 0
            cur=cur.children[index]
        for elem in cur.count:
            summission+=cur.count[elem]
        return summission

                
class MapSum:
    def __init__(self):
        self.trie=Trie()
        self.seen=set()
        
    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key,val)
    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)