class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]
    
    

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            
            if not cur.children[ord(char.lower())-97]:
                cur.children[ord(char.lower())-97]=TrieNode()

            cur=cur.children[ord(char.lower())-97]
        cur.is_end=True

                
        

    def search(self, word: str) -> bool:
        
        memo = {}

        def dfs(node, i):
            if i == len(word):
                return node.is_end

            if (node, i) in memo:
                return memo[(node, i)]

            char = word[i]

            if char == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        memo[(node, i)] = True
                        return True
                memo[(node, i)] = False
                return False

            if not node.children[ord(char.lower()) - 97]:
                memo[(node, i)] = False
                return False

            result = dfs(node.children[ord(char.lower()) - 97], i + 1)
            memo[(node, i)] = result
            return result

        return dfs(self.root, 0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)