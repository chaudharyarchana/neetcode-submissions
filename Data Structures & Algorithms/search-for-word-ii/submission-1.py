
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True

        ROWS = len(board)
        COLS = len(board[0])

        ans = []
        visited = set()

        def dfs(r, c, node, path):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children):
                return

            visited.add((r, c))

            ch = board[r][c]
            node = node.children[ch]
            path.append(ch)

            if node.end:
                ans.append("".join(path))
                node.end = False          # avoid duplicates

            dfs(r + 1, c, node, path)
            dfs(r - 1, c, node, path)
            dfs(r, c + 1, node, path)
            dfs(r, c - 1, node, path)

            path.pop()
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, [])



class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True

        ROWS = len(board)
        COLS = len(board[0])

        ans = []
        visited = set()

        def dfs(r, c, node, path):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children):
                return

            visited.add((r, c))

            ch = board[r][c]
            node = node.children[ch]
            path.append(ch)

            if node.end:
                ans.append("".join(path))
                node.end = False          # avoid duplicates

            dfs(r + 1, c, node, path)
            dfs(r - 1, c, node, path)
            dfs(r, c + 1, node, path)
            dfs(r, c - 1, node, path)

            path.pop()
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, [])

        return ans