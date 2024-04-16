import time
from multiprocessing import Pool

def f(x=0):
    for _ in range(100_000_000):
        x += 1
    print(x)

init = time.perf_counter()
print("Start")

list(map(f, [0, 1, 2, 3]))

end = time.perf_counter()
print("End")
print("Time: ", end - init)


init = time.perf_counter()
print("Start")

p = Pool()
p.map(f, [0, 1, 2, 3])


end = time.perf_counter()
print("End")
print("Time: ", end - init)