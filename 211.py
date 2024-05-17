class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current['*'] = ''

    def search(self, word: str) -> bool:
        def dfs(node,word:str):
            if len(word)==0:
                return '*' in node
            letter = word[0]
            if letter != '.':
                if letter not in node:
                    return False
                return dfs(node[letter],word[1:])

            for item in node.keys():
                if item == '*':
                    continue
                if dfs(node[item],word[1:]):
                    return True
            return False

        return dfs(self.root,word)

word_d = WordDictionary()
word_d.addWord("at")
word_d.addWord("and")
word_d.addWord("an")
word_d.addWord("and")
print(word_d.search("a"))
print(word_d.search(".at"))
word_d.addWord("bat")
print(word_d.search(".at"))