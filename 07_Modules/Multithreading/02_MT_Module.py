'''
In Python, the threading module provides a very simple and intuitive API for spawning multiple threads in a program.
Let us consider a simple example using a threading module:
'''
# Python program to illustrate the concept
# of threading
# importing the threading module
import threading #import the threading module


def print_cube(num):
    # function to print cube of given num
    print("Cube: {}".format(num * num * num))


def print_square(num):
    # function to print square of given num
    print("Square: {}".format(num * num))

'''
To create a new thread, we create an object of Thread class. It takes following arguments:
target: the function to be executed by thread
args: the arguments to be passed to the target function
To start a thread, we use start method of Thread class.
'''
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    '''
    Once the threads start, the current program (you can think of it like a main thread) also keeps on executing.
    In order to stop execution of current program until a thread is complete, we use join method.
    '''
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    '''
    As a result, the current program will first wait for the completion of t1 and then t2.
    Once, they are finished, the remaining statements of current program are executed.
    '''
    # both threads completely executed
    print("Done!")

    #check image : threading_module_process.png