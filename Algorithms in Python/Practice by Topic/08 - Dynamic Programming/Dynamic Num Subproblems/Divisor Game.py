# Determine if the input n is a winnable position using bottom up dynamic
# programming
def divisor_game(n: int) -> bool:
    # Initialize a list to hold the tabulations which determine winnability
    # Program will work from the smallest subproblem on the left towards the
    # final result at the right
    dp = [False] * (n+1)

    # State space is defined by nodes which are either 'winning' or 'losing'
    # A winning node is one in which a player can force a win by playing
    # optimally, while a losing position is one where the opponent can force
    # a win.

    # Explore the state space - 
    # Loop over the entire space of possible numbers
    for i in range(2, n+1): # Don't need to consider 0 & 1 since they mark the termination of the game
        # J represents a number the player might choose
        for j in range(1, i): # Start from the base case: 1
            # A player may only choose a number that divides evenly into the current
            # total. Numbers not satisfying this criteria are handled gracefully due
            # to the way the subproblem list is initialized
            if i % j == 0:
                # If dp[i-j] was a losing position, moving to it will make it a winning
                # position by definition.
                dp[i] = dp[i] or not dp[i - j]
                print("------", j, dp)
            print("---", j, dp)
        print(i, dp)

    return dp[-1] # Last element will be the solution

if __name__ == "__main__":
    n = 8
    res = divisor_game(n)
    print("true" if res else "false")
