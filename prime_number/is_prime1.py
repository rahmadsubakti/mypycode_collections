def is_prime(n):
    if n == 1:
        return False # 1 is not prime number
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 119]

for i in lst:
    print(is_prime(i)"is prime", end='\n')
