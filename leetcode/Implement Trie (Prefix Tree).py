import copy
class TrieNode:

    def __init__(self, value):
        self.value = None
        if value:
            self.value = value
        self.length = None
        if self.value:
            self.length = len(self.value)
        self.next = [None for i in range(26)]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("$")

    def __str__(self):

        def exploreNode(node):
            result = []
            if node.value[-1] == "#":
                return [node.value]
            for child in node.next:
                if child:
                    for x in exploreNode(child):
                        result.append(node.value + x)
                    
            return result
        return str(exploreNode(self.root))


    def locateWord(self, word):
        if word == "#":
            return 0
        return ord(word[0]) - ord('a') + 1

    def compareWords(self, word1, word2):
        """
        compare words
        :type word1: str
        :type word2: str
        :rtype: int idx: break both words starting from idx(inclusive)
        -1: break word2 at idx
        1: break word1 at idx
        0: break both words at idxs
        """
        idx = 0
        while True:
            if idx >= len(word1):
                return (-1, idx)
            if idx >= len(word2):
                return (1, idx)
            if word1[idx] != word2[idx]:
                return (0, idx)
            idx += 1
        return None


    def insert(self, word, loc = None):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word: return
        wordValue = copy.deepcopy(word).lower()
        if loc is None: 
            loc = self.root
            wordValue += "#"
        if loc.next[self.locateWord(wordValue)] is None:
            loc.next[self.locateWord(wordValue)] = TrieNode(wordValue)
            return
        loc = loc.next[self.locateWord(wordValue)]
        jud, idx = self.compareWords(loc.value, wordValue)
        if jud >= 0:
            # print("insert", wordValue, "at", loc.value[:idx])
            self.insert(loc.value[idx:], loc)
        if jud <= 0:
            # print("insert", wordValue[idx:], "at", loc.value[:idx])
            self.insert(wordValue[idx:], loc)
        loc.value = loc.value[:idx]
        loc.length = len(loc.value)
        return

    def search(self, word, loc = None):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word: return False
        wordValue = copy.deepcopy(word).lower()
        if loc is None: 
            loc = self.root
            wordValue += "#"

        loc = loc.next[self.locateWord(wordValue)]
        if loc is None: return False
        jud, idx = self.compareWords(loc.value, wordValue)
        if jud >= 0:
            return False
        else:
            if len(loc.value) == len(wordValue):
                return True
            return self.search(wordValue[loc.length:], loc)
        return False

    def startsWith(self, prefix, loc = None):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix: return False
        wordValue = copy.deepcopy(prefix).lower()
        if loc is None: 
            loc = self.root

        loc = loc.next[self.locateWord(wordValue)]
        if loc is None: return False
        jud, idx = self.compareWords(loc.value, wordValue)
        if jud >= 0:
            if len(wordValue) <= len(loc.value) and jud == 1:
                return True
            return False
        else:
            # print(wordValue)
            # print("find", idx, wordValue[idx:], "at", loc.value)
            # print(loc.value, wordValue)
            if len(loc.value) == len(wordValue):
                return True
            return self.startsWith(wordValue[idx:], loc)
        return False





# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("")
obj.insert("Tire")
obj.insert("insert")
obj.insert("insert")
obj.insert("startsWith")
obj.insert("startsWith")
obj.insert("search")
obj.insert("search")
print(obj)
print(obj.search("a"))
print(obj.search(""))
print(obj.search("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(obj.search("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"))
print(obj.search("aaa"))
# param_3 = obj.startsWith(prefix)
print()
print(obj.startsWith("a"))
print(obj.startsWith(""))
print(obj.startsWith("aa"))
print(obj.startsWith("aaa"))
print(obj.startsWith("ab"))
print(obj.startsWith("aab"))