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


# Dictionaries
# To define a dictionary:
phonebook = Dict(
    "Jenny" => "867-5309",
    "Ghostbusters" => "555-2368"
    )

println("")
println("")

# To add an element:
phonebook["Kramer"] = "555-FILK"
phonebook

println("")
println("")

# To delete and return an element
myitem = pop!(phonebook, "Kramer")
println(myitem)
phonebook

# Tuples
# To create a tuple:
my_tuple = ("a", "b", "c")
# Indexing starts at 1 in Julia
my_tuple[1]

# Arrays
myarray = [1,2,3,4,5,6,7, "a"]
# use push!() and pop!() functions to add and remove elements
push!(myarray, "ZZZ")
myarray
pop!(myarray)
myarray


# Loops

# While Loop
function countup(i)
    while i < 10
        i += 1
        println(i)
    end
end
countup(0)

# For Loop
for element in myarray
    println(element)
end

for n = 1:10
    println(n)
end


# Conditionals

x = 0
y = 0

if x > y
    println("$x is larger than $y")
elseif y > x
    println("$y is larger than $x")
else
    println("$x and $y are equal")
end

# This statement
if x > y
    x
else
    y
end

# Could be rewritten as:
(x > y) ? x : y

# functions
# use the '!' to notate that a function returns a modified/mutated version of the input
# functions can be defined like:
function sayhi(name)
    println("Hi $name, its great to see you!")
end

sayhi("Mike")

# can also define like this:
sayhi2(name) = println("Hi $name, its great to see you!")

# can also declare an anonymous function:
myvar = name -> println("Hi $name, its great to see you!")
myvar("Chewbacca")

