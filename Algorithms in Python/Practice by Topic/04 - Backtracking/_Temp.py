def decode_ways(digits: str) -> int:
    memo = {}
    num_digs = len(digits)

    def helper(start_ind):
        if start_ind == num_digs:
            return 1
        ways = 0
        # Cannot decode a digit that starts with a 0 so short circuit
        # this branch
        if digits[start_ind] == 0:
            return ways
        # Decode 1 digit
        ways += helper(start_ind + 1)
        # Decode 2 digits
        if int(digits[start_ind:start_ind+2]) >= 10:
            ways += helper(start_ind + 2)

        return ways
    return helper(0)

if __name__ == "__main__":
    digits = '999'
    res = decode_ways(digits)
    print(res)
