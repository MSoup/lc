class TrieNode:
    # Initialize a TrieNode with a dictionary to hold children nodes and a flag to mark word's end
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = Trie()
    def suggestedProducts(self, products, searchWord):
        # Create trie
        for word in products:
            self.root.add(word)

        prefix = ""
        result = []
        for c in searchWord:
            prefix += c
            matches = self.getMatches(prefix)
            result.append(matches)
        return result

    def getMatches(self, prefix):
        curr = self.root.trie
        for c in prefix:
            # Append [], there are zero possible matches
            if c not in curr.children:
                return []
            # Change node to explore deeper into prefix
            curr = curr.children[c]

        matches = []
        self.dfs(curr, matches, prefix)
        return matches

    def dfs(self, curr, matches, prefix):
        # Explore all baths and build matches
        if len(matches) == 3:
            return
        if curr.isEnd:
            matches.append(prefix)
        
        # sorted to ensure its lexicographically minimum
        for key in sorted(curr.children.keys()):
            self.dfs(curr.children[key], matches, prefix + key)


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
