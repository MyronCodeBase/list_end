import random


def list_end():
    #a = random.sample(range(10), 5)
    a = [1,2,3,4]
    b = a[:1] + a[-1:]
    print(b)


list_end()