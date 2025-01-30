# Greed Algorithms

# Defined by a few properties:
# 1) Builds the solution piece by piece
# 2) At each step of the algorithm, it chooses the solution which offers the most obvious and immediate benefit
# 3) When combined, each locally opimum solution adds up to the globally optimum solution

# Examples:
    # - Insertion sort
    # - Selection sort
    # - Topological sort
    # - Prims algorithm
    # - Kruskal's algorithm
    # - Activity selection problem
    # - Coin change problem
    # - Fractional knapsack problem

# ACTIVITY SELECTION
# -----------------------
# Given N number of activities with their start and end times, select the maximum
# number of activities that can be performed by a single person, assuming that a
# person can only work on one activity at a time.

# It is a greedy algorithm because at each step, we choose the best activity at that
# step and freeze it (never come back to it again).  In the end, these local choices
# add up to the global optimum, hence its greediness.

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
              ]
# TC: O(NlogN) due to the sort
# SC: O(1)
# Algorithm is simple.  Key thing is to sort by end time
def getMaxActivities(activities):
    activities.sort(key=lambda x: x[2]) # Since this is a 2D array, we need to use a lambda fn. Sort rows by 3 element in row

    i = 0 # Leading activity
    first_activity = activities[i][0]
    print(first_activity)
    for j in range(len(activities)): # Loop through the activities and compare the start/end times
        if activities[j][1] > activities[i][2]: # If the trailing activity's start time is greater than the leading activies end time, we can do it
            print(activities[j][0])
            i = j # Update the leading activity pointer since we're iterating through the list
# getMaxActivities(activities)


# COIN CHANGE PROBLEM
# -----------------------
# Given a coins of different denominations and a total amount of money, find the
# minimum number of coins you need to make up the given amount.

# It is a greedy algorithm because we select the best (biggest) applicable coin
# at each step.  The best coin is one that is as large as it can be without being
# bigger than the total amount of money we've yet to divy up.  At the end we add
# all the coins (locally best solutions) up to form the globally best solution

# TC: O(n) iterating over every list element
# SC: O(1)
coins = [1,2,5,20,50,100]
total = 201
def coinChange(amount, coins):
    remaining = amount
    coins.sort()
    index = len(coins)-1 # Start with largest coin
    while True: # Just run the loop until we break out of it
        coin_value = coins[index] # Work our way from the largest coin to the smallest one
        if remaining >= coin_value:
            print(coin_value)
            remaining -= coin_value
        if remaining < coin_value:
            index -= 1 # Only decrement index if we don't have enough remaining. This ensures we pick the largest valid coin

        if remaining == 0:
            break
# coinChange(total, coins)


# FRACTIONAL KNAPSACK PROBLEM
# -----------------------
# TC: O(ONLogN)
# SC: O(1)

# Given a set of items, each with a unique weight and value, determine the number of
# each item to include in a collection (knapsack, box, etc.) such that the total weight 
# is less than or equal to a given limit and also that the total value is as high as
# possible.

# Combinatorial optimization problem. Find the object value density is key to solving
# the problem.

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsackSolver(items, capacity):
    items.sort(key=lambda x : x.ratio, reverse=True) # Sort the items list by value density property, greatest to least
    used_capacity = 0
    total_value = 0
    for item in items:
        # If a whole item will fit in our knapsack, add it and update variables
        if used_capacity + item.weight <= capacity:
            used_capacity += item.weight
            total_value += item.value
        # If we can't fit the whole item, find the amount that will fit and put that in the knapsack
        else:
            unused_weight = capacity - used_capacity
            value = item.ratio * unused_weight
            used_capacity += unused_weight
            total_value += value

        if used_capacity == capacity:
            break
    print("Total Value: ", total_value)        
    
i1 = Item(20, 100)
i2 = Item(30, 120)
i3 = Item(10, 60)
my_list = [i1, i2, i3]
knapsackSolver(my_list, 50)