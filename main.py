from random import shuffle
class card:
	def __init__(self,s,r):
		self.suit = s
		self.rank = r

suit = ['Diamond','Hearts','Clubs','Spades']
deck = []
for s in suit:
	for i in range(1,14):
		deck.append(card(s,i))# 52 cards in deck

def table():# generate 2 cards for each player and 5 public cards 
	shuffle(deck)
	p1 = [deck[0],deck[1]]
	p2 = [deck[2],deck[3]]
	community_card = [deck[4],deck[5],deck[6],deck[7],deck[8]]
	return [p1,p2,community_card]



def findRoyalFlush(cards):
	cards.sort(key=lambda x: x.rank)
	if (cards[0].rank==1 and cards[1].rank==10 and cards[2].rank==11 and cards[3].rank==12 and cards[4].rank==13):
		if (cards[0].suit==cards[1].suit==cards[2].suit==cards[3].suit==cards[4].suit):
			return True
	return False

def printcards(cards):
	for c in cards:
		print (c.rank,c.suit)


[p1,p2,community_card]=table()
card1=card('Diamond',1)
card2=card('Diamond',10)
card3=card('Diamond',11)
card4=card('Diamond',13)
card5=card('Diamond',12)


cc=[card1,card3,card2,card4,card5]
if(findRoyalFlush(cc)):
	print ('Found')
else:
	print ('Not Found')




'''
def detectHandValue(cards):
	if(findRoyalFlush(cards)):
		return 10
	elseif(findStraightFlush(cards)):
		return 9
	elseif (findFourOfAKind(cards)):
		return 8
	elseif (findFullHouse(cards)):
		return 7
	elseif (findFlush(cards)):
		return 6
	elseif (findStraight(cards)):
		return 5
	elseif (findThreeOfAKind(cards)):
		return 4
	elseif (findTwoPairs(cards)):
		return 3
	elseif(findPair(cards)):
		return 2
	else 
		return 1
'''