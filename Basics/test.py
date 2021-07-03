import random


def testFunc():
    global x
    x = "Python!"


# testFunc()
# print(x)

# For a specified number, prints that number of random values between 1 and 100
def randomNumberPrinter(length):
    count = 0
    for i in range(length):
        count += 1
        i = random.randrange(0, 100)
        print("Random Number", str(count) + ":", str(i))


# randomNumberPrinter(100)

""" x = 5

y = 5

if x == y:
    print("Woah")
else:
    print("Yikes")
 """

# print("HELLO WORLD")
