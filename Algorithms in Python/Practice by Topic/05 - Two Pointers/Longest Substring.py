# Uses a sliding window to find the longest substring without repeating characters
def longest_substring_without_repeating_characters(s: str) -> int:
    su = set(s) # Remove duplicate characters using set
    char_count = {c:0 for c in su} # Create a dictionary to hold the character count 
    longest_substring = 0
    slow = 0
    # Loop over the input string and find the longest substring without repeating
    # chracters
    for fast in range(0, len(s)):
        char_count[s[fast]] += 1
        # If any character has a count greater than than 1, shrink the window by moving
        # pointer rightward until the first instance of the duplicate character is to
        # the left of the window boundary
        while char_count[s[fast]] > 1:
            char_count[s[slow]] -= 1
            slow += 1
        longest_substring = max(longest_substring, fast-slow+1) # Add 1 to account for the inclusive nature of indices

    return longest_substring

if __name__ == "__main__":
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)
