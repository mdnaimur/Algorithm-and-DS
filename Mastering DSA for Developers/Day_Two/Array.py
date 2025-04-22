DEFAULT_CAPACITY = 10


class CustomArray:
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.capacity = capacity
        self.array = [None] * capacity
        self.length = 0

    def _resize(self, new_capacity):
        pass

    def push(self, element):
        self.array[self.length] = element
        # print(f' push: {self.array} = {element}')
        self.length += 1

    def insert(self, index, element):
        # index < 0 or index > self.length:
        if index < 0 or index > self.length:
            raise IndexError('Index out of bounds')

        # if self.length == self.capacity:
        #     pass

        # last item insert
        if index == self.length:
            # return self.push(element)
            self.array[index] = element
            self.length += 1
            return

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
            print(f"array[{i}] Insert: {self.array}")

        self.array[index] = element
        self.length += 1

    def copy(self):
        newArray = [None] * self.capacity

        for i in range(self.length):
            newArray[i] = self.array[i]
        return newArray


# Example usage:
custom_array = CustomArray()
# custom_array.push(5)
# custom_array.push(7)
# custom_array.push(2)
# custom_array.push(3)

custom_array.insert(0, 22)
custom_array.insert(0, 15)
custom_array.insert(0, 25)
custom_array.insert(0, 32)
custom_array.insert(custom_array.length, 99)

print(custom_array.array)
print(f'lenght is now : {custom_array.length}')
