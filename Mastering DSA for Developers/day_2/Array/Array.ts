const DEFAULT_CAPACITY = 53;

class CustomArray<T> {
  private capacity: number;
  private array: (T | undefined)[];
  private length: number;

  constructor(capacity: number = DEFAULT_CAPACITY) {
    this.capacity = capacity;
    this.array = new Array<T | undefined>(capacity);
    this.length = 0;
  }

  private resize(newCapacity: number): void {
    if (newCapacity === this.capacity) return;

    const newArray = new Array<T | undefined>(newCapacity);
    for (let i = 0; i < this.length; i++) {
      newArray[i] = this.array[i];
    }
    this.array = newArray;
    this.capacity = newCapacity;
  }

  private grow(): void {
    this.capacity *= 2;
    this.resize(this.capacity);
  }

  private shrink(): void {
    if (this.capacity / 2 < this.length) return;
    this.capacity = Math.max(DEFAULT_CAPACITY, Math.floor(this.capacity / 2));
    this.resize(this.capacity);
  }

  push(element: T): void {
    if (this.length === this.capacity) {
      this.grow();
    }
    this.array[this.length] = element;
    this.length++;
  }

  pop(): T {
    if (this.length === 0) {
      throw new Error('Array is empty');
    }
    const element = this.array[this.length - 1];
    this.length--;

    if (this.length < this.capacity / 4) {
      this.shrink();
    }

    return element as T;
  }

  insert(index: number, element: T): void {
    if (index < 0 || index > this.length) {
      throw new Error('Index out of bounds');
    }

    if (this.length === this.capacity) {
      this.grow();
    }

    for (let i = this.length; i > index; i--) {
      this.array[i] = this.array[i - 1];
    }
    this.array[index] = element;
    this.length++;
  }

  remove(index: number): T {
    if (index < 0 || index >= this.length) {
      throw new Error('Index out of bounds');
    }

    const element = this.array[index];
    for (let i = index; i < this.length - 1; i++) {
      this.array[i] = this.array[i + 1];
    }
    this.length--;

    if (this.length < this.capacity / 4) {
      this.shrink();
    }

    return element as T;
  }

  get(index: number): T {
    if (index < 0 || index >= this.length) {
      throw new Error('Index out of bounds');
    }
    return this.array[index] as T;
  }

  set(index: number, element: T): void {
    if (index < 0 || index >= this.length) {
      throw new Error('Index out of bounds');
    }
    this.array[index] = element;
  }

  indexOf(element: T): number {
    for (let i = 0; i < this.length; i++) {
      if (this.array[i] === element) {
        return i;
      }
    }
    return -1;
  }

  contains(element: T): boolean {
    return this.indexOf(element) !== -1;
  }

  clear(): void {
    this.array = new Array<T | undefined>(DEFAULT_CAPACITY);
    this.length = 0;
    this.capacity = DEFAULT_CAPACITY;
  }

  toArray(): T[] {
    return this.array.slice(0, this.length) as T[];
  }

  toString(): string {
    return this.toArray().join(', ');
  }
}

// ✅ Example Usage:
const customArray = new CustomArray<number>();
customArray.push(5);
customArray.push(2);
customArray.push(3);

console.log(customArray.toArray()); // [5, 2, 3]
