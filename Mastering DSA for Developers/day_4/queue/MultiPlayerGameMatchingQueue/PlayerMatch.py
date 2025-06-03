class PlayerMatch:
    def __init__(self, teamSize=2):
        self.playerQueue = [None] * teamSize
        self.playerMatchSize = teamSize
        self.front = 0
        self.rear = 0
        self.count = 0
        # self.playerMatchCreation = [None] * teamSize
        # self.plyerCount = 0

    def joinQueue(self, player):
        if self.isFull():
            raise Exception("Team Full")

        self.playerQueue[self.rear] = player
        self.rear = (self.rear + 1) % self.playerMatchSize
        self.count += 1
        print(f"Player is added: {player}")
        # print("len check", len(self.playerQueue))
        # check len while teamsize pop and make player Match
        if self.count == self.playerMatchSize:
            self.player_match()

    def player_match(self):
        match_player = []
        for _ in range(self.playerMatchSize):
            player = self.deQueue()
            # self.playerMatchCreation[self.plyerCount] = player
            # self.plyerCount += 1
            match_player.append(player)
        print("Matching creation", match_player)
        print("__" * 30)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("No player found....")

        player = self.playerQueue[self.front]
        self.playerQueue[self.front] = None  # Optonal:for understand
        self.front = (self.front + 1) % self.playerMatchSize
        self.count -= 1
        # print(f"[deQueue] Player: {player}")
        return player

    def isFull(self):
        return self.count == self.playerMatchSize

    def isEmpty(self):
        # print(f"[check emty front == rear] = {self.front} = {self.rear}")
        return self.count == 0

    def __str__(self):
        if self.isEmpty():
            return "No player found"

        result = []
        index = self.front
        for _ in range(self.count):
            result.append(str(self.playerQueue[index]))
            index = (index + 1) % self.playerMatchSize
        return str(result)
        # return " (Players) <-".join(result)
