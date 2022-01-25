#!/usr/bin/env python3

strArr = ["a", "b", "c", "@", "3", "42"]

i = 0
while i < len(strArr):
    print(strArr[i])
    i += 1

multiArr = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

print("len(multiArr) = " + str(len(multiArr)))
print("len(multiArr[0]) = " + str(len(multiArr[0])))
itrCount = 0
i = 0
while i < len(multiArr):
    j = 0
    while j < len(multiArr[0]):
        itrCount += 1
        if multiArr[i][j] == 1:
            print("i = " + str(i) + ", j = " + str(j))
            i = len(multiArr)
            break
        j += 1
    i += 1

print("itrCount = ", itrCount)

strWord = "Alex"
print(strWord[2])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2
print(list1 * 3)
print(8 in list1)
print("Al" in strWord)
print("Al1" not in strWord)

for number in list1:
    print(number)




