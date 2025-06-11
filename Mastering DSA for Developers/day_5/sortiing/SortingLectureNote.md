
# Sorting

Sorting is the process of arranging data in a particular order—usually ascending (small to large) or descending (large to small). It’s a fundamental operation in computer science that helps in optimizing search operations, organizing data meaningfully, and preparing datasets for algorithms that require ordered input (e.g., binary search).

## Types of Sorting

- **Internal Sorting:** Sorting is done entirely in main memory. Used when data fits in RAM.  
  *Examples:* Quick Sort, Merge Sort, Bubble Sort.

- **External Sorting:** Used when data is too large to fit into memory and needs disk-based sorting.  
  *Example:* External Merge Sort.

### Stable vs. Unstable Sorting

- **Stable:** Maintains the relative order of equal elements.
- **Unstable:** May change the order of equal elements.

### Comparison-based vs. Non-comparison-based

- **Comparison-based:** Relies on comparing elements.  
  *Examples:* Merge Sort, Quick Sort, Bubble Sort.
- **Non-comparison-based:** Uses techniques like counting or hashing.  
  *Examples:* Counting Sort, Radix Sort, Bucket Sort.

---

## Common Sorting Algorithms

| Algorithm      | Time (Avg)   | Space  | Stable | Summary (How It Works) |
|----------------|--------------|--------|--------|-----------------------|
| Bubble Sort    | O(n²)        | O(1)   | ✅ Yes | Repeatedly swaps adjacent elements if they are in the wrong order. |
| Selection Sort | O(n²)        | O(1)   | ❌ No  | Selects the smallest element and places it at the correct position one by one. |
| Insertion Sort | O(n²)        | O(1)   | ✅ Yes | Inserts each element into its correct position in a growing sorted part of the array. |
| Merge Sort     | O(n log n)   | O(n)   | ✅ Yes | Recursively divides the array and merges sorted halves. |
| Quick Sort     | O(n log n)   | O(log n)| ❌ No | Picks a pivot, partitions elements around it, and recursively sorts subarrays. |
| Heap Sort      | O(n log n)   | O(1)   | ❌ No  | Builds a max heap and repeatedly extracts the maximum element. |
| Counting Sort  | O(n + k)     | O(k)   | ✅ Yes | Counts the frequency of each element and uses it to place elements in order. |
| Bucket Sort    | O(n + k)     | O(n + k)| ✅ Yes | Distributes elements into buckets, sorts each bucket, then concatenates them. |

---

## Sorting Array vs Linked List

### Sorting an Array

✅ Easy to access any element instantly.  
✅ Swapping elements is trivial (no structure breaks).  
✅ Many fast algorithms (Quick Sort, Heap Sort) work best with arrays.  
⚠️ Sorting needs care with large arrays.

### Sorting a Linked List

❌ Random access is expensive (no jumping to middle).  
❌ Swapping values is inefficient (rewiring links is tricky).  
✅ However, merging two lists (Merge Sort) is very efficient (only pointer changes).

### Algorithms Comparison

| Algorithm         | Array | Linked List | Notes |
|-------------------|-------|-------------|-------|
| Bubble Sort       | ✅    | ✅ (but slow)| Simple, but O(n²). |
| Selection Sort    | ✅    | ✅          | Simple, but not ideal for large datasets. |
| Insertion Sort    | ✅    | ✅          | Good for small or nearly sorted data. |
| Quick Sort        | ✅ Best | ❌ Bad      | Needs random access, bad for linked lists. |
| Merge Sort        | ✅    | ✅ Best      | Perfect for linked lists (easy merging). |
| Heap Sort         | ✅    | ❌ Not practical | Heap needs array-like structure. |
| Counting/Bucket Sort | ✅ | ❌         | Needs direct indexing (arrays only). |

---

## Bubble Sort

Bubble Sort is one of the simplest sorting algorithms. It repeatedly compares adjacent elements and swaps them if they are in the wrong order, slowly “bubbling” the largest value to the end in each pass.

### Complexity

| Case  | Time Complexity |
|-------|-----------------|
| Best (sorted) | O(n) — thanks to early exit |
| Average      | O(n²) |
| Worst        | O(n²) |
| Space        | O(1) — in-place |

### General Implementation of Bubble Sort

```javascript
function bubbleSortBad(arr = []) {
	for (let i = 0; i < arr.length; i++) {
		for (let j = 0; j < arr.length; j++) {
			if (arr[j] > arr[j + 1]) {
				[arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
			}
		}
	}
	return arr;
}

const arr2 = [64, 34, 25, 12, 22, 11, 90];
console.log(bubbleSortBad(arr2));
```

