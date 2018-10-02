print("Hello World!")
x = "hello Dojo!"
print(x)
y = 42

x = "hello "*50
print(x)
print("Dojo"*50+"coding"*100)

list = [3,5,1,2]
for i in list:
    print(i)

# This was boned up
# list = [3,5,1,2]
# for i in range(list):
#     print(i)

list = [3,5,1,2]
for i in range(len(list)):
    print(i)

# Basic
for i in range(151):
    print(i)

# Multiples of Five
# i = 2
# while i*5 <= 1000001:
#     print(i*5)
#     i+=1

# Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print ('coding ' + 'dojo')
    elif i % 5 == 0:
        print ('coding')
    else:
        print (i)

# Whoa. That Sucker's Huge
huge_sucker = 0
for i in range(1,500000,2):
    huge_sucker += i
print(huge_sucker)

#v2
x = 0
for i in range(0,500001):
   if i % 2 != 0:
       x=x+i
print(x)

# Countdown by Fours
for i in range(2018,1,-4):
    print(i)

# Flexible Countdown
def flexible_countdown(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if (i % mult == 0):
            print(i)

flexible_countdown(2,9,3)
