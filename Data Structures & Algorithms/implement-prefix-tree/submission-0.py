class PrefixTree:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:  # bin
            if ch not in curr:
                curr[ch] = {}   # curr = {b : {}}
            
            curr = curr[ch] # now curr point to b : {} -> {}
        curr["*"] = True # end of word


    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]

        return "*" in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
        
        