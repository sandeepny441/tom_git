def is_prime(given_num):
    upper_bound = int(given_num ** 0.5)+1
    for i in range(2, upper_bound):
        if given_num % i == 0:
            return False
    return True


print(is_prime(23))
