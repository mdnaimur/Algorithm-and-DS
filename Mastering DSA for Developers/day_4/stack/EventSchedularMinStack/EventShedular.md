# Event Scheduler with Min Stack
* Build a Min Stack supporting getMin() operation in O(1)
* Explain why a Stack is more suitable than alternative data structures

---


## Setup Instruction
1. **clone the repository**
   ``` bash
   git clone https://github.com/mdnaimur/mastering-dsa-for-developers.git

   ```
      ``` bash
   git checkout real_world

   ```
    ``` bash
        inside dsa_real_life
        Part_1-Real-World/
        cd EventSchedularMinStack
    ```

2. **Run App**
   
   ``` bash
   docker-compose up --build

   ```
3. **Without Docker** 
    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate 
    ```


    **On macOS/Linux:**
    ``` bash
    source venv/bin/activate
    ```
    ```bash
    pip install -r requirements.txt

    ```
    **Run**
    ```bahs
    python main.py

    ```

---

**Output**

``` bash
Main Stack(top to bottom): [28, 2, 32, 5]
Min Stack(Top to Bottom): [2, 2, 5, 5]
Current min:2

main peek: 28
min:  2
Main Stack(top to bottom): [2, 32, 5]
Min Stack(Top to Bottom): [2, 5, 5]
Current min:2

main peek: 2
min:  2
Main Stack(top to bottom): [32, 5]
Min Stack(Top to Bottom): [5, 5]
Current min:5

main peek: 32
min:  5
Main Stack(top to bottom): [5]
Min Stack(Top to Bottom): [5]
Current min:5

main peek: 5
min:  5
Main Stack(top to bottom): [5]
Min Stack(Top to Bottom): [5]
Current min:5
```