class Jar:

    def __init__(self, capacity=12):

        self._size = 0

        if type(capacity) is not int:
            raise ValueError
        if capacity >= 0:
            self._capacity = capacity
        else: 
            raise ValueError
            

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if not n >= 0:
            raise ValueError
        if self._size + n > self._capacity:
            raise ValueError
        else:
            self._size += n


    def withdraw(self, n):
        if not n >= 0:
            raise ValueError
        if n > self._size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(20)
    print(jar.capacity)
    print(jar.size)
    jar.deposit(10)
    print(jar.size)
    print(jar)
    jar.withdraw(5)
    print(jar.size)
    print(jar)

if __name__ == "__main__":
    main()