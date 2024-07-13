

def findHands(hand):
    
    ranks = []
    suits = []
    possibleHands = []

    for card in hand:
        if len(card)==2:
            rank = card[0]
            suit = card[1]
        elif len(card)==3:
            rank = card[0:2]
            suit = card[2]
        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11
        
        suits.append(suit)
        ranks.append(int(rank))

    sortedRanks = sorted(ranks)
    
    # Royal Flush , Straight Flush ,Flush
    if  suits.count(suits[0])==5:
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleHands.append(10)
        elif all(sortedRanks[i]-sortedRanks[i-1]== 1  for i in range(1,len(sortedRanks))):
            possibleHands.append(9)
        else:
            possibleHands.append(6)

    # Straight
    if all(sortedRanks[i]-sortedRanks[i-1]== 1  for i in range(1,len(sortedRanks))):
         possibleHands.append(5)

    uniqueHandValues = list(set(sortedRanks))

    # Four of a Kind , Full House
    if len(uniqueHandValues)==2:
        for val in sortedRanks:
            if sortedRanks.count(val)==4:
                possibleHands.append(8)
            elif sortedRanks.count(val)==3:
                possibleHands.append(7)

    # Three of a Kind , Two Pair
    if len(uniqueHandValues)==3:
        for val in sortedRanks:
            if sortedRanks.count(val)==3:
                possibleHands.append(4)
            elif sortedRanks.count(val)==2:
                possibleHands.append(3)
    # Pair
    if len(uniqueHandValues)==4:
        possibleHands.append(2)

    else:
        possibleHands.append(1)


    pokerHandRanks = {10:"Royal Flush",9:"Straight Flush",8:"Four of a Kind",
                      7:"Full House",6:"Flush",5:"Straight",4:"Three of a Kind",
                      3:"Two Pair",2:"Pair",1:"High Card"}
    
    # Royal Flush
    

    # print(ranks,suits)
    output = pokerHandRanks[max(possibleHands)]
    print(hand,output)
    return output


if __name__ == "__main__":
    findHands(["AH","KH","QH","JH","10H"]) # Royal Flush
    findHands(["QC","JC","10C","9C","8C"]) # Straight Flush
    findHands(["5C","5S","5H","5D","QH"]) # Four of a Kind
    findHands(["2H","2D","2S","10H","10C"]) # Full House
    findHands(["2D","KD","7D","6D","5D"]) # Flush
    findHands(["JC","10H","9C","8C","7D"]) # Straight
    findHands(["10H","10C","10D","2D","5S"]) # Three of a Kind
    findHands(["KD","KH","5C","5S","6D"]) # Two Pair
    findHands(["2D","2S","9C","KD","10C"]) # Pair
    findHands(["KD","5H","2D","10C","JH"]) # High Card
    



