class Card:


    def __init__(self, list):
        self.right = int(list[0])
        self.top = int(list[1])
        self.left = int(list[2])
        self.bottom = int(list[3])
        self.lable = int(list[4])

    def __str__(self):
        return "card[right={0}, top={1}, left={2}, botttom={3}, lable={4}]".format(self.right, self.top, self.left, self.bottom, self.lable)

    def isCollage(self,card):
        for i in range(4):
            if(self.right == card.left and self.right != 0):
                return 1
            elif(self.top == card.bottom and self.top != 0):
                return 1
            elif(self.left == card.right and self.left != 0):
                return 1
            elif(self.bottom == card.top and self.bottom != 0):
                return 1
            card.turn()
        return 0

    def turn(self):
        temp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp

    def isRight(self, card):
        for i in range(4):
            if(self.right == card.left and card.left != 0):
                return 1
            card.turn()
        return 0

    def isLeft(self, card):
        for i in range(4):
            if(self.left == card.right and card.right != 0):
                return 1
            card.turn()
        return 0

    def isBottom(self, card):
        for i in range(4):
            if (self.bottom == card.top and card.top != 0):
                return 1
            card.turn()
        return 0