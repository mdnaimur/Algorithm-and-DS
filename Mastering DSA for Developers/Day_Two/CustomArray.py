DEFAULT_CAPACITY = 10

'''
Array Custom Operation
-- Insert( insert value with index number)
-- Push (push value insert without indexing)
-- Pop (Value or data delete from top)
-- remove ( Remove date)
-- get ( get value by index)
-- set (set the value index and elementsss)
-- IndexOf(find index throgh the element)
-- contains
-- clear ( reset array)
-- toArray ( slice or orginal formate)
-- toString (print value)

'''


class CustomArray:
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.capacity = capacity
        self.array = [None] * capacity
        self.length = 0

    def _resize(self, new_capacity):
        if new_capacity == self.capacity:
            return
        print(
            f"[DEBUG: resize]: I am working inside resize newCapacity {new_capacity}")
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
        # print(f' push: {self.array} = {element}')
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
            raise IndexError('Index out of bounds')

        if self.length == self.capacity:
            self._grow()

        # last item insert
        if index == self.length:
            # return self.push(element)
            self.array[index] = element
            self.length += 1
            return

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
            # print(f"array[{i}] Insert: {self.array}")

        self.array[index] = element
        self.length += 1

    def set(self, index, elemet):
        self._checkIndex(index)
        self.array[index] = elemet

    def get(self, index):
        self._checkIndex(index)
        return self.array[index]

    def index_of(self, element):
        for i in range(self.length):
            if self.array[i] == element:
                return i
        return -1

    def contains(self, elemet):
        return self.index_of(elemet) != -1

    def copy(self):
        # new_array = [None] * self.capacity  # it is raw not smart to take
        # smart for root level array creation
        new_array = CustomArray(self.capacity)

        for i in range(self.length):
            # new_array[i] = self.array[i]
            new_array.push(self.array[i])
        return new_array

    def remove(self, index):
        self._checkIndex(index)

        element = self.array[index]
        print("Remove value is: ", element)

        for i in range(self.length):
            self.array[i] = self.array[i+1]

        self.length -= 1

        if self.length < self.capacity // 4:
            self._shrink()
        return element

    def clear(self):
        self.array = [None] * DEFAULT_CAPACITY
        self.length = 0
        self.capacity = DEFAULT_CAPACITY

    def _checkIndex(self, index):
        if index < 0 or index > self.length:
            raise IndexError('Index out of bounds')

    def to_array(self):
        return self.array[:self.length]

    def __str__(self):  # default array print  if it not here it will print object ref
        return ', '.join(str(self.array[i]) for i in range(self.length))


# Example usage:
custom_array = CustomArray()
custom_array.push(5)
custom_array.push(7)
custom_array.push(2)
custom_array.push(3)

custom_array.push(50)
custom_array.push(70)
custom_array.push(20)
custom_array.push(30)

custom_array.push(15)
custom_array.push(27)
custom_array.push(32)
custom_array.push(43)

# custom_array.insert(1, 22)
# custom_array.insert(0, 15)
# custom_array.insert(2, 25)
# custom_array.insert(7, 32)
# custom_array.insert(custom_array.length, 99)

# custom_array.remove(3)

print(custom_array.array)
print(f'lenght is now : {custom_array.length}')

# newCopyArray = custom_array.copy()
# print(f'copying array : {newCopyArray}')
# custom_array.clear()
# print("Clear Array:", custom_array.to_array())
# print('Array Type:', type(newCopyArray))
# print("copy array from ", newCopyArray.to_array())

# index_element = newCopyArray.index_of(25)
# if index_element != -1:
#     print(f"Found index of eleemts {index_element}")
# else:
#     print("not found for this element")

# pop_item = newCopyArray.pop()

# print(
#     f"PoP element {pop_item} \n After Pop new Array {newCopyArray.to_array()}")

# set_item = newCopyArray.set(1, 40)
# print(f" set new array {newCopyArray.to_array()}")

# get_item = newCopyArray.get(2)
# print(f"{get_item} is retribe from {newCopyArray.to_array()}")

# if newCopyArray.contains(get_item):
#     print("Item is found")
# else:
#     print(f"{get_item} not found")
