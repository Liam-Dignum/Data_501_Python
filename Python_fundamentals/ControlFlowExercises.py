print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
i = 0
while i < 5:
    print(x[i])
    i+=1





print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in x:
    if i % 2 == 0:
        print(i)




print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
i=0
while i < 5:
    if i % 2 == 0:
        print(x[i])
    i += 1
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
firstinitallist = []
for name in names:
    print(name[0])
    firstinitallist.append(name[0])




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
indexlist = []
for name in names:
    print(name.index(' '))
    indexlist.append(name.index(' '))



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initialslist = []
for name in names:
    print(name[0], ' ', name[name.index(' ')+1])
    initialslist.append(name[0] + ' ' + name[name.index(' ')+1])


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for list in list_of_lists:
    if len(list) == len(set(list)):
        print(list)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
complete = 0
while complete == 0:
    try:
        inputnum =int(input('Enter a number above 100\n'))
    except:
        print('Not a number')
        continue
    if inputnum > 100:
        print(inputnum)
        complete +=1
    else:
        print('Number not above 100 try again')



print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
def checkIfPrime(num:int):
    if num > 1:

        # Iterate from 2 to n // 2
        for i in range(2, (num // 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
complete = 0
while complete == 0:
    try:
        inputnum =int(input('Enter a number above 100\n'))
    except:
        print('Not a number')
        continue
    checkIfPrime(inputnum)
    if inputnum > 100:
        print(inputnum)
        complete +=1
    else:
        print('Number not above 100 try again')





