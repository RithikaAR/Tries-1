class TrieNode:
    def __init__(self, c: str=''):
        self.char = c
        self.nodes = {}
        self.reach_word = False
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = self.root
        for w in word:
            if w not in n.nodes:
                n.nodes[w] = TrieNode(w)
            n = n.nodes[w]
        n.reach_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.root
        for w in word:
            if w not in n.nodes:
                return False
            n = n.nodes[w]
        return n.reach_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.root
        for w in prefix:
            if w not in n.nodes:
                return False
            n = n.nodes[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
