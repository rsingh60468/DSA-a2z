arr = [1, 2, 3, 1, 2]
# BRUTE FORCE METHOD
def f(array, n):
    counter = 0
    for i in array:
        if i == n:
            counter += 1
    print(counter)
    return counter
# f(arr,4)  

# HASHING
freq = {}
for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1

# print(freq)
# print(freq[2])
# print(freq.items())
max_freq = 0
el = None
for key, val in freq.items():
    if val > max_freq:
        max_freq = val
        el = key

# print([el, max_freq])