def is_palindrome(s: str) -> bool:
    ls = s.lower()
    # Load only alphanumeric characters into the list for analysis
    ns = [s for s in ls if s.isalnum()]
    left = 0
    right = len(ns)-1
    while left < right:
        if ns[left] != ns[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    s = 'Do geese see God'
    res = is_palindrome(s)
    print("true" if res else "false")
