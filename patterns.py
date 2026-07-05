#PATTERN PRINTING
import string
n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print("")

# for i in range(n): #easy
#     print("*"*n)

# for i in range(1,n+1):
#     print("*"*i)

# for i in range(1, n+1):
#     print(str(i)*i)

# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print("*"*n)
#     else:
#         print("*"," "*(n-2),"*", sep="")

# for i in range(1, n+1):
#     print(str(n-i+1)*(n-i+1))

# for i in range(1, n+1):
#     print(" "*(n-i),str(i)*i)

# for i in range(1, n+1):
#     # print(str(i)*i)
#     for n in range(i):
#         print(n+1, end="")
#     print("")

# for i in range(1,n+1):
#     print(" "*(n-i), "*"*i, "*"*(i-1), sep="")

# PATTERN NO. 13

# cnt =1
# for i in range(1, n+1):
#     for j in range(1, 1+i):
#         print(cnt, end="")
#         cnt +=1
#     print("")

# PATTERN NO. 14

# print(string.ascii_lowercase)
# for i in range(1, n+1):
#     print(string.ascii_lowercase[:i])

# PATTERN NO. 11

# for i in range(n):
#     for j in range(i+1):
#         if (i + j) % 2 == 0:
#             print(1, end="")
#         else:
#             print(0, end="")
#     print("")

# PATTERN 21

for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        right = 2*n-2-j
        bottom = 2*n-2-i
        print(n-min(top, left, right, bottom), end="")
    print("")