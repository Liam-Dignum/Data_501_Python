print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions


def square(n):
    return n*n


def percentage(n):
    return n/100


def multiplier(n, m):
    return n*m


def addition(a, b, c):
    return a + b + c

# A1a:

squareLam = lambda x: x*x

print(squareLam(5))

percentageLam = lambda x: x/100

print(percentageLam(50))

multiplierLam = lambda x,y: x*y

print(multiplierLam(5,29))

additionLam = lambda x,y,z: x+y+z

print(additionLam(3,6,10))



print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1

# A1b:
# takes input num a and returns the product of all whole positive numbers, a*((a-1)*((a-1)-1) while a is greater than 1


print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

# A1c:

print(list(map(squareLam,list_of_numbers)))

# -------------------------------------------------------------------------------------- #