# The problem "FizzBuzz" is a classic example often used in coding interviews to assess basic programming 
# abilities. Given a positive integer n, the task is to construct an array of strings that follow a 
# specific pattern based on whether the index of the array (starting from 1) is divisible by 3, 5, or both:

# For each index 'i' that is divisible by both 3 and 5 (for example, 15, 30, 45), the array should contain 
# the string "FizzBuzz" at that index.
# If the index 'i' is only divisible by 3 (like 3, 6, 9), the array should have "Fizz" at that index.
# If the index 'i' is only divisible by 5 (such as 5, 10, 20), the string "Buzz" should appear at that 
# index.
# For all other indexes that don't meet the above divisibility conditions, the array should store the index
#  'i' itself as a string.
# The function should return the array, which is described as answer, and it should be 1-indexed, 
# meaning the first element corresponds to i=1.

def fizzbuzz(arrLen):
    answer = [''] * arrLen
    for i in range(1, arrLen + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer[i-1] = "FizzBuzz"
        elif i % 3 == 0:
            answer[i-1] = "Fizz"
        elif i % 5 == 0:
            answer[i-1] = "Buzz"
        else:
            answer[i-1] = str(i)
    
    return answer
#print(fizzbuzz(15))

# Return to robot origin

# This LeetCode problem involves determining whether a robot, which starts at the origin (0, 0) on a 2D 
# plane, returns to its starting point after executing a series of moves. The series of moves is given as 
# a string where each character corresponds to a move in one of four possible directions: 'R' (right), 'L' 
# (left), 'U' (up), and 'D' (down). The task is to analyze this string and return true if the robot ends 
# up at the origin after all the moves or false otherwise. The key point is to keep track of the robot's 
# position relative to the origin, regardless of how it's facing, and verify if it returns to (0, 0).

def robotReturn(moveSequence):
    mSSafe = moveSequence.upper()
    directions = set(mSSafe)
    moves = {}
    for d in directions:
        moves[d] = mSSafe.count(d)
    if moves["R"] == moves["L"] and moves["U"] == moves["D"]:
        return True
    else:
        return False

print(robotReturn("RRUDLLL"))