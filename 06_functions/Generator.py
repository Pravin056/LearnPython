'''
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
Generators are useful when we want to produce a large sequence of values,
but we don't want to store all of them in memory at once.

generator creates own iterator

Iterator                                vs      Generator
01. iterator keyword : return                   01. Generator keyword : yield
02. iterator returns single value               02. Generator returns multiple value by iterator index/count
03. Class is used to implement an iterator      03. Function is used to implement a generator.
04. Local Variables aren’t used here.           04. All the local variables before the yield function are stored.
05. Iterators are used mostly to iterate or     05. Generators are mostly used in loops to generate an iterator
    convert other objects to an iterator            by returning all the values in the loop without affecting the
    using iter() function.                          iteration of the loop
06. Iterator uses iter() and next() functions   06. Generator uses yield keyword
07. Every iterator is not a generator           07. Every generator is an iterator


'''

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)