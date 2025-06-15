# Part 3: Thinking Beyon code

## 1. One scenario where Selection Sort  is better than Insertion Sort ?



---

**Ans:**
Let’s first understand how **Selection Sort** and **Insertion Sort** work. In both cases, the **worst-case time complexity is** $O(n^2)$.

* **Selection Sort**: This algorithm selects the first value as the minimum, then **traverses the unsorted part of the array to find the true minimum** and swaps it with the current position. It performs at most **O(n)** swaps.

* **Insertion Sort**: This algorithm compares the current element with elements on its left and **inserts it into the correct position by shifting elements** that are greater than it. It may perform **up to O(n²) swaps** in the worst case.

 **Key Difference:**
The number of **swaps** differs significantly:

* **Selection Sort** does fewer swaps: at most $O(n)$
* **Insertion Sort** can do up to $O(n^2)$ swaps

 In memory devices like **flash drives or pendrives**, which have a **limited number of write (swap) operations**, **Selection Sort is more suitable** than Insertion Sort because it minimizes write operations.

---


## 2. Why is Bubble Sort impractical for large datasets? When might it outperform Merge Sort?


Bubble sort time complexity Worst and average case O(n^2). It will take long time to sorting  data when datasets large it will become more time consume So this case Bubble sort is impractical for large datasets. 
Merge Sort Time complexity worst case O(n log n) which is very efficiency large datasets

Bubble sorts also too much swap which adds more overhead.
Where Bubble sorts is better:
* learing purpose , small datasets. 


