import unittest

class Queue():

    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)
    
    def remove(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)
    
    def __repr__(self):
        s = '['

        for i in range(len(self.queue)):
            s += str(self.queue[i])

            if i < len(self.queue) - 1:
                s += ','
        
        s += ']'
        return s
    
    def __getitem__(self, index):
        return self.queue[index]
    
    def __len__(self):
        return len(self.queue)

class Animal():

    def __init__(self, name):
        self.order = None
        self.name = name
    
    def order_greater(self, animal):
        return self.order < animal.order
    
    def __repr__(self):
        s = ''
        s += self.__class__.__name__
        s += ':'
        s += self.name
        s += ':'
        s +=  str(self.order)
        return s

class dog(Animal):
    pass

class cat(Animal):
    pass

class AnimalShelter():

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0
    
    def __repr__(self):
        s = ''
        dog_counter = 0
        cat_counter = 0
        ordered_list = []
        for _ in range(len(self.dogs) + len(self.cats)):
            if dog_counter < len(self.dogs) and cat_counter < len(self.cats):
                if self.dogs[dog_counter].order_greater(self.cats[cat_counter]):
                    ordered_list.append(str(self.dogs[dog_counter]))
                    dog_counter += 1
                else:
                    ordered_list.append(str(self.cats[cat_counter]))
                    cat_counter += 1
            elif dog_counter >= len(self.dogs):
                ordered_list.append(str(self.cats[cat_counter]))
                cat_counter += 1
            elif cat_counter >= len(self.cats):
                ordered_list.append(str(self.dogs[dog_counter]))
                dog_counter += 1
        
        s += str(ordered_list)
        return s

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        
        if animal.__class__.__name__ == 'cat':
            self.cats.add(animal)
        if animal.__class__.__name__ == 'dog':
            self.dogs.add(animal)
    
    def dequeue_any(self):
        if self.dogs.peek().order_greater(self.cats.peek()):
            return self.dogs.remove()
        else:
            return self.cats.remove()
    
    def dequeue_dog(self):
        return self.dogs.remove()
    
    def dequeue_cat(self):
        return self.cats.remove()

class TestQueue(unittest.TestCase):

    def testAnimalShelter(self):
        pass

if __name__ == '__main__':
        shelter = AnimalShelter()

        animals = [dog('flash'), dog('gordon'), cat('devil'), cat('ginger')]

        for animal in animals:
            shelter.enqueue(animal)
        
        print(shelter)


