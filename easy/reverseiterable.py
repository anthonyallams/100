'''
CHALLENGE: REVERSE AN ITERABLE
Given an iterable value, reverse it
NB: Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have __next__() method, which returns the next item of the object

EXAMPLE
Given the following iterables, you will get
reverse('solution') => noitulos
reverse([1,2,3,4]) => [4,3,2,1]
reverse((1,2,3,4)) => (4,3,2,1)
reverse({1:'apple', 2:'orange', 3:'banana', 4:'mango'})=> 
        {'apple': 1, 'banana': 3, 'mango': 4, 'orange': 2}
'''


def reverse_iterable(input):  # O(n)
    # Check if input is a dict and reverse
    # Check if input is a str, tuple, set or list and reverse it
    # Use try except statement to handle TypeError if a non-iterable is entered as iput
    try:
        if type(input) == dict:
            return {value: key for key, value in input.items()}
        elif type(input) == str or list or tuple or set:
            return input[::-1]
        else:
            return
    except TypeError:
        print(f'{input} is not an iterable. Try again')

