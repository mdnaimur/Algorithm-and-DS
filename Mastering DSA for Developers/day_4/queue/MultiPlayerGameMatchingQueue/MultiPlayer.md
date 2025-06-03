# Multiplayer Game Matchmaking Queue
* Implement a Queue
* Choose between Array-based or Linked List-based implementation
* Justify your choice based on complexity and memory considerations

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
        cd MultiPlayerGameMatchingQueue
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
 Arraybased Queue

Player is added: Mamun
Player is added: Naimur
Player is added: Kawsar
Matching creation ['Mamun', 'Naimur', 'Kawsar']
____________________________________________________________
Player is added: Sumon
Player is added: Parvez
******************************

LinkedList Queue

******************************
New Player joined: Bangladesh
New Player joined: Pakistan
Player Match has Created with: ['Bangladesh', 'Pakistan']
____________________________________________________________


New Player joined: India
New Player joined: Srilanka
Player Match has Created with: ['India', 'Srilanka']
____________________________________________________________


New Player joined: Nepal
New Player joined: Austrilia
Player Match has Created with: ['Nepal', 'Austrilia']
____________________________________________________________


New Player joined: England
```

### Array Based or Linked List Based Implementation which one better and why 

| Array Implementation   Queue            | Linked list Implementation    Queue       |
|:----------------------------------------|:------------------------------------------|
|Fixed size :need resize                  | Dynamic: grow as player with|
| careful to handle index                 | No need to Handle index |
| Faster than LinkedList for index        | Slightly Slow than Array |


$${\color{red}{\textbf{Complexity and Space}}}$$


| Operation | Array Queue | Linked List Queue |
|:----------|:------------|:------------------|
| EnQueue   | O(1)        | O(1)              |
| DeQueue   | O(1) **{If not circular logicO(n)}** | O(1)|
|Space Usage | O(n)       | O(n) |




