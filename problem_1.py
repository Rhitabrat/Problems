"""
All students need to write a number on board from a particular range. They have to find a
solution to find closest pair from numbers written.
"""
print("Enter the numbers separated by a space:")
arr = input()
l = list(map(int, arr.split(' ')))


def closestPair(ls):
    ls.sort()
    a = [ls[i + 1] - ls[i] for i in range(len(ls)-1)]

    b = a.index(min(a))
    idx = [index for index, value in enumerate(a) if value == b]

    print("The closest pairs are:")
    for i in idx:
        print("("+str(ls[i])+", "+str(ls[i+1])+")")

closestPair(l)