### Improved Implementation

```javascript
function bubbleSortGood(arr = []) {
	let n = arr.length;
	let swapped;

	for (let i = 0; i < n - 1; i++) {
		swapped = false;

		for (let j = 0; j < n - 1 - i; j++) {
			if (arr[j] > arr[j + 1]) {
				[arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
				swapped = true;
			}
		}

		if (!swapped) break;
	}

	return arr;
}

const arr = [64, 34, 25, 12, 22, 11, 90];
console.log(bubbleSortGood(arr));
```

### How it Works?

Sorting `[3, 1, 4, 2]`

- First pass:
  - Compare 3 and 1 → swap → `[1, 3, 4, 2]`
  - Compare 3 and 4 → no swap
  - Compare 4 and 2 → swap → `[1, 3, 2, 4]`

- Second pass:
  - Compare 1 and 3 → no swap
  - Compare 3 and 2 → swap → `[1, 2, 3, 4]`

- Third pass:
  - Compare 1 and 2 → no swap → done ✅

---

## Selection Sort

### Complexity

| Case  | Time Complexity |
|-------|-----------------|
| Best  | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) — in-place |

### Implementation

```javascript
function selectionSort(arr = []) {
	const n = arr.length;

	for (let i = 0; i < n - 1; i++) {
		let minIndex = i;

		for (let j = i + 1; j < n; j++) {
			if (arr[j] < arr[minIndex]) {
				minIndex = j;
			}
		}

		if (minIndex !== i) {
			[arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
		}
	}

	return arr;
}

const arr = [64, 34, 25, 12, 22, 11, 90];
console.log(selectionSort(arr));
```

### How it works?

Sorting `[3, 1, 4, 2]`:

- First pass:
  - Min is 1 → swap with 3 → `[1, 3, 4, 2]`

- Second pass:
  - Min in `[3, 4, 2]` is 2 → swap with 3 → `[1, 2, 4, 3]`

- Third pass:
  - Min in `[4, 3]` is 3 → swap → `[1, 2, 3, 4]`

✅ Sorted.

---

## Insertion Sort

### Complexity

| Case  | Time Complexity |
|-------|-----------------|
| Best (sorted) | O(n) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) — in-place |

### Implementation

```javascript
function insertionSort(arr = []) {
	const n = arr.length;

	for (let i = 1; i < n; i++) {
		let current = arr[i];
		let j = i - 1;

		while (j >= 0 && arr[j] > current) {
			arr[j + 1] = arr[j];
			j--;
		}

		arr[j + 1] = current;
	}

	return arr;
}

const arr = [64, 34, 25, 12, 22, 11, 90];
console.log(insertionSort(arr));
```

### How it works?

Sorting `[4, 3, 5, 1]`:

- First pass:
  - Insert 3 → `[3, 4, 5, 1]`

- Second pass:
  - 5 is greater than 4 → stays

- Third pass:
  - Insert 1 → `[1, 3, 4, 5]`

✅ Sorted.

---

## Selection vs Insertion Sort

| Aspect                   | Selection Sort          | Insertion Sort          |
|--------------------------|-------------------------|------------------------|
| Basic Idea               | Select min/max and place | Insert each element into position |
| Best Case Time           | O(n²)                   | O(n) (if already sorted) |
| Average & Worst Case     | O(n²)                   | O(n²)                   |
| Space                    | O(1)                    | O(1)                    |
| Stability                | No                      | Yes                     |
| Suitable For             | Small arrays, simplicity| Nearly sorted arrays    |

---





# Bucket Sort

Bucket Sort is a sorting algorithm that:

- Distributes elements into buckets based on a specific range or criteria.
- Sorts each bucket individually, often using another sorting algorithm (like insertion sort or quicksort).
- Concatenates all the buckets to form the final sorted array.

## How Bucket Sort Works?

### 1. Decide the number of buckets
- Buckets are just “groups” to hold similar items.
- You choose how many buckets you want based on your data range and how spread out the values are.

### 2. Put each item into the right bucket
- Look at each item in the array.
- Decide which bucket it belongs to based on its value.  
  Example: If value is `23` and bucket size is `10`, it goes into the 2nd bucket — `bucket[2]`.

### 3. Sort each bucket
- After all items are placed into buckets, sort the items inside each bucket.
- Each bucket is usually small, so sorting is fast.

