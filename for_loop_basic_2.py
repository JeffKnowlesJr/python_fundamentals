# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggieSize(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    print(arr)
    return(arr)
biggieSize([2,6,1,3,45,6,-22,-100])

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPositives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
        if i == len(arr) - 1:
            arr[i] = count
            print(arr)
            return arr
countPositives([-1,5,3,-5])

def countPositives(arr):
    count = 0
    for val in arr:
        if val > 0:
            count += 1
# special python reverse index
    arr[-1] = count
    print(arr)
    return arr
countPositives([-1,5,3,-5])

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum)
    return sum
sumTotal([-1,5,3,-5])

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def average(arr):
    total = arr[0]
    for i in range(1, len(arr)):
        total += arr[i]
    print(total / len(arr))
    return total / len(arr)
average([1,2,3,4])

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr):
    print(len(arr))
    return len(arr)
length([1,2,3,4])

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    val = arr[0]
    if len(arr) == 0:
        return false
    else:
        for i in range(len(arr)):
            if arr[i] < val:
                val = arr[i]
    print(val)
    return val
minimum([-1,-2,-8,-3])

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    val = arr[0]
    if len(arr) == 0:
        return false
    else:
        for i in range(len(arr)):
            if arr[i] > val:
                val = arr[i]
    print(val)
    return val
maximum([-1,-2,-8,-3])

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultimateAnalyze(arr):
    anals = {"sumTotal": arr[0], "average": arr[0], "minimum": arr[0], "maximum": arr[0]}
    for i in range(1,len(arr)):
        if arr[i] < anals["minimum"]:
            anals["minimum"] = arr[i]
        elif arr[i] > anals["maximum"]:
            anals["maximum"] = arr[i]
        anals["sumTotal"] += arr[i]
        anals["average"] += arr[i]
    anals["average"] = anals["average"] / len(arr)
    print(anals)
    return anals
ultimateAnalyze([1,6,3,2,5,7,8,9,2,23])

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverseList(arr):
    for i in range(int(len(arr)//2)):
# FOBO - Fear of OFF BY ONE
        temp = arr[i]
        arr[i] = arr[-1-i]
        arr[-1-i] = temp
    print(arr)
# Can be done with a hot swap and no temp VAR
reverseList([1,5,7,3])
