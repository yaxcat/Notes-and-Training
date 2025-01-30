# Divide and Conquer Algorithms

# Paradigm in which an algorithm is designed to break the problem into smaller,
# more easily solvable subproblems of a similar type.  When they are simple 
# enough to be solved directly, the solutions to the subproblems are combined to
# render the solution to the original problem.

# While DC algorithms can be similar to greedy algorithms, they're generally more
# complex and better at returning a truly optimal result

# Main property necessary to use divide and conquer is optimal substructure.  If
# a problem's substructer is optimal, it means that once an optimal solution for
# each of the subproblems can be found, they can be added up to the globally optimal
# solution

# FIBONACCI SERIES
#--------------------------
# Fibonacci series is a good example of a divide and conquer algorithm since the two
# computations can be broken down recursively until we get to 0 and 1 (first numbers
# in any Fibonacci sequence) and then sum of each of those recursive calls down the
# stack can be added up to get to the ultimate result

def fib(n):
    # Base case
    if n < 1:
        return "n cannot be negative"
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
    
#print(fib(10))


# NUMBER FACTOR
#--------------------------
# Given N, find the number of ways to express N as the sum of 1, 3, and 4.
# For example, if N = 4 the solution is: {4}, {1,3}, {3,1}, {1,1,1,1}

def numberFactor(n):
    # Base cases
    if n in (0, 1, 2):
        return 1 # 1 way to express 0 (empty set), 1 way to express 1 ({1}), and 1 way to express 2 ({1,1})
    elif n == 3:
        return 2 # Two ways to express 3 ({1,1,1} and {3})
    
    # Otherwise, break the problem down until hits one of the base cases.  We'll
    # solve these subproblems and add up their results to get our overall
    # solution (optimal structure)
    else:
        sub1 = numberFactor(n-1)
        sub2 = numberFactor(n-3)
        sub3 = numberFactor(n-4)
        return sub1 + sub2 + sub3
#print(numberFactor(50))    


# HOUSE ROBBER
#--------------------------
# There are N number of houses along a street with different amounts of money
# in each one. Starting at the beginning of the street, you must maximize the 
# amount of money you steal, but you cannot rob two houses which are adjacent

def houseRobber(houses, currentIndex):
    # Base case, we've moved past the last house, so quit
    if currentIndex >= len(houses):
        return 0
    # Recursively decide whether to rob the current house and skip the next (stealFirstHouse)
    # or skip the current house and move to the next (skipFirstHouse).
    # The function is called recursively with updated indices to ensure the correct house is skipped.
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)
        skipFirstHouse = houseRobber(houses, currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)
houses = [6,7,1,30,8,2,4]
#print(houseRobber(houses, 0))


# CONVERT STRING
#--------------------------
# S1 and S2 are are strings.  Using operations including delete, insert or
# replace, find the minimumn number of operations necessary to convert S2
# into S1.

# Examples:
#   - S1 = catch
#   - S2 = carch
#   - Answer = 1, replace r with t

#   - S1 = table
#   - S2 = tbres
#   - Answer = 3, insert 'a' into second position, replace 'r' with 'l' and delete 's'

def findMinStringOps(s1, s2, index1, index2):
    # BASE CASES
    # If we've traversed the entire control word, it means any characters left
    # on the word we want to mutate are extras and can be discarded.  So capture and 
    # return the number of characters to delete from the 2nd string
    if index1 == len(s1):
        return len(s2) - index2
    # If we've reached the end of the 2nd string, we must capture what remains of the
    # first string, so that those characters can be inserted into our mutating string
    if index2 == len(s2):
        return len(s1)-index1
    # If the characers for each string are identical, run the fn recursively to work
    # our way through the words
    if s1[index1] == s2[index2]:
        return findMinStringOps(s1, s2, index1+1, index2+1)
    # If not, explore all three possible operations.  This will form a tree of all
    # possible solutions, most of which will be suboptimal, but that is okay.  We
    # will select the best best branch in the tree at the end.
    else:
        # Define the subproblems and generate the result
        deleteOp = 1 + findMinStringOps(s1, s2, index1, index2+1) # Add 1 to index2 because we know there is a character we need to delete at index2 itself
        insertOp = 1 + findMinStringOps(s1, s2, index1+1, index2) # Add 1 to index1 because we know there is a character in s1 that is missing from s2
        replaceOp = 1 + findMinStringOps(s1, s2, index1+1, index2+1) # We're just doing a replace, so we increment each index by 1 to move on

        # Take the minimum possible number of operations
        return min(deleteOp, insertOp, replaceOp)

