# Iterator that generates numbers from 1 to n (inclusive)
class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration
        

counter = Counter(10)
for o in counter:
    print(o)


# Iterator that yields even numbers from 0 up to n
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current < self.n:
            num = self.current
            self.current += 1

            if num % 2 == 0:
                return num
        
        raise StopIteration
    
    
even_nums = EvenNumbers(21)
for o in even_nums:
    print(o)


# Iterator that yields every second element from the given list
class EverySecond:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.nums):
            num = self.nums[self.index]
            self.index += 2
            return num
        
        raise StopIteration
    

every_second = EverySecond([10, 20, 30, 40, 50])
for i in every_second:
    print(i)