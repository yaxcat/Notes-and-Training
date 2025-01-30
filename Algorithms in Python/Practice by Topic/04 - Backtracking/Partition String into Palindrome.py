from typing import List

def partition(s: str) -> List[List[str]]:
    input_len = len(s)
    all_palindromes = []
    # Determines if a given substring is a palindrome by comparing it to its reversed version.
    # Used to validate substrings when building palindrome partitions.
    def is_palindrome(prefix):
        return prefix == prefix[::-1] 
    # Recursively explores the state space tree searching substrings of the input string that are palindromes
    def dfs(start, substrings):
        # Base case - When our starting position is equal to the length of the input
        # string, stop, since there are no characters left to traverse
        if start == input_len:
            all_palindromes.append(substrings[:]) # Append any palindromic substrings we have found from the current character position. substrings[:] ensures a copy of the current list is appended (to avoid potential side effects if substrings were modified later).
            return
        # Loop through potential substrings starting from the current position. Each iteration slices the string 
        # from 'start' to the current 'end' position. The range dynamically adjusts as 'start' is updated 
        # during recursive calls.
        for end in range(start+1, input_len+1):
            # Extract a substring from 'start' to 'end' and check if it's a palindrome.
            prefix = s[start:end] 
            # If the substring is a palindrome, continue exploring this branch of the state space tree.
            # Non-palindromic substrings are skipped, and the loop advances to the next potential substring.
            if is_palindrome(prefix): 
                # Recursively explore the branch corresponding to the current palindromic prefix. The 'end' position 
                # becomes the new starting point, allowing the function to process subsequent substrings.
                dfs(end, substrings + [prefix])
    dfs(0, [])
    return all_palindromes

if __name__ == "__main__":
    s = 'aab'
    res = partition(s)
    for row in res:
        print(" ".join(row))
