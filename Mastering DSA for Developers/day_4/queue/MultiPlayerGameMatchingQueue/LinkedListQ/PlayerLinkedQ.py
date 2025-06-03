from LinkedListQ.Node import Node


class PlayerLinkedQueue:
    def __init__(self, teamSize=2):
        self.front = None
        self.rear = None
        self.teamSize = teamSize
        self.count = 0

    def joinPlayer(self, player):
        newPlayer = Node(player)
        if self.isEmpty():
            self.front = self.rear = newPlayer
            self.count += 1
        else:
            self.rear.next = newPlayer
            self.rear = newPlayer
            self.count += 1

        print(f"New Player joined: {player}")
        if self.count == self.teamSize:
            self.player_match()

    def player_match(self):
        players = []
        for _ in range(self.teamSize):
            players.append(self.deQueue())

        print(f"Player Match has Created with: {players}")
        print("__" * 30)
        print('\n')

    def deQueue(self):
        if self.isEmpty():
            raise Exception("No Player found")

        player = self.front.player
        self.front = self.front.next
        self.count -= 1
        if self.front is None:
            self.rear = None
        return player

    def isEmpty(self):
        return self.front is None

    def __str__(self):
        values = []
        current = self.front
        while current:
            values.append(str(current.player))
            current = current.next

        return " -> ".join(values) if values else "TeamQueue is Empty"
