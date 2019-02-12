"""
My own code to generate prime in list
"""
def gen_prime(n):
    if n == 1:
        return "n must be bigger than 1"
    prime = []
    not_prime = []
    for i in range(2, n):
        if i not in not_prime:
            prime.append(i)
            not_prime += [x * i for x in range(2, (n//i)+1)]
    return prime

print(gen_prime(120))