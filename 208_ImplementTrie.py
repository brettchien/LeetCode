class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.end = False
        
    def __contains__(self, key):
        return key in self.children
        
    def __getitem__(self, key):
        return self.children[key]

    def __setitem__(self, key, value):
        if key not in self.children:
            self.children[key] = value

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = TrieNode
            node = node[ch]
        node.end = True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for ch in word:
            if ch in node:
                node = node[ch]
            else:
                return False
        return node.end
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch in node:
                node = node[ch]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
if __name__ == "__main__":
    trie = Trie()
    trie.insert("a")
    print trie.search("a"), trie.startsWith("a")
