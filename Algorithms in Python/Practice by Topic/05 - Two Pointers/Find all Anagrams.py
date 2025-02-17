from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    starts = [] # Holds the starting position of the anagram
    ol = len(original)
    cl = len(check)

    # A goal is to avoid the extra overhead incurred by a dictionary
    # so use lists to mirror that functionality
    # Store the number of occurances for each character during a 
    # check
    check_frequency = [0]*26    
    # Store the number of occurances for each character within
    # the current window
    window = [0]*26
    # Retrieve the ASCII value of 'a'. This is used as a 
    # correction factor so that we can start our lists at index 0
    a = ord('a') # 97
    # Use two windows for convenience and readability. Could use
    # one but this would require additional conditionals or 
    # redundant calculation
    # First window - Loop over the length of 'check'. Record the
    # frequency distribution of characters in both strings
    for i in range(cl):
        check_frequency[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1
    # If the frequency distributions are identical, then the current
    #  window is a permutation (anagram) of check, so we append its 
    # starting position.
    if window == check_frequency:
        starts.append(0)
    # Second window - Picking up from boundary of the first window
    # slide this window along the remaining length of the list. 
    for i in range(cl, ol):
        # Decrement the number of occurances of the given letter in
        # original by 1 as the leftmost element drops outside of the
        # window boundary
        window[ord(original[i-cl]) - a] -= 1
        # Perform the reverse operation for the character on the 
        # right which slides into the window boundary
        window[ord(original[i]) - a] += 1
        # Add the starting index if an anagram is found
        if window == check_frequency:
            starts.append(i-cl+1)
    return starts

if __name__ == "__main__":
    txt1 = 'abab'
    txt2 = 'ab'
    original = txt1
    check = txt2
    res = find_all_anagrams(original, check)
    print(" ".join(map(str, res)))
