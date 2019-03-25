import multiprocessing
import random
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class Model:
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(10, input_shape=(10, ),activation='relu'))
        self.model.add(Dense(1,activation='linear'))
        adam = Adam(lr=0.001)
        self.model.compile(loss='mse', optimizer=adam)
        self.weights = []
        self.updateW()

    def updateW(self):
        for layer in self.model.layers:
            self.weights.append(layer.get_weights()[0].T)

    def getW(self):
        return self.weights

m = Model()

manager = multiprocessing.Manager()
shared_data = manager.Namespace()
shared_data.w= m.getW()
shared_data.dontstop = True

def simulate(queue, shared_data):
    cont = shared_data.dontstop
    while cont:
        w = shared_data.w
        cycles = random.randint(2, 4)
        for i in range(cycles):
            # Some abitrary action
            l = [i for i in range(3)]
            queue.put((l, random.randint(5, 10)))
        queue.put('Done')
        cont = shared_data.dontstop

def updater(queue, model, shared_data):
    epoch = 0
    data = []
    while epoch < 10:
        item = queue.get()
        if item =='Done':
            epoch+=1
            print(epoch)
        else:
            data.append(item)
        if epoch == 3:
            model.updateW()
            shared_data.w = m.getW()
    shared_data.dontstop = False

queue = multiprocessing.Queue()
processes = []
num_cores = 7

for i in range(num_cores):
    process = multiprocessing.Process(target=simulate, args=(queue,shared_data))
    processes.append(process)

for proc in processes:
    proc.start()

updater(queue, m, shared_data)

while 1:
    running =any(p.is_alive() for p in processes)
    if not running:
        break;

for proc in processes:
    proc.join()
