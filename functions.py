#!/usr/bin/env python3

list1 = [1, 4, 8]
print(list1)
list1.append(42)
list1.insert(0, 11)
print(list1)
print(list1.index(42))

str1 = "alex"
str2 = "Name is {1}{2}{3}{0}".format(str1[0], str1[1], str1[2], str1[3])
print(str2)

str3 = "Word is {C}{F}{K}{U}".format(U="K", C="F", F="U", K="C")
print(str3)

str4 = "*".join(["q", "w", "e"])
print(str4)
str4List = str4.split("*")
print(str4List)


def my_func(var):
    """
    :param var: input
    :return: result
    """
    print("myFunc. var = ", var)
    return len(str(var))


lenVar = my_func("232EEW34")
print(lenVar)
lenVar = my_func(12313)
print(lenVar)


