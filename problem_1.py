"""
All students need to write a number on board from a particular range. They have to find a
solution to find closest pair from numbers written.
"""

l = []
a = []
b = []
print("Enter the numbers separated by a space:")
arr = input()
l = list(map(int, arr.split(' ')))

def closestPair(ls):
    ls.sort() 
    a = [ls[i + 1] - ls[i] for i in range(len(ls)-1)]
    print(a)
        
    b = sorted(a)
    print("B: " + str(b))

    var = b[0]
    idx = a.index(var)
    # print(ind)
    print("Closest numbers are " + str(ls[idx]) + " and " + str(ls[idx+1]) + " with a difference of " + str(var))
    
    j=0
    while (a[j] == b[0]):
        j =j+1
        print(j)
        print("Biatch")
        
closestPair(l)