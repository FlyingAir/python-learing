classmates = ['jay', 'fay', 'me']
print(classmates)
print(len(classmates))
print("1:"+classmates[0]+"\n2:"+classmates[1]+"\n3:"+classmates[2])
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text[:3])
print(text[4:])
print(text[1:3])
# 负数：-1 从倒数第一个开始
print(classmates[-1]+classmates[-2])
classmates.append("MJ")
classmates.insert(0, "aaa")
classmates.pop()
classmates.pop(2)
print(classmates)
t = (1, 2, 3)
print(t)
d = (1,)
print(d)
# Fibonacci series:
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, b+a

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

