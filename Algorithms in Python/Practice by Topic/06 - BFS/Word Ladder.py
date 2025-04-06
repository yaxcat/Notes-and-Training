from typing import List
from collections import deque

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    whitelist = set(word_list)
    visited = {begin:0}

    # Exit immediately if the end is not in the whitelist
    if end not in whitelist:
        return -1

    # Naively creates a new word by mutating the input word at the given position for
    # every letter in the alphabet
    def get_neighbors(word, position):
        results = []
        for letter in letters:
            new_word = word[:position] + letter + word[position+1:]
            if new_word != word and new_word in whitelist:
                results.append(new_word)
        return results
    
    def bfs(root):
        word_len = len(root)
        q = deque([root])
        while q:
            curr_node = q.popleft()
            # Loop over each letter in the current word (node) and generate a list of
            # potentially viable words that may be formed by changing that letter
            for i in range(word_len):
                for neighbor in get_neighbors(curr_node, i):
                    # Prune by skipping off target and previously visited words
                    if neighbor in visited:
                        continue
                    # Update visited and q and return the number of steps if found
                    visited[neighbor] = visited[curr_node]+1
                    if neighbor == end:
                        return visited[neighbor]
                    q.append(neighbor)
        return -1 # If it is not possible to get to the end
    return bfs(begin)

if __name__ == "__main__":
    begin = 'fool'
    end = 'sage'
    s = 'fool pool poll pole pale sale sage'
    word_list = s.split()
    res = word_ladder(begin, end, word_list)
    print(res)
