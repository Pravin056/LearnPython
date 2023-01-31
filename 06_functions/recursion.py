# def abc():
#     print("Recursive")
#     abc()
#     #RecursionError: maximum recursion depth exceeded while calling a Python object
# abc()

#Always use condition with recursive function call

def facto(x):
    '''
    This is a recursive function to find the factorial of an integer
    :param x:
    :return:
    '''

    if x == 1:
        return 1     #this is the end of query
    else:
        return(x * facto(x-1))

    # return(5 * facto(5-1)) ---- 5 * 4
    # return(4 * facto(4-1)) ---- 5 * 4 * 3
    # return(3 * facto(3-1)) ---- 5 * 4 * 3 * 2
    # return(2 * facto(2-1)) ---- 5 * 4 * 3 * 2 * 1 = 120

print(facto(5))