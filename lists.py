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

word1 = "qwerty"
countE = 0
for symbol in word1:
    if symbol == "e":
        countE += 1

print("countE =", countE)

numbers = list(range(1, 10, 2))
print(numbers)

for i in range(0, 5):
    print(i)

print(list1)
print(list1[1:3])
print(list1[:3])
print(list1[3:])
print(list1[::2])  # с шагом 2
print(list1[1:-1])
print(list1[::-1])  # reverse list!
print(list1[3:1:-1])  # reverse list!



