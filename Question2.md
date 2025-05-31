
# 📘 Assignment Instructions & Details

This **7-day assignment** is designed to evaluate your strategic understanding of core **data structures and algorithms** in real-world scenarios. You are expected to:

- Design thoughtful solutions  
- Justify your decisions with **complexity analysis**  
- Engage **creatively** with each problem

---

## 📤 Submission Guidelines

- Submit your work as a **public GitHub repository**
- Organize your repository with **clear folder structures**
- Include:
  - ✅ Source code with comments  
  - ✅ Diagrams  
  - ✅ Markdown explanations
- ❌ **AI tools** (e.g., ChatGPT, GitHub Copilot) are **not allowed**. Any detected use will result in **disqualification**

---

## 🧩 Part 1: Real-World Scenarios — Data Structures Design (40 Points)

Solve the following **real-world problems**. For each:

- Choose the **most appropriate data structure**
- Implement the solution
- Justify your choice with **complexity analysis**

---

### 🔄 Problem 1: Shopping Cart System (15 Points)

**Scenario:**  
A shopping cart system for an e-commerce site. Every time a user adds a product, the **latest added product** should appear at the top. When finalized, products should be processed from **oldest to newest**.

- Use a **Stack** to solve this
- Implement **efficient** push, pop, and finalization operations
- Consider **multi-stack** solutions if helpful

---

### 🎮 Problem 2: Multiplayer Game Matchmaking Queue (15 Points)

**Scenario:**  
Players join a real-time **matchmaking queue**, and matches are made once there are enough players.

- Implement a **Queue**
- Choose between **Array-based** or **Linked List-based** implementation
- Justify your choice based on **complexity** and **memory** considerations

---

### 📅 Problem 3: Event Scheduler with Min Stack (10 Points)

**Scenario:**  
Tasks are inserted sequentially, and you must retrieve the **highest priority** (lowest number) task **instantly**.

- Build a **Min Stack** supporting `getMin()` operation in **O(1)**
- Explain why a **Stack** is more suitable than alternative data structures

---

## ⚙️ Part 2: Algorithm Strategy Challenges (35 Points)

Solve the following **algorithmic decision problems**:

---

### 🔍 Challenge 1: Searching Strategy (15 Points)

**Scenario:**  
A hospital where patients arrive randomly. Doctors search for patients by **ID**.

- Choose between:
  - Linear Search  
  - Binary Search  
  - Interpolation Search  
  - Hash Map Search
- Implement your chosen method
- Discuss **why other options are less effective**

---

### 📦 Challenge 2: Searching in Product Catalog (10 Points)

**Scenario:**  
Managing a **sorted product catalog** with clustered similar products.

- Choose between:
  - Binary Search  
  - Interpolation Search
- Implement the best-suited method
- Explain your decision

---

### 🔄 Challenge 3: Sort the Right Way (10 Points)

**Scenario:**  
Sorting small batches of inventory (~50 items) that are **nearly sorted**.

- Choose between:
  - Bubble Sort  
  - Insertion Sort  
  - Selection Sort
- Justify using **complexity analysis**, especially for **best-case performance**

---

## 🧠 Part 3: Thinking Beyond Code (25 Points)

Answer the following **conceptual questions** concisely but insightfully:

1. **(5 Points)** One scenario where **Selection Sort** is better than **Insertion Sort**?
2. **(5 Points)** Why is **Bubble Sort** impractical for large datasets? When might it outperform **Merge Sort**?
3. **(5 Points)** Can you use **Binary Search** on an **infinite data stream**? Why or why not?
4. **(5 Points)** Stack (Array) vs Stack (Linked List) for **browser tab history** — which would you choose and why?
5. **(5 Points)** A limitation of an **Inverted Index** in real-world search engines and how to mitigate it?

---

## 📝 Evaluation Rubric

| Category                     | Points |
|-----------------------------|--------|
| Correct Implementation (Code) | 40     |
| Thought Process & Justification | 30     |
| Complexity Analysis           | 15     |
| Documentation & Clarity       | 10     |
| Creativity & Thoughtfulness   | 5      |
| **Total**                    | **100** |
