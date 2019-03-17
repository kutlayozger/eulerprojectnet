t = 600851475143
primes = [2, 3]
for i in range(int(pow(t, 0.5))):
    if i > 3:
      if i % 2 != 0:
        if i % 3 !=0:
            prime = True
            for j in primes:
                if i % j == 0:
                    prime = False
            if prime:
                primes.append(i)
            if (prime and t % i == 0):
                print("i:", i)
