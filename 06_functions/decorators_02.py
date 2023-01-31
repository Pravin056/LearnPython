#without decoration
#
# def student(func):
#     def inner(name):
#         if name == "srujan":
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


def col(func):
    def inner(name):
        if name == "red":
            print("its RED")
        else:
            func(name)
    return inner


@col
def col2(name):
    print(name,"hhhhh")

col2("RED")