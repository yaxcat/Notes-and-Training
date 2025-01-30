# RECURSION

# Recursive functions call themselves to solve a problem.  Recursion has a few properties
#   1. Performs the same operation multiple times using different inputs
#   2. At every step, the function uses smaller inputs to make the problem smaller
#   3. Base condition is needed to stop the recursion, otherwise an infinite loop is bound to occur

# Need:
#   1. Recursive thinking is important to and commonplace in programming because it allows the programmer to break
#      down big problems into smaller ones, which are easier to solve 
#   2. Traversal of trees and graphs
#   3. Interviews
#   4. Used in many algorithms (divide and conquer, greed and dynamic programming)

# Recursive techniques can commonly be used for problems with the following phrases:
#   - Design an algorthim to compute nth...
#   - Write code to list the n...
#   - Implement a method to compute all...

#___________________________________________________________________________________________________________________
# Under the hood:
#   Recursive functions are evaluated by the system and instances of the function are stored in the call stack and
#   executed in LIFO order. There are push and pop methods for the call stack, just like there are for DIY stacks.
#   If we pass 5 into the example below, the call stack actually looks like:
#       5.  recursiveExample(1) - Executed first
#       4.  recursiveExample(2) - Executed second
#       3.  recursiveExample(3) - Executed third
#       2.  recursiveExample(4) - Executed fourth
#       1.  recursiveExample(5) - Executed fifth
#
# Note that the execution order is opposite what you would expect, given the way the function prints out.  Execution
# 'bottom-up, not 'top-down'
#___________________________________________________________________________________________________________________

def recursiveExample(n):
    if n < 1:
        print("n < 1, terminating recursion")
    else:
        print(n)
        recursiveExample(n-1)

#recursiveExample(5)

# Iteration is both more space and time efficient than recursion, but recursive code is easier to write, especially
# for some data structures.

# Iterative function termination is governed by a control variable, whereas recursive function termination is 
# governed by an if condition



def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

#print(powerOfTwo(5))

# Factorial function:
def factorial(n):
    # Allows us to throw an exception if a negative number is a supplied
    assert n >= 0 and int(n) == n, 'The number must be a positive integer.'
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(10))


# Fibonacci Sequence:
def fib(n):
    assert n >= 0 and int(n) == n, "Fibonacci number cannot be negative number or non integer."
    end = [0, 1] # Fibonacci sequence terminates in 0 or 1
    if n in end:
        return n
    else:
        return fib(n-1) + fib(n-2) # Start from n and work backwards towards the base case


print(fib(7))