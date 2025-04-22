DEFAULT_CAPACITY = 53


class CustomArray:
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.capacity = capacity
        self.array = [None] * capacity
        self.length = 0

    def _resize(self, new_capacity):
        if new_capacity == self.capacity:
            return
        new_array = [None] * new_capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def _grow(self):
        self._resize(self.capacity * 2)

    def _shrink(self):
        if self.capacity // 2 < self.length:
            return
        self._resize(max(DEFAULT_CAPACITY, self.capacity // 2))

    def push(self, element):
        if self.length == self.capacity:
            self._grow()
        self.array[self.length] = element
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Array is empty")
        element = self.array[self.length - 1]
        self.length -= 1
        if self.length < self.capacity // 4:
            self._shrink()
        return element

    def insert(self, index, element):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.capacity:
            self._grow()
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        element = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1
        if self.length < self.capacity // 4:
            self._shrink()
        return element

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index, element):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        self.array[index] = element

    def index_of(self, element):
        for i in range(self.length):
            if self.array[i] == element:
                return i
        return -1

    def contains(self, element):
        return self.index_of(element) != -1

    def clear(self):
        self.array = [None] * DEFAULT_CAPACITY
        self.length = 0
        self.capacity = DEFAULT_CAPACITY

    def to_array(self):
        return self.array[:self.length]

    def __str__(self):
        return ', '.join(str(self.array[i]) for i in range(self.length))


# Example usage:
custom_array = CustomArray()
custom_array.push(5)
custom_array.push(2)
custom_array.push(3)

print(custom_array.to_array())  # [5, 2, 3]
