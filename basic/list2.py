#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  prev = 0
  x = []
  for val in nums:
      if val != prev:
          x.append(val)
          prev = val
  return x


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    x = []
    j = 0
    total_l = len(list1) + len(list2)
    # print(list1)
    # print('ENTER FXN')
    for item1 in list1:
        # print("item1: ", item1, '\t', "j: " ,j, 'max: ', str(len(list2)))
        # print()
        while j < len(list2) and item1 >= list2[j]:
            # print('while loop')
            # print(list2[j], "\t1\t", str(item1))
            x.append(list2[j])
            j += 1
            # print('j incremented')
        # print('exit loop', 'item1: ', item1)
        x.append(item1)
        # print('x: ', x)

# the following line addresses a problem previously missed:
# what if the item in list 2 is greater than the item in list 1,
# AND len(l2) > len(l1)

    if len(x) < total_l:
        rem = total_l - len(x)
        rem_ind = rem * -1
        x += list2[rem_ind:]
    return x

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print( '%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print( 'remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print( 'linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
