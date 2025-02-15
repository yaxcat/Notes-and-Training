from typing import List

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    results = []
    path = []
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def dfs(start):
        if start == len(digits):
            results.append(''.join(path))
            return
        for letter in keypad[digits[start]]:
            path.append(letter)
            dfs(start+1)
            path.pop()
    dfs(0)
    return results

if __name__ == "__main__":
    digits = '56'
    res = letter_combinations_of_phone_number(digits)
    print(" ".join(res))
