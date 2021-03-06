#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
<<<<<<< HEAD
import string as s # for removing punctuation
=======
>>>>>>> origin/master

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
<<<<<<< HEAD
def get_dict(filename):
    f = open(filename, 'rU')
    d = {}
    """
    this code needs to be changed because...
    it gets the words but also keeps the punctuations tacked on
    must remove punc.
    """
    for line in f:
        line = line.lower()
        for ch in s.punctuation:
            if ch in line:
                line = line.replace(ch, '')
=======
def readfile(filename):
    f = open(filename, 'rU')
    d = {}
    return f, d

def print_words(filename):
    [f, d] = readfile(filename)
    for line in f:
        line = line.lower()
>>>>>>> origin/master
        l =line.split() # changed, read line 29
        for i in range(len(l)):
            if l[i] in d:
                d[l[i]] += 1
            else:
                d[l[i]] = 1
<<<<<<< HEAD
    return d

def print_words(filename):
    d = get_dict(filename)
    sorted_keys = sorted(d) # list of keys
    d_list = [] # representative sorted list
    counter = 0
    for key in sorted_keys:
        entry = d[key]
        d_list.append([key, entry])
        counter += 1
=======
    sorted_keys = sorted(d) # list of keys
    """
    d_sorted is not a dictionary
    cannot use dict methods on d
    need to fix this!!!

    UPD1: should use a sorted representation, a dictionary doesn't get sorted
    ie, a list of lists/tuples

    UPD2: updated to created sorted list representing dictionary
    realized error in sorting, must be sorted by entries, not keys
    --can be sorted later in process
    """
    d_list = [] # representative sorted list
    counter = 0
        for key in sorted_keys:
            entry = d[key]
            d_list.append([key, entry])
            counter += 1


>>>>>>> origin/master

    # this also needs to be fixed
    for key, entry in d_list:
        print(key,'\t', entry)
    return d_list



def print_top(filename):
<<<<<<< HEAD
    d = get_dict(filename)
    l = []
    """
    works well, something wrong
    prints more than just the top 20, also list in lowest count to highest
    """

    for word, count in d.items():
        l.append([word, count])
    ls = sorted(l, key = sort2, reverse = True)
    for i in range(20):
        print(ls[i][0], '\t', ls[i][1])
    return ls
=======
    [f, d] = readfile(filename)
    for line in f:
        line = line.lower()
        l =line.split(' ')
        for i in range(len(l)):
            if l[i] in d:
                d[l[i]] += 1
            else:
                d[l[i]] = 1
    l = []
    for word, count in d.items():
        l.append([word, count])
    ls = sorted(l, key = sort2)
    for i in ls:
        print(ls[i][0], '\t', ls[i][1])

print('function created', '[2]')
>>>>>>> origin/master

def sort2(x):
    return x[1]




###
<<<<<<< HEAD
# the following must be called in cmd as:
# python wordcount {--count or --topcount} file
=======
# print('hello')
# print('values', sys.argv)
# stored_value = sys.argv
>>>>>>> origin/master

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3: # looks at the length of arguments passed
    print ('usage: ./wordcount.py {--count | --topcount} file') # tells you what arguments to pass
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print( 'unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
