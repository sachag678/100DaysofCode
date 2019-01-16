import multiprocessing
import random

def simulate(queue):
    cycles = random.randint(200, 400)
    print(cycles)
    for i in range(cycles):
        # Some abitrary action
        l = [i for i in range(10)]
        queue.put((l, random.randint(5, 10)))

queue = multiprocessing.Queue()
processes = []
num_cores = 8

for i in range(num_cores):
    process = multiprocessing.Process(target=simulate, args=(queue, ))
    processes.append(process)
    process.start()

data = []
while 1:
    running = any(p.is_alive() for p in processes)
    while not queue.empty():
        data.append(queue.get())
    if not running:
        break

print(len(data))

for proc in processes:
    print('Process {} Done'.format(proc.pid))
    proc.join()

print('Simulation Complete')

