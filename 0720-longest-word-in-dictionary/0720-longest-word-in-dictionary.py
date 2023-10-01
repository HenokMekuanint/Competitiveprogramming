class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for char in word:
            if char not in  cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.is_end=True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie=Trie()
        for word in words:
            trie.insert(word)
        store=[]
        def dfs(trieNode,word,consec,at_the_beg):
            if not trieNode.children:
                if consec>1 or (trieNode.is_end and at_the_beg):
                    store.append(word)
                return consec
            for child in trieNode.children:
        
                if trieNode.children[child].is_end and at_the_beg:
                        dfs(trieNode.children[child],word+child,consec+1,at_the_beg)
                else:
                    if consec>0:
                        store.append(word)
            
        dfs(trie.root,"",0,True)
        if not store:
            return ""
        else:
            store.sort()
            max_len=0
            for elem in store:
                max_len=max(max_len,len(elem))
            for elem in store:
                if len(elem)==max_len:
                    return elem
        

        