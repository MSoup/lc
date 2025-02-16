class TrieNode:
    # Initialize a TrieNode with a dictionary to hold children nodes and a flag to mark word's end
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def suggestedProducts(self, products, searchWord):
        result = []
        trie = Trie()
        for product in products:
            trie.add(product)

        current = trie.trie # start at root
        built_word = ""
        for char in searchWord:
            built_word += char
            if char not in current.children:
                remaining = len(searchWord) - len(built_word) + 1
                for _ in range(remaining):
                    result.append([])
                break
            
            current = current.children[char]
            suggestions = []
            

            def dfs(node, word):
                if len(suggestions) == 3:
                    return
                if node.isEnd:
                    suggestions.append(word)
                for c in sorted(node.children.keys()):
                    dfs(node.children[c], word + c)

            dfs(current, built_word)
            result.append(suggestions) 
        return result

        
        

class Trie:
    def __init__(self):
        self.trie = TrieNode()
    def add(self, word):
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True
