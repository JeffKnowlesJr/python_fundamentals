# Countdown
def countdown(x):
    arr = []
    for i in range(x,-1,-1):
        arr.append(i)
    print(arr)
countdown(5)

# Print and Return
def printAndReturn(x):
    print(x.pop(0))
    return x[0]
print(printAndReturn([1,2]))

def printAndReturn2(x):
    print(x[0])
    return x[1]
print(printAndReturn([1,2]))

# First Plus Length
def firstPlusLength(x):
    return x[0] + len(x)
print(firstPlusLength([1,2,3,4,5,6,7]))

# This Length, That Value
def lengthAndValue(value,size):
    newlist = []
    for i in range(1,size):
        newlist.append(value)
    return newlist
print(lengthAndValue(5,19))

def lengthAndValue(value,size):
    newlist = []
    for i in range(1,size):
        newlist.insert(0,value)
    return newlist
print(lengthAndValue(5,19))

def valuesGreaterThanSecond(arr):
    if (len(arr) < 2):
        return false
    else:
        newlist = []
        for i in range(2, len(arr)):
            if (arr[i] > arr[1]):
                newlist.append(arr[i])
    print(len(newlist))
    return newlist
print(valuesGreaterThanSecond([2,1,6,8,9,3]))
