def maximal_square(matrix: list[list[int]]) -> int:
    # Handle the edge case of a null matrix
    if not matrix:
        return 0
    
    # Retrieve the dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])


    # Generate a grid equal to the dimensions of the input matrix
    # to build up our results
    dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]


    # Initialize variable to keep track of biggest square found as we go
    best = 0

    # Process the top and bottom boundaries first
    # Fill in the leftmost column
    for row in range(num_rows):
        dp[row][0] = matrix[row][0] # Boundary will just reflect whatever is in the matrix; fine since its 0 or 1
        best = max(dp[row][0], best) # Will either be 1 or 0 since we're on the boundary
    # Fill in top row
    for col in range(num_cols):
        dp[0][col] = matrix[0][col]
        best = max(dp[0][col], best)

    # Starting from the first unprocessed cell in the top left, fill in the internal cells
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            # Skip 0 cells
            if matrix[row][col] == 0: 
                continue
            # At each iteration, we must analyze the candidate squares we have built up so far using smaller
            # subsets of the overall matrix. We select the minimum precomputed square so far. This is because
            # the square size formed at the current cell (matrix[row][col]) can only be as big as the minimum
            # defined by the three coordinates we are testing, due to the nested nature of the geometry.
            dp[row][col] = min(
                dp[row-1][col], # Up from current position
                dp[row][col-1], # Left from current position
                dp[row-1][col-1] # Diagonal from current position
            ) + 1 # Add 1 for the current cell, since it's part of the new expanded square
            best = max(dp[row][col], best)

    return best*best # question asks for area

if __name__ == "__main__":
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = maximal_square(matrix)
    print(res)
