# BACKTRACKING

# Backtracking algorithms are problem solving algorithms that use the brute force approach
# for finding the desired output.  However, they are often faster than a naive brute force
# approach because they contain logic to eliminate work branches that we know will not
# generate the desired result.

# Brute force approaches evaluate all possible scenarios and choose the best solution

# Most of the time, backtracking is not used to find the optimal solution; in this case
# dynamic programming is used instead.  Backtracking is employed where there are multiple
# possible solutions to a problem and we want to know about all of them.

# There are three types of problem that can be solved via backtracking"
#   1) Decision - search for a feasible solution
#   2) Optimization - search for the best solution
#   3) Enumeration - find all feasible solutions

# Backtracking problems can be represented in a structure called a 'state tree' or 
# 'potential search tree'

# Operationally, a backtracking algorithm proceeds in the following steps:
#   1) Checks whether the given node is a valid solution or not
#   2) If the solution is not valid, the node and any subsequent nodes on the branch are 
#      discarded (this is the time saving piece)
#   3) Recursively enumerate all subtrees of the node to find a valid solution

# N Queens Problem
# Place N number of queens on an NxN chess board in such a way that no two queens can
# attack one another.  Queens can move left, right, up, down and diagonally. The following
# rules apply:
#   1) Queens may not be placed on the same column
#   2) Qeens may not be placed on the same row
#   3) Queens may not be diagonal from one another

# We can build the solution by adding queens to the board one by one and checking the 
# bounding function (rejection criteria) with each iteration

class NQueens:
    def __init__(self, n): # Number of Queens and number of rows and columns on the board will be the same
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(' Q ', end='') # Skip the default carriage return since we want it to look like a board
                else:
                    print(' - ', end='')
            print('\n')

    def is_place_safe(self, row, col):
        # Check horizontally
        for col_ind in range(self.n):
            if self.chess_table[row][col_ind] == 1:
                return False
            
        # -
        # Problem is implemented in such a way that only one queen is assigned to each column. Therefore, we do
        # not need logic to check for other queens in the same column.
        # -

        # Check diagonally bottom right to top left
        col_ind = col
        # Step backwards diagonally from current position. We do not need to check to the right of the current
        # position because we only place one queen at a time.
        for row_ind in range(row, -1, -1): 
            if row_ind < 0:
                break
            if self.chess_table[row_ind][col_ind] == 1:
                return False
            col_ind -= 1 # Decrement so that we can continue traversing the diagonal
        
        # Check diagonally top right to bottom left
        col_ind = col
        for row_ind in range(row, self.n): # Going this direction, we must increase the row by 1 instead of decrease
            if row_ind < 0:
                break
            if self.chess_table[row_ind][col_ind] == 1:
                return False
            col_ind -= 1 # Decrement so that we can continue traversing the diagonal        
        
        # If no competing queens have been found
        return True

    def solve(self, col):
        # Base case - we have placed all the queens.
        if col == self.n:
            return True
        # Because we place one queen per column, we can just iterate over the rows to assess whether or not
        # we've found a good spot for our queen.
        for row in range(self.n):
            if self.is_place_safe(row, col):
                self.chess_table[row][col] = 1
                # Now call solve recursively to check the other possiblities. If we can place the other queens
                # successfully, we'll have finished.
                if self.solve(col+1):
                    return True
                # If not, we must backtrack
                self.chess_table[row][col] = 0 # Remove the qeen from the current spot since we know it's not going to work
        
        return False
    
    def solve_NQueens(self):
        if self.solve(0): # Start at the very beginning
            self.print_queens()
        else:
            print("There is no solution for this configuration!")

queens = NQueens(4)
queens.solve_NQueens()