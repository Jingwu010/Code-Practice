class TrieNode:
        def __init__(self, value):
            self.value = value
            self.isWord = False
            self.next = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        loc = self.root
        for c in word.lower():
            if c not in loc.next:
                loc.next[c] = TrieNode(c)
            loc = loc.next[c]
        loc.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word: return False
        loc = self.root
        for c in word.lower():
            if c in loc.next:
                loc = loc.next[c]
            else: return False
        if loc.isWord: return True
        else: return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix: return False
        loc = self.root
        for c in prefix.lower():
            if c in loc.next:
                loc = loc.next[c]
            else: return False
        return True
        
obj = Trie()
obj.insert("app")
obj.insert("apple")
obj.insert("beer")
obj.insert("add")
obj.insert("jam")
obj.insert("rental")
print()
print(obj.search("app"))
print(obj.search("apple"))
print(obj.search("add"))
print(obj.search("beer"))
print(obj.search("apple"))
print()
print(obj.startsWith("app"))
print(obj.startsWith("apps"))
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)