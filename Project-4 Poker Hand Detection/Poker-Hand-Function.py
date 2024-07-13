

def findHands(hand):
    
    ranks = []
    suits = []

    for card in hand:
        if len(card)==2:
            rank = card[0]
            suit = card[1]
        elif len(card)==3:
            rank = card[0:2]
            suit = card[2]
        ranks.append(rank)
        suits.append(suit)

    print(ranks,suits)
    return 0


if __name__ == "__main__":
    findHands(["AH","KH","QH","JH","10H"])#Royal Flush
    findHands(["QC","JC","10C","9C","8C"])#Stright Flush

