from typing import List

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    dig_list = list(digits)
    num_digs = len(dig_list)
    letter_combinations = []
    def dfs(dig_list, start, combo):
        lookup = {
            '2': ['A', 'B', 'C'], 
            '3': ['D', 'E', 'F'], 
            '4': ['G', 'H', 'I'], 
            '5': ['J', 'K', 'L'], 
            '6': ['M', 'N', 'O'], 
            '7': ['P', 'Q', 'R', 'S'], 
            '8': ['T', 'U', 'V'], 
            '9': ['W', 'X', 'Y', 'Z']
            }
        if start == num_digs:
            letter_combinations.append(''.join(combo).lower())
            return
        for l in lookup[dig_list[start]]:
            combo.append(l)
            dfs(dig_list, start+1, combo)
            combo.pop()

    dfs(dig_list,0,[])

    return letter_combinations

if __name__ == "__main__":
    digits = '56'
    res = letter_combinations_of_phone_number(digits)
    print(" ".join(res))
