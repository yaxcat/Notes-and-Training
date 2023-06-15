# Exercise 1.

# Write a recursive function to find the sum of digits for a positive integer number
# Input: 123
# Output: 6
#___________________________________________________________________________________________________________________

def sum_digits(n):
    assert n > 0 and int(n) == n, "The number must be a positive integer."
    if n < 10:
        print("Base Case:", "n:", n)
        return n
    else:
        print("n:", n, "Integer:", (n//10), "Remainder:", int(n%10))
        return int(n%10) + (sum_digits(n//10))
#print(sum_digits(1283))


# Exercise 2.
# Write a recursive function to calculate the power of a number
#___________________________________________________________________________________________________________________

def power(base, exp):
    assert int(exp) == exp, "The exponent must be integer only"
    if exp < 1:
        return 1
    else:
        return base * power(base, exp -1)



# Exercise 3.
# Write a recursive function to find the greatest common divisor (GCD) of two integer numbers.
#___________________________________________________________________________________________________________________

# Use the Euclidean algorithm, which divides the larger number by the smaller number, and then the smaller by the 
# remainder and so on until until a divisor which yeilds a remainder of zero is found.  For instance:
# Factor = 48
# Divisor = 18
# Greatest Common Divisor(48, 18) ->
#   1. 48/18 =  2, remainder 12,
#   2. 18/12 =  1, remainder 6,
#   3. 12/6  =  2, remainder 0
#   Solution = 6


def euclidean_gcd(n, m):
    assert int(n) == n and int(m) == m, "The numbers must be integers" 
    assert n > 0 and m > 0, "The numbers must be greater than zero"
    if n % m == 0:
        print("n:", n, "m:", m)
        return m
    else:
        print("n:", n, "m:", m)
        return euclidean_gcd(m, n % m) # In order to get the desired behavior, we need to swap the position of the n & m parameters in the recursive function call
print(euclidean_gcd(48, 18))


# Exercise 4.
# Convert a number from decimal to binary using recursion 
# Input: 10
# Output: 1010
#___________________________________________________________________________________________________________________

# Use a process similar to the Euclidean algorithm. Divide the input number by 2, then keep dividing the quotient
# by 2 until it is zero
# 
# Decimal to Binary (10) ->
#   1. 10/2 -> Quotient = 5, Remainder = 0
#   2. 5/2  -> Quotient = 2, Remainder = 1
#   3. 2/2  -> Quotient = 1, Remainder = 0
#   4. 1/2  -> Quotient = 0, Remainder = 1

def decimal_to_binary(num, binary_result=""):
    assert int(n) == n, "The parameter must be an integer"
    if num == 0:
        return binary_result
    else:
        print("Quotient:", num, "Remainder:", num % 2)
        return decimal_to_binary(num//2, str(num % 2) + binary_result)

print(decimal_to_binary(57.8))