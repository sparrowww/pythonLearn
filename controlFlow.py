#!/usr/bin/env python3

myBool = False  # True
print(myBool)
print(2 == 2)

var1 = 11
var2 = 42
if var1 == var2:
    print("var1 == var2. var = " + str(var1))
if var1 > var2:
    print("var1 > var2. var1 = " + str(var1) + ", var2 = " + str(var2))
if var1 < var2:
    print("var1 < var2. var1 = " + str(var1) + ", var2 = " + str(var2))

if var1 > 0:
    print("var1 > 0")
    if var1 > 10:
        print("var1 > 10")
        if var1 > 100:
            print("var1 > 100")

if myBool:
    print("myBool is True!")
else:
    print("myBool is False!")

if var2 < 0:
    print("var2 < 0! var2 = " + str(var2))
elif var2 == 0:
    print("var2 == 0! var2 = " + str(var2))
else:
    print("var2 > 0! var2 = " + str(var2))

itr = 0
while itr < 10:
    itr += 1
    if itr < 5:
        continue
    print("itr = " + str(itr))

itr2 = 0
while True:
    itr2 += 1
    if itr2 > 10:
        break



