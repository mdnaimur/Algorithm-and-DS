# 📘 Assignment Instructions & Details

---

## 📝 Overview

This 7-day assignment is designed to evaluate your understanding of core data structures—**Arrays, Linked Lists, Hash Tables, and Hash Sets**—along with **asymptotic analysis**. You will:

- Engage in complexity analysis  
- Implement custom data structures  
- Solve real-world inspired problems using appropriate structures

---

## 📤 Submission Guidelines

- Submit your work as a **public GitHub repository**
- Organize your repository with clear **folder structures**
- Include **source code**, **comments**, **diagrams**, and **Markdown explanations**
- ❌ **AI tools (e.g., ChatGPT, GitHub Copilot) are not allowed**  
  _Detected use will result in disqualification_

---

## 🧠 Part 1: Algorithm Complexity Analysis (30 Points)

Analyze **time and space complexity** for each of the following algorithms. For every algorithm:

- ✅ Provide input-output mapping
- ✅ Give step-by-step cost breakdown
- ✅ Determine final **asymptotic complexities** (time and space)
- ✅ Suggest optimizations, if any

**Algorithms to analyze:**

1. Insert at the beginning of a dynamic array  
2. Insert at the end of a linked list  
3. Search for an element in a hash set  
4. Rehash a hash table after crossing load factor  
5. Delete a node from a singly linked list by value  
6. Check if an array contains all unique values  
7. Count common elements in two hash sets  
8. Convert an array into a linked list  
9. Clone a hash table with chaining  
10. Compare array vs. hash set lookup performance

---

## 🛠️ Part 2: Custom Data Structures (30 Points)

Choose and implement **any two** of the following options. Each implementation must include:

- Clean and reusable **API**
- **Design explanation** with complexity
- Real-world applicability and trade-offs
- Inline documentation and **README** with diagram (if applicable)

**Options:**

### 🔹 Time-Aware Linked List
- Each node stores **timestamp of insertion**
- Add methods to retrieve nodes inserted within last _n_ seconds

### 🔹 Secure Hash Table
- Prime bucket sizing with auto-resizing
- Ordered key tracking
- Optional **TTL (time-to-live)** support for entries

### 🔹 Garbage-Collected Hash Set
- Automatically remove entries not used for a configurable time
- O(1) average lookup and deletion
- Manual clean-up support

### 🔹 Event-Driven Linked List
- Listens to insert/update/delete actions
- Supports registering **external listeners with callbacks**

---

## 🌍 Part 3: Real-World Problem Solving (20 Points)

Choose **any two** of the following problems and solve them using the **best possible data structure(s)**. Your solution must:

- ✅ Include a code implementation
- ✅ Explain your data structure decision
- ✅ Provide time and space analysis
- ✅ Optionally include supporting diagrams

**Scenarios:**

### 🛒 Inventory Lookup System
- Maintain a **product catalog**
- Allow **quick availability checks** and **frequent insertions/removals**
- Ensure **scalability** as inventory grows

### 📰 Recent Posts Feed
- Maintain the **10 most recent user posts**
- Support **constant-time insertion/removal**
- Preserve **chronological order**

### 🔁 Duplicate Detector in Stream
- Track stream of user actions
- Identify duplicates in **O(1)** average time  
- **Bonus:** Support **time-window filtering** (e.g., ignore duplicates within 5 minutes)

---

## 🪞 Part 4: Reflection & Documentation (10 Points)

Prepare a `README.md` file summarizing your assignment experience:

- 📌 List chosen tasks and their rationale
- 🧠 Reflect on **challenges and lessons learned**
- ⚖️ Discuss **trade-offs** and complexity decisions
- 🧩 Include **system or memory layout diagrams** (as needed)
- 🎥 Optional: Add a short (**max 2-minute**) video walkthrough

---

## 🧾 Evaluation Rubric

| Category                        | Points |
|---------------------------------|--------|
| Algorithm Analysis              | 30     |
| Custom Data Structures (2)      | 30     |
| Real-World Problem Solving (2)  | 20     |
| Documentation & Explanation     | 10     |
| Clarity, Code Quality, Structure| 5      |
| Creativity & Thoughtfulness     | 5      |
| **Total**                       | **100**|

---

> 💡 **Good luck!** This assignment is intended to challenge your reasoning, problem-solving, and structural thinking. Submit thoughtful and well-documented solutions that demonstrate a solid grasp of core concepts.
