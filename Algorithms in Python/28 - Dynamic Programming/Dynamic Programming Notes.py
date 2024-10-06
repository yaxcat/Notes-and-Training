# DYNAMIC PROGRAMMING

# Dynamic programming is an algorithmic technique for solving optimization problems by
# breaking them down into simpler subproblems and utilizing the fact that the optimal
# solution to the overall problem depends on the optimal solution to the subproblems.

# Dynamic programming requires two things - 
#   1) Optimal substructure
#   2) Overlapping subproblems

# It is is similar to divide and conquer techniques in that it breaks big
# problems down into smaller subproblems.  However, in dynamic programming, if subproblems 
# overlap (have to be solved multiple times) redundant computations are avoided by reusing
# the results of overlapping problems. Additionally, dynamic programming is applied to problems
# with an optimal substructure, where the overall solution can be constructed from the 
# optimal solutions to overlapping subproblems.  In divide-and-conquer techniques, the 
# subproblems can be solved independently of one another.

# Two approaches
#   1) Top Down - Memoization: Solve the bigger problem by recursively finding the solution to
#      smaller subproblems. When a subproblem is solved, its result is cached so that we don't
#      end up solving it repeatedly. Storing the results of already solved problems is called
#      'memoization'.
#   2) Bottom Up = Tabulation: This solution avoids recursion.  Instead, we solve related sub-
#      problems first and use their results to fill up a table.  Based on the results fo the 
#      table, the solution to the top/big problem is found.  Time complexity will typically be
#      better since recursion is avoided.  Overall, using a bottom-up approach is usually better
#      all around since the stack is not used, but trying to identify the base problem can be
#      quite difficult and this is why memoization is seen more frequently in the wild.  


# Examples - 

# NUMBER FACTOR
#--------------------------
# Given N, find the number of ways to express N as the sum of 1, 3, and 4.
# For example, if N = 4 the solution is: {4}, {1,3}, {3,1}, {1,1,1,1}

# Top Down
def numberFactorTD(n, memDict):
    # Base cases
    if n in (0, 1, 2):
        return 1 # 1 way to express 0 (empty set), 1 way to express 1 ({1}), and 1 way to express 2 ({1,1})
    elif n == 3:
        return 2 # Two ways to express 3 ({1,1,1} and {3})
    
    # Otherwise, break the problem down until hits one of the base cases.  We'll
    # solve these subproblems and add up their results to get our overall
    # solution (optimal structure)
    else:
        # Check to see if the value for n has already been computed via the dictionary
        # If not, we'll need to recursively break the problem down and store the result
        # in the dictionary for future lookups.
        if n not in memDict:
            sub1 = numberFactorTD(n-1, memDict)
            sub2 = numberFactorTD(n-3, memDict)
            sub3 = numberFactorTD(n-4, memDict)
            memDict[n] = sub1 + sub2 + sub3
        return memDict[n]
#print(numberFactorTD(50, {}))    


# Bottom up
def numberFactorBU(n):
    # Base cases are stored in the initial list
    # n =  0  1  2  3
    tab = [1, 1, 1, 2]
    # Now loop through the range of values for n and iteratively build up to the final 
    # result
    for i in range(4, n+1): # Start at the first non-base case position and continue until we reach n
        tab.append(tab[i-1] + tab[i-3] + tab[i-4]) # Calculate the result for each subproblem as we work our way up
    return tab[n] 
#print(numberFactorBU(5))    


# HOUSE ROBBER
#--------------------------
# There are N number of houses along a street with different amounts of money
# in each one. Starting at the beginning of the street, you must maximize the 
# amount of money you steal, but you cannot rob two houses which are adjacent

houses = [6,7,1,30,8,2,4]

# Top Down
def houseRobberTD(houses, currentIndex, memDict):
    # Base case, we're at the end of the block
    if currentIndex >= len(houses):
        return 0
    else:
        # Using memoization, we check to see if the subproblem has been solved
        # before computing a result
        if currentIndex not in memDict:
            stealFirstHouse = houses[currentIndex] + houseRobberTD(houses, currentIndex+2, memDict)
            skipFirstHouse = houseRobberTD(houses, currentIndex+1, memDict)
            memDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return memDict[currentIndex]
#print(houseRobberTD(houses, 0, {}))

# Bottom Up
def houseRobberBU(houses):
    # Initialize a DP array to store max money starting from house i
    temp = [0]*(len(houses)+2) # Add two extra elements to handle boundary conditions for the last house
    # Start at the last house and work backwards
    for i in range(len(houses)-1, -1, -1):  # Use reverse iteration because we must process future decisions before the current one.  We know those last two (non-existent) houses are worth 0, so its easy to work our way up from there
        # Either rob current house i and add the money from two houses ahead (temp[i+2]),
        # or skip current house and take the best solution from the next house (temp[i+1])
        temp[i] = max(houses[i]+temp[i+2], temp[i+1]) # Take the max of stealing from the first house or skipping it
    return temp[0]
print(houseRobberBU(houses))

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

# Top Down
def findMinStringOpsTD(s1, s2, index1, index2, memDict):
    # Base cases
    if index1 == len(s1): # We have reached the end of the control string
        return len(s2) - index2 # Calculate the # of characters we need to drop from the mutating string
    if index2 == len(s2): # we have reached the end of the word we're trying to mutate
        return len(s1) - index1 # Calculate the # of characters we need to add to the mutating string
    if s1[index1] == s2[index2]: # Characters in each word are identical
        return findMinStringOpsTD(s1, s2, index1+1, index2+1, memDict) # Recursively work through the words
    else: # Characters don't match.  One of three operations will be optimal.  We must test all.
        dictkey = str(index1) + str(index2)
        if index2 not in memDict:
            deleteOp = 1 + findMinStringOpsTD(s1, s2, index1, index2+1, memDict) # Add 1 to index2 because we know there is a character we need to delete at index2 itself
            insertOp = 1 + findMinStringOpsTD(s1, s2, index1+1, index2, memDict) # Add 1 to index1 because we know there is a character in s1 that is missing from s2
            replaceOp = 1 + findMinStringOpsTD(s1, s2, index1+1, index2+1, memDict) # We're just doing a replace, so we increment each index by 1 to move on
            memDict[dictkey] = min(deleteOp, insertOp, replaceOp)

        return memDict[dictkey]

print(findMinStringOpsTD("table", "tbrltt", 0, 0, {}))

# Bottom Up
def findMinOperationBU(s1, s2, tempDict):
    # Populate the dictionary with a key for every character in both the strings
    for i1 in range(len(s1)+1):
        dictKey = str(i1)+'0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2)+1):
        dictKey = '0'+str(i2)
        tempDict[dictKey] = i2
    
    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dictKey = str(i1)+str(i2)
                dictKey1 = str(i1-1)+str(i2-1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1)+str(i2)
                dictKeyD = str(i1-1)+str(i2)
                dictKeyI = str(i1)+str(i2-1)
                dictKeyR = str(i1-1)+str(i2-1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI],tempDict[dictKeyR]))
    dictKey = str(len(s1))+str(len(s2))
    return tempDict[dictKey]
    