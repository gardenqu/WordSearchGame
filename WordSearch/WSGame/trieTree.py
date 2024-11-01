''' Define the TrieNode Class 
    Each node in the Trie will have 2 attributes
       1) Children: A dictionary where the Keys are charcters and the values are the child nodes
       2) is_end_of_word: A boolean indicating whether the current node marks the end of a word
    '''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

'''Define the Trie Class
 The Trie class itself will contain:
    1) a root node (an instance of the TrieNode
    2) Methods to insert words, search for words, and check for prefixes
    
    In a Trie, each node can have multiple children, where each child corresponds to a character. 
    The children attribute of a node is typically a dictionary (or similar structure) 
    that maps characters to their respective child TrieNode instances.

    The Trie validates the words found by players by checking if sequences of letters are real words from the predefined list.'''

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    #insert a word into the Trie
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True
    # Search for a word in the Trei
    def search(self,word):
        node=self.root

        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_end_of_word
    
    # Check if there is any word in the Trie that starts with the given prefix
    def start_with(self,prefix):
        node=self.root

        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
    

    def _print_words(self, node, prefix, words):
        if node.is_end_of_word:  # If this node marks the end of a word
            words.append(prefix)  # Add the constructed word to the list
            
        for char, child_node in node.children.items():  # Traverse the children
            self._print_words(child_node, prefix + char, words)  # Recursive call


    def print_words(self):
        words = []  # List to store the words
        self._print_words(self.root, '', words)  # Start from the root with an empty prefix
        return words
    
    
    def is_empty(self):
        # Check if the root node has no children
        return len(self.root.children) == 0

