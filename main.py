from card import Card


cards = []
dictionary = {}

def readFile():
    lable = 1
    with open("F:\\data.txt","r") as file:
       for line in file:
           items = line.rstrip("\n").split(" ")
           items.append(lable)
           cards.append(Card(items))
           lable += 1

    for card in cards:
        list = []
        for c in cards:
            if(card.isCollage(c)):
                list.append(c)
        dictionary[card.lable] = list

def BFSRight(header):
    listResult = [header]
    while header != 0:
        list = dictionary.get(header.lable)
        for card in list:
            if (header.isRight(card)):
                listResult.append(card)
                header = card
                break
        else:
            header = 0

    for card in listResult:
        print(card.lable, end=" ")
    print()

def BFSDown(header):
    listResult = [header]
    while header != 0:
        list = dictionary.get(header.lable)
        for card in list:
            if (header.isBottom(card)):
                listResult.append(card)
                header = card
                break
        else:
            header = 0

    for card in listResult:
        list = dictionary.get(card.lable)
        for c in list:
            if(card.isLeft(c)):
                print("Khong thuc hien duoc")
                return

    for card in listResult:
        BFSRight(card)

def printSol():
    keys = dictionary.keys()
    for key in keys:
        values = dictionary.get(key)
        if(len(values) < 2):
            print("Khong thuc hien duoc")
            return

    first = 0
    for card in cards:
        isFirst = 0
        for i in range(4):
            if (card.left == 0 and card.top == 0):
                first = card
                isFirst = 1
                break
            card.turn()
        if (isFirst):
            break
    BFSDown(first)


def main():
    readFile()
    printSol()

if __name__ == '__main__':
    main()