print(findMinStringOps("table", "tbrltt", 0, 0))


# ZERO ONE KNAPSACK PROBLEM
#--------------------------

# You have a knapsack with a finite capacity C.  Given N items
# with various weights and profits, determine the maximum
# profit you can hold given the mix of items.  The items cannot
# be subdivided.

# Mango- W:3, P:31
# Apple- W:1, P:26
# Orange- W:2, P:17
# Banana- W:5, P:72

# Knapsack capacity: 7

# This problem is similar to the house robber problem.  In order to find
# the answer, we must explore the space of all possible solutions and then choose
# the best one.

class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value

def ZeroOneKnapsack(items, capacity, current_index):
    # If we're over capacity or out of items, return zero 
    if capacity <= 0 or current_index < 0 or current_index >= len(items):
        return 0
    # Otherwise, we can break the problem into two subproblems to recursively explore the space of possibilities
    elif items[current_index].weight <= capacity:
        # Option 1: Include the current item and explore the remaining items with reduced capacity
        profit1 = items[current_index].value + ZeroOneKnapsack(items, capacity-items[current_index].weight, current_index+1)
       # Option 2: Exclude the current item and explore the remaining items with the same capacity
       #    - Note that Option 2 does not perform its own value calculation in the sense of adding
       #    - a new item's value.  Rather it delegates calculation of profit to further recursive 
       #    - calls.  The values it does return are the result of aggregations up the stack 
        profit2 = ZeroOneKnapsack(items, capacity, current_index+1)
        # Return the maximum profit obtained by either including or excluding the current item
        return max(profit1, profit2)
    else: # Item is too heavy
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

#print(ZeroOneKnapsack(items, 7, 0))


# LONGEST COMMON SUBSEQUENCE (LCS)
#--------------------------

# You are given two strings, s1, and s2.  You must find the longest subsequence 
# which is common to both strings.  The subsequence is defined as a sequence of
# characters that can derived from another sequence by deleting some elements,
# but never changing any.

# S1 = elephant
# S2 = erepat
# Result = 5 (eepat)

# Subproblems
#   Option 1 - Characters match
#       - 1 + f(2,8 : 2,6) add 1 for the match, then proceed to 2nd character in each string. 8 & 6 are lengths of strings
#   Option 2 - Characters do not match
#       - 0 + f(3,8 : 2,7) see if 3rd character in S1 matches 2nd in S2
#   Option 3 - Characters do match
#       - 0 + f(2,8 : 3,7) do the same thing as option 2 but reversed so that we can explore the entire possiblity space

def findLCS(s1, s2, ind1, ind2):
    # If we've traversed the entirety of either string, there can be no more matches
    if ind1 == len(s1) or ind2 == len(s2):
        return 0
    if s1[ind1] == s2[ind2]: # Characters match, so add 1 to result and proceed to the next characters in both strings
        return 1 + findLCS(s1, s2, ind1+1, ind2+1)
    # If the characters don't match, there are two possibilites to explore, we'll
    # do that recursively in the else block to look at all possibilites
    else:
        opt2 = findLCS(s1, s2, ind1+1, ind2) # Skip current character of S1
        opt3 = findLCS(s1, s2, ind1, ind2+1) # Skip current character of S2
        return max(opt2, opt3)
    
#print(findLCS("elephant", "erepat", 0, 0))


# LONGEST PALINDROMIC SUBSEQUENCE (LPS)
#--------------------------

# For a given string, S, find the longest palindromic subsequence. This is a
# sequence which can be derived from the parent sequence by deleting some
# elements without changing the order and also reads the same backwards and forwards

# Palindrome ex. - madam, racecar

# "elrmenmet" -> "ememe" -> 5
# length of "elrmenmet" is 9 characters

