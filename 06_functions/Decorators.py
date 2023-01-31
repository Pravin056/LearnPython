'''
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour
of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of
the wrapped function, without permanently modifying it.
'''

#without decorator
import time
# def calc_square(numbers):
#     start = time.time()
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     end = time.time()
#     print("cal_square took" + str((end-start)*1000) + "mil sec")
#     return result
#
# def calc_cube(numbers):
#     start = time.time()
#     result =[]
#     for number in numbers:
#         result.append(number*number*number)
#     end = time.time()
#     print("cal_cube took" + str((end-start)*1000) + "mil sec")
#     return result
#
# array = range(1,100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)



#with decorator
# def time_it(func):
#     def wrapper(*arg, **kwargs):
#         start = time.time()
#         result = func(*arg, **kwargs)
#         end = time.time()
#         print(func.__name__+"took"+str((end - start)*1000) + "mil sec")   # __name__ call magical function
#         return result
#     return wrapper
#
# @time_it
# def calc_square(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     return result
#
# @time_it
# def calc_cube(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     return result
#
# array = range(1,100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)


#without decoration
#
# def student(func):
#     def inner(name):
#         if name == "srujana":
#             print("you are late")
#         else:
#             func(name)
#     return inner
#
#
# @student
# def alter(name):
#     print("hello", name, "you are on time")
#
#
# alter("srujan")
# alter("deepika")


# def student(func):
#     def inner(name):
#         if name == 6:
#             print("you are late")
#         else:
#             func(name)
#     return inner
#
#
# @student
# def alter(name):
#     print("hello", name, "you are on time")
#
#
# alter(6)
# alter("deepika")


def student(func):
    def inner(name):
        if name == 9:
            print("right answer")
        else:
            func(name)
    return inner


@student
def alter(name):
    print("hello", name, "you are on time")


alter(3*3)
alter("deepika")