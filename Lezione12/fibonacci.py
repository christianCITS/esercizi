def fibonacci (i: int):

    a=1
    b=1

    for _ in range(i):

        c=a+b
        a=b
        b=c


    return b



import time



a= time.time()

print(fibonacci(52))


print(f"Tempo impiegato: {time.time()-a}")
