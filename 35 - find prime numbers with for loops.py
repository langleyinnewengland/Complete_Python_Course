for n in range(2,21):
    for x in range(2,n):
        #if n/x has remainder 0
        if n % x ==0:
            print(f"{n} equals {x} * {n/x}")
            break
    #encountered a prime number
    else:
        print(f"{n} is a prime number")
