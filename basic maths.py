# ARMSTRONG NUMBER

# n = 153
# og = n
# p = len(str(n))
# sm = 0
# while n > 0:
#     digit = n % 10
#     sm = sm + digit ** p
#     n = n // 10
# if sm == og:
#     print(True)
# else:
#     print(False)

# PRINT ALL DEVISORS

# n = 6
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)
    
# GDC OF 2 NUMBER

# n1 = 12
# n2 = 6
# l1 = {1} #using sets bcox lists dont have intersection method
# l2 = {1}
# for i in range(1, n1+1):
#     if n1 % i == 0:
#         l1.add(i)

# for j in range(1, n2+1):
#     if n2 % j == 0:
#         l2.add(j)

# print(max(l1.intersection(l2)))

# CHECK FOR PRIME NUMBER

n = 19
l1 = []
for i in range(1, n+1):
    if n % i == 0:
        l1.append(i)
if len(l1) == 2:
    print("prime")
else:
    print("composite")