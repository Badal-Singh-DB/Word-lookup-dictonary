class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def auto_suggestions(self, prefix):
        def _suggestions(node, prefix):
            if node.is_end_of_word:
                suggestions.append(prefix)
            for char, child_node in node.children.items():
                _suggestions(child_node, prefix + char)

        node = self.root
        suggestions = []
        for char in prefix:
            if char not in node.children:
                return suggestions
            node = node.children[char]
        _suggestions(node, prefix)
        return suggestions
