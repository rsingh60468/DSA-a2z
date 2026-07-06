# PRINT 1 TO N USING RECURRSION

def printNumber(n, i=1):
    print(i)
    if i == n:
        return
    printNumber(n, i+1)

# printNumber(5)

# PRINT N TO 1 USING RECURRSION 

def printRevNum(n):
    print(n)
    if n == 1:
        return
    printRevNum(n-1)

# printRevNum(5)

# SUM OF FIRST N NUMBERS

def sumNum(n, i = 1, gt = 0):
    gt = gt + i
    if i == n:
        print(gt)
        return gt
    sumNum(n, i+1, gt)

# sumNum(5)

# FACTORIAL OF GIVEN NUMBER N

def Factorial(n, i = 1, fact = 1):
    fact = fact * i
    if i == n:
        print(fact)
        return fact
    Factorial(n, i+1, fact)

# Factorial(8)

# REVERSE AN ARRAY

nums = [1, 2, 3, 4, 5]
def RevArr(arr, i = 0, dupe = []):
    if i == len(arr):
        print(dupe)
        return dupe
    dupe.append(arr[len(arr) - 1 - i])
    RevArr(arr, i + 1, dupe)
    
# RevArr(nums)

# CHECK IF STRING IS PELINDROM OR NOT

string = "hahahah"
def Palindrom(s, i = 0):
    if i >= len(s)/2:
        print("is palindrom")
        return True

    if s[i] == s[len(s) - 1 - i]:
        Palindrom(s, i + 1)
    else:
        print("not a palindrom")
        return False

# Palindrom(string)

# FIBONACI NUMBER

def F(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return (F(n-1) + F(n-2))

# print(F(8))