### 4. Join all buckets together
- Go through all buckets in order.
- Pull out the sorted items from each bucket and combine them into one big sorted array.

## Example

Array to sort: `[29, 25, 3, 49, 9, 37, 21, 43]`

- Create 5 buckets (say 0–9, 10–19, 20–29, 30–39, 40–49)

### Distribute:

- 29 → bucket 2
- 25 → bucket 2
- 3 → bucket 0
- 49 → bucket 4
- 9 → bucket 0
- 37 → bucket 3
- 21 → bucket 2
- 43 → bucket 4

### Buckets after distributing:

- bucket 0: `[3, 9]`
- bucket 2: `[29, 25, 21]`
- bucket 3: `[37]`
- bucket 4: `[49, 43]`

### Sort each bucket:

- bucket 0: `[3, 9]`
- bucket 2: `[21, 25, 29]`
- bucket 3: `[37]`
- bucket 4: `[43, 49]`

### Merge:

`[3, 9, 21, 25, 29, 37, 43, 49]`

## Basic Implementation

```javascript
function bucketSort(arr) {
  const n = arr.length;
  if (n <= 0) return arr;

  // Create empty buckets
  const buckets = Array.from({ length: n }, () => []);

  // Put array elements in different buckets
  for (let i = 0; i < n; i++) {
    const index = Math.floor(arr[i] * n);
    buckets[index].push(arr[i]);
  }

  // Sort individual buckets and concatenate
  return buckets.flatMap(bucket => bucket.sort((a, b) => a - b));
}
````

## Using Bucket Sort on an Array of Objects

We want to sort this data:

```javascript
const students = [
  { name: "Alice", score: 87 },
  { name: "Bob", score: 92 },
  { name: "Charlie", score: 78 },
  { name: "David", score: 85 },
  { name: "Eve", score: 90 },
];
```

### Step-by-Step:

* Normalize scores (if needed). Let’s assume scores are between 0 and 100.
* Map scores to buckets.
* Sort each bucket based on score.
* Concatenate the results.

```javascript
function bucketSortObjects(arr, key) {
  const n = arr.length;
  if (n <= 0) return arr;

  const buckets = Array.from({ length: 10 }, () => []);

  for (let i = 0; i < n; i++) {
    const value = arr[i][key];
    const index = Math.floor((value / 100) * 10); // Normalize
    buckets[index].push(arr[i]);
  }

  return buckets.flatMap(bucket => bucket.sort((a, b) => a[key] - b[key]));
}

// Example usage
const sortedStudents = bucketSortObjects(students, "score");
```

## Is Bucket Sort Similar to a Hash Table?

* Both distribute data based on a key or value.
* Both involve some kind of “bucket” (or slot) for organizing elements.
* Both may suffer from collisions and need a way to handle multiple values per slot.

### Difference Between Bucket Sort & Hash Table

| Feature          | Bucket Sort                          | Hash Table                      |
| ---------------- | ------------------------------------ | ------------------------------- |
| Purpose          | Sorting                              | Fast lookup/insertion/deletion  |
| Collisions       | Sorted inside buckets                | Resolved using chaining/probing |
| Ordering         | Output is sorted                     | No inherent ordering            |
| Internal Sorting | Uses another sorting algo per bucket | Not applicable                  |

## Time Complexity using Array Based Solution

| Case    | Time Complexity     | Notes                                |
| ------- | ------------------- | ------------------------------------ |
| Best    | O(n)                | Uniform distribution, simple sorting |
| Average | O(n + n log(n/k))   | Depends on how balanced buckets are  |
| Worst   | O(n²) or O(n log n) | All elements in one bucket           |
| Space   | O(n + k)            | One bucket per range segment         |

## Implementation using Linked List

```javascript
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SortedLinkedList {
  constructor() {
    this.head = null;
  }

  insert(value) {
    const newNode = new Node(value);
    if (!this.head || value < this.head.val) {
      newNode.next = this.head;
      this.head = newNode;
      return;
    }
    let current = this.head;
    while (current.next && current.next.val < value) {
      current = current.next;
    }
    newNode.next = current.next;
    current.next = newNode;
  }

  toArray() {
    const result = [];
    let curr = this.head;
    while (curr) {
      result.push(curr.val);
      curr = curr.next;
    }
    return result;
  }
}

