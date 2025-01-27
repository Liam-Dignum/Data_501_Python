from numpy.core.defchararray import lower
from pandas import factorize

print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def returnDivisors(num:int):
    outputlist = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            outputlist.append(i)
    return outputlist
print(returnDivisors(10))



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def isFactor(num1,num2):
    num1Factors = returnDivisors((num1))
    num2Factors = returnDivisors(num2)
    if num2 in num1Factors or num1 in num2Factors:
        return True
    else:
        return False

print(isFactor(5,10))





# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def positionInAlp(input:str):
    return alphabet.index(lower(input))

print(positionInAlp(input('Enter a letter\n')))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def idNum(Name:str):
    id =''
    for char in Name:
        id+= str(positionInAlp(char))
    return id

print(idNum(input('Enter a Name\n')))




print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password(Name):
    id = int(idNum(Name))
    for char in Name:
        id -= int(positionInAlp(char))
    return id


print(password(input('Enter a Name\n')))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def checkIfPrime(input:str):
    try:
        num = int(input)
        if num > 1:

            # Iterate from 2 to n // 2
            for i in range(2, (num // 2) + 1):

                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    return "is not a prime number"
            else:
                return "is a prime number"
        else:
            return "is not a prime number"
    except:
        return 'Invalid input enter a number'
print(checkIfPrime(input('Enter a Number\n')))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

print(checkIfPrime(input('Enter a Number\n')))

# -------------------------------------------------------------------------------------- #






