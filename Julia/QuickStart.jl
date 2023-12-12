# Print
println("Hello world")

# Get the type of an object
my_int = 42
my_str = "Hello world"
typeof(my_int)
typeof(my_str)

# Arithmatic operations
sum = 3 + 7
difference = 10 - 3
product = 20 * 5
quotient_1 = 100 / 10
quotient_2 = 100.0 / 10
quotient_3 = 100 / 10.0
quotient_4 = 100 / 3
power = 10 ^ 2
mod = 101 % 2
println(sum)
println(difference)
println(product)
println(quotient_1)
println(quotient_2)
println(quotient_3)
println(quotient_4)
println(power)
println(mod)

# Can insert variables into strings like in PHP
this_int = 10
this_str = "variable"
println("inserting this integer: $this_int, and this string: $this_str, like in PHP")

# string() function can be used for conversion and concatenation
str_1 = "This is part 1 and..."
str_2 = "this is part 2."
concat = string(str_1, str_2)
convert = string(100)
println(concat)
println(convert)

# Can also concatenate like:
println(str_1*str_2)
println("$str_1$str_2")