# Subproblems
#   Option 1 - Characters match
#       - 2 + f(2, 8).  If the first and last characters in the sequence match, add two. Then we must evaluate if the 2nd element from the front matches the 2nd element from the back and so on.
#   Option 2 - Characters do not match
#       0 + f(1, 8). If they don't match, we don't add anything. One option is to stay at the first character and evaluate the second character in from the back.
#   Option 3 - Characters do not match
#       0 + f(2, 9). The other thing we can try is to stay on the last character and evaluate the second element in from the front


def findLPS(s, startIndex, endIndex):
    # In this case, we have traversed through the middle of the list, so exit and return 0
    if startIndex > endIndex:
        return 0
    # In this case, we have reached the element in the middle of the string. The character
    # will always be equal to itself, so return 1 and exit
    elif startIndex == endIndex:
        return 1
    # Option 1
    # Option 1: If characters match, add 2 to our total and move inwards from both ends
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex+1, endIndex-1)
    # If the characters don't match, recursively explore all possibilites
    else:
        opt2 = findLPS(s, startIndex, endIndex-1) # Stay at current left position and move in from the right
        opt3 = findLPS(s, startIndex+1, endIndex) # Stay at current right position and move in from the left
        return max(opt2, opt3)
    

#print(findLPS("ELRMENMET", 0, 8))


# MINIMUM COST TO REACH THE LAST CELL
#--------------------------

# Given a 2D matrix, each cell has a cost associated with it.  Start from some 
# cell and navigate to (0, 0), finding the path which has the minimum possible cost.
# Movement is constrained such that you can only move left or up.

# Finds the minimum cost path given the movement constraints by starting at the row/col
# provided and working toward (0,0) in the top left
def findMinCost(twoDArray, row, col):
    # If either coordinate is < 0, we've passed the bounds of the array
    if row == -1 or col == -1:
        return float('inf')
    # If we've reached our goal point, return its cost so we can add it to the total
    elif row == 0 and col == 0:
        return twoDArray[0][0]
    # Otherwise, run our subproblems, which entail moving toward the origin by either
    # moving left from our input position, or up by 1.
    else:
        opt1 = findMinCost(twoDArray, row-1, col) # Move up
        opt2 = findMinCost(twoDArray, row, col-1) # Move left
        # Access the value at our current location and add it to the minimum cost
        # from the possible paths calculated by the recursive calls.
        return twoDArray[row][col] + min(opt1, opt2)

twoDList =  [[4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3]]

#print(findMinCost(twoDList, 4, 4))



# NUMBER OF PATHS TO REACH THE LAST CELL WITH A GIVEN COST
#--------------------------

# Given a 2D matrix, each cell has a cost associated with it.  Start from some 
# cell and navigate to (0, 0), finding the number of paths which can get to 
# (0, 0) for a given cost. Movement is constrained such that you can 
# only move left or up.

# Starts with the user specified cell and target cost. Initially, the target
# cost is decremented by the cost of the starting cell, since we're already 
# there.  Then, each time a move is made to a neighboring cell, the running
# cost is decremented again by the cost of the neighboring cell we've moved
# to.
def numberOfPaths(twoDAarray, row, col, cost):
    # If the remaining cost is negative, this path exceeds the allowed cost, so return 0.
    if cost < 0:
        return 0
    # If we've reached the origin point
    elif row == 0 and col == 0:
        # We're trying to hit that target cost exactly, so if our target
        # cost minus our running route cost are 0, we've done it. Add 1
        # for this route.
        if twoDAarray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        # If the row is 0, all we can do is track left
        return numberOfPaths(twoDAarray, 0, col-1, cost-twoDAarray[0][col])
    elif col == 0:
        # If the col is 0, all we can do is move up
        return numberOfPaths(twoDAarray, row-1, 0, cost - twoDAarray[row][0])
    else:
        opt1 = numberOfPaths(twoDAarray, row-1, col, cost - twoDAarray[row][col]) # Move up
        opt2 = numberOfPaths(twoDAarray, row, col-1, cost - twoDAarray[row][col]) # Move left
        return opt1 + opt2
    
smallerList =   [[4,7,1,6],
                [5,7,3,9],
                [3,2,1,2],
                [7,1,6,3]]
#print(numberOfPaths(smallerList, 3, 3, 25))