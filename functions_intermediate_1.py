"""
# Create beCheerful().  Within it, print string "good morning!" 98 times.
print("*"*80)
def beCheerful(name='', repeat=1):
	print(f"good morning {name}\n"*repeat)
beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")
# helpful tips for the next assignment
import random
print(random.random()) # returns a random floating number between 0.000 to 1.000
print(random.random()*50) # returns a float between 0.000 to 50.000
int( 3.654 ) # returns 3
round( 3.654 ) # returns 4

As part of this assignment, please create a function randInt() where

randInt() returns a random integer between 0 to 100
randInt(max=50) returns a random integer between 0 to 50
randInt(min=50) returns a random integer between 50 to 100
randInt(min=50, max=500) returns a random integer between 50 and 500
Create this function without using random.randInt() but you are allowed to use random.random().
"""

def randInt():
    import random
    rand = round(random.random()*100)
    print("\nRandom 1 - 100:")
    return rand
print(randInt())

def randInt(max):
    import random
    rand = round(random.random()*max)
    print("Random 1 -", max, ":")
    return rand
print(randInt(max=50))

def randInt(min):
    import random
    rand = round(random.random()*min + min)
    print("Random ", min, " - ", 2*min, ":")
    return rand
print(randInt(min=50))

def randInt(min, max):
    import random
    rand = round(random.uniform(min, max))
    print("Random ", min, " -", max, ":")
    return rand
print(randInt(min=50, max=500))
