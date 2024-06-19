import time
import random

def bubble_sort(x: list[int]):
    for _ in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j+1]:
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
            



list_input:list[int]=[random.randint(0,100) for _ in range(100)]

start=time.time()
end=time.time()

bubble_sort(list_input)
print(list_input)
print(f"Bubblesort:{end-start}")
