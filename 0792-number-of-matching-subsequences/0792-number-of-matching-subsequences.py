class Trie:
    def __init__(self):
        self.root=TrieNode()
    def char_to_integer(self,chr):
        return ord(chr.lower())-97
    
    def insert(self,word):
        cur=self.root
        for char in word:
            index=self.char_to_integer(char)
            if not cur.children[index]:
                cur.children[index]=TrieNode()
            cur=cur.children[index]
        cur.is_end=True
        cur.count+=1
    
class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]
        self.count=0      
class Solution(object):

    def numMatchingSubseq(self, s, words):
        
        ans=[0]
        trie = Trie()
        root = trie.root



        for word in words:
            trie.insert(word)

        def find_idx(ch, i):
            
            for j in range(i, len(s)):
                if s[j] == ch:
                    return j
            return -1

        def solve(node,last_idx):
            
            
            if node.is_end:
                ans[0] += node.count

            for i in range(len(node.children)):
                if node.children[i]:
                    idx = find_idx(chr(i+97), last_idx + 1)
                    if idx != -1:
                        solve(node.children[i], idx)
            return
        solve(root,-1)
        return ans[0]