function bucketSortWithLinkedList(arr) {
  const n = arr.length;
  if (n <= 0) return arr;

  const buckets = Array.from({ length: n }, () => new SortedLinkedList());

  for (let i = 0; i < n; i++) {
    const index = Math.floor(arr[i] * n);
    buckets[index].insert(arr[i]);
  }

  return buckets.flatMap(bucket => bucket.toArray());
}
```

## Time Complexity using Linked List Based Solution

| Step                  | Time Complexity        |
| --------------------- | ---------------------- |
| Distribute to buckets | O(n)                   |
| Insert sorted (LL)    | O(1) avg, O(n/k) worst |
| Concatenate           | O(n)                   |

## Example Scenario

### Sorting student data (name, roll no, score between 1-100) using Bucket Sort.

#### Choosing number of buckets `k`:

* **k ≈ √n**
  Common statistical heuristic.
  If n = 30 → k ≈ √30 ≈ 5 to 6 buckets.

* **Domain Range / Expected Bucket Width**
  Domain = 1-100 → if 10 point buckets → k = 100 / 10 = 10.

### Let’s Use: `k = 10`

* Bucket 0 → 0-9
* Bucket 1 → 10-19
* …
* Bucket 9 → 90-100

### Data Example

```javascript
const students = [
  { name: "Alice", roll: 1, score: 87 },
  { name: "Bob", roll: 2, score: 92 },
  { name: "Charlie", roll: 3, score: 78 },
  ...
];
```

### Array Implementation

```javascript
function bucketSortForStudents(students = []) {
  const k = students.length / 2;
  const buckets = Array.from({ length: k }, () => []);

  for (const student of students) {
    const index = Math.floor(student.score / (100 / k));
    buckets[index].push(student);
  }

  console.log('buckets', JSON.stringify(buckets, null, 2));

  return buckets.flatMap(bucket => bucket.sort((a, b) => a.score - b.score));
}
```

#### Explanation of index calculation:

```javascript
const index = Math.floor(student.score / (100 / k));
```

* `100 / k` → Bucket range size.
* `student.score / (100 / k)` → Determines bucket index.
* `Math.floor()` → Ensures index is an integer.

### Linked List Implementation

```javascript
class StudentNode {
  constructor(student) {
    this.student = student;
    this.next = null;
  }
}

class SortedStudentList {
  constructor() {
    this.head = null;
  }

  insert(student) {
    const node = new StudentNode(student);
    if (!this.head || student.score < this.head.student.score) {
      node.next = this.head;
      this.head = node;
      return;
    }

    let current = this.head;
    while (current.next && current.next.student.score < student.score) {
      current = current.next;
    }
    node.next = current.next;
    current.next = node;
  }

  toArray() {
    const result = [];
    let current = this.head;
    while (current) {
      result.push(current.student);
      current = current.next;
    }
    return result;
  }
}

function bucketSortStudentsLL(students) {
  const k = 10;
  const buckets = Array.from({ length: k }, () => new SortedStudentList());

  for (const student of students) {
    const index = Math.min(Math.floor(student.score / 10), k - 1);
    buckets[index].insert(student);
  }

  return buckets.flatMap(bucket => bucket.toArray());
}
```

## Complexity Analysis

| Step                  | Array-Based Bucket | Linked List Bucket |
| --------------------- | ------------------ | ------------------ |
| Distribute to buckets | O(n)               | O(n)               |
| Intra-bucket sorting  | O(m log m)         | O(m²)              |
| Concatenation         | O(n)               | O(n)               |
| Total Avg. Time       | O(n + n log(n/k))  | O(n) (if m ≈ 1)    |
| Total Worst Time      | O(n log n)         | O(n²)              |
| Space                 | O(n + k)           | O(n + k)           |

## Comparison of Approaches

### Array of Buckets → Sort Later

* Each bucket holds values unsorted at first.
* Sort them later (e.g., quicksort, `.sort()`).
* Efficient even if `m` is a bit large.

### Linked List Bucket with Sorted Insert

* Each value is inserted in order.
* Worse performance as `m` increases.

### Example: Bucket gets 30 elements (m = 30)

| Strategy                     | Time Cost             |
| ---------------------------- | --------------------- |
| Array + Sort                 | O(30 log 30) ≈ O(150) |
| Sorted Insert in Linked List | O(30²) = O(900)       |

**Summary:**
For very small buckets (like 3–5 items), `O(m²)` is acceptable.
For large buckets, array + sort is faster and more efficient.

```

---

If you want, I can also generate a **`.md` file** and give it to you for download directly — would you like me to? Just say **yes**. 🚀
```
