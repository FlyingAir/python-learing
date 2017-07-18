arr = [1, 2, 3, 4, 5, 6]
print(max(arr))
print(hex(16))


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            print(int(x), 'is not a prime')
            return False
    else:
        print(int(x), 'is a prime')
        return True


result = is_prime(3)
print(result)
