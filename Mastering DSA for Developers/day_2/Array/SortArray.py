DEFAULT_SIZE = 7


class SortedArray:
    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.array = [None] * size
        self.length = 0

    def insert(self, value):
        if self.length < 0:
            raise IndexError("Index out of box")

        if self.length == self.size:
            self._doble_size()

        i = self.length  # i value set exmple: lenght = 4

        while i > 0 and self.array[i - 1] > value:
            self.array[i] = self.array[i - 1]
            i -= 1

        self.array[i] = value
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]

        self.length -= 1

        if self.length < self.size // 2:
            self._half_size()

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        return self.array[index]

    def search(self, value):
        left = 0
        right = self.length - 1

        while left < right and self.array[left] <= value and self.array[right] >= value:
            mid = (left + right) // 2
            if self.array[mid] == value:
                return value
            elif self.array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def _resize(self, new_size):
        if new_size == self.size:
            return

        new_array = [None] * new_size
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.size = new_size

    def _doble_size(self):
        self._resize(self.size * 2)

    def _half_size(self):
        if self.size // 2 < self.length:
            return
        self._resize(self.size // 2)

    def clear(self):
        self.array = [None] * DEFAULT_SIZE
        self.length = 0
        self.size = DEFAULT_SIZE

    def __str__(self):
        return ', '.join(str(x) for x in self.array[:self.length])


sortArray = SortedArray()

sortArray.insert(95)
sortArray.insert(19)
sortArray.insert(25)
sortArray.insert(5)
sortArray.insert(15)
sortArray.insert(1)
sortArray.insert(115)

print(sortArray.array)
print(f"length {sortArray.length}")
print(f"siZe {sortArray.size}")

sortArray.remove(3)
print(
    f"Value searching result: {'found' if sortArray.search(1555) != -1 else 'not found'}")
print("after remvoe", sortArray.array)
print(f"length {sortArray.length}")
print(f"siZe {sortArray.size}")
print(f"get the item {sortArray.get(3)}")

print(f"Clear Array {sortArray.clear()}")
