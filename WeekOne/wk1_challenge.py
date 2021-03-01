"""
1. Write a variable called "name" and set it equal to your name
    and print it out in the terminal
2. Write a for loop that prints out numbers -1 through -10
3. Write a while loop that prints out numbers -1 through -10
4. Define a function called "hello" which prints "hello world"
    and call the function so it shows in the terminal output
5. Define a function "sum" which takes two parameters(x,y)
     write a variable "z" in the function which calculates the sum
     inside the function and returns "z". Set a variable equal to the
     function call and print that variable output
    ** There should not be print statement in the function **
6. Print out all odd numbers from 1 - 100 using the modulo operator
7. * optional, but highly recommended challenge*
    Write an algorithm to detect prime numbers func name isPrime()
    prime number is the one that is only divisible by 1 and itself
"""

# Solutions

# 1.

name = 'Maximo Mugisha'
print(name)

# 2.

for i in range(1, 11):
    print(0 - i)

# 3.

n = -1
while n >= -10:
    print(n)
    n -= 1


# 4

def hello():
    print('Hello World')


hello()


# 5

def Sum(x, y):  # func name shouldn't be camelcase, but this is how it was specified in the question
    z = x + y
    return z


add = Sum(4, 5)
print(add)

# 6.

for o in range(1, 100):
    if o % 2 != 0:
        print(o)


# 7.

def isPrime():  # func name shouldn't be camelcase, but this is how it was specified in the question
    """
    A function to detect whether the input number is a prime
    """
    num = int(input('Enter any number: '))
    # This next line is cause prime numbers must be greater than one
    if num > 1:
        for k in range(2, num):
            if (num % k) == 0:
                print(num, 'is not a prime number')
                # I use num // i to use the floor number to avoid decimal points in respose
                # and to return at least its other two multiples
                print(k, 'times', num // k, 'is', num)
                # I use break statement in order to leave the loop 
                # and execute the next line since there could be other numbers of i to compare against.
                # one is enough! to disqualify it from being prime 
                break
        else:
            print(num, 'is a prime number')
    else:
        print(num, 'is not a prime number')


isPrime()

# References
# https://www.javatpoint.com/python-check-prime-number
# https://www.programiz.com/python-programming/break-continue#:~:text=Python%20break%20statement,will%20terminate%20the%20innermost%20loop.

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(str(num) + " is not prime")
                return True
        print(str(num) + " is prime")
    else:
        print(str(num) + " is not prime")
        return False
is_prime(7)

#use return so that the data can be further reused. for example this functions
#  returns a boolean data type .. it can be used to know that the entered number 
# is prime or not