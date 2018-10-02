"""
max(sequence) returns the largest value in the sequence
sum(sequence) return the sum of all values in sequence
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence
Built-in Functions and Methods for Dictionaries
Python includes the following standalone functions for dictionaries:

len() - give the total length of the dictionary.
str() - produces a string representation of a dictionary.
type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.
Python includes the following dictionary methods (either dict.method(yourDictionary) or yourDictionary.method() will work):

.clear() - removes all elements from the dictionary
.copy() - returns a shallow copy dictionary
.fromkeys(sequence, [value]) - create a new dictionary with keys from sequence and values set to value.
.get(key, default=None) - for key key, returns value or default if key is not in dictionary.
.items() - returns a view object of dictionary's (key, value) tuple pairs.
.keys() - return a view object of dictionary keys.
.pop(key) - returns the value associated with the key and removes the key-value pair from the dictionary.
.setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
.update(dict2) - adds dictionary dict2's key-values pairs to an existing dictionary.
.values() - returns a view object of dictionary values.
"""
print("max()", max([1,65,2]))
print("sum()", sum([1,65,2]))
