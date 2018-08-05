from random import shuffle
class card:
	def __init__(self,s,r):
		self.suit = s
		self.rank = r
def getSuit():
	suit = ['Diamond','Hearts','Clubs','Spades']
	return suit

deck = []
for s in getSuit():
	for i in range(1,14):
		deck.append(card(s,i))# 52 cards in deck

def table():# generate 2 cards for each player and 5 public cards 
	shuffle(deck)
	p1 = [deck[0],deck[1]]
	p2 = [deck[2],deck[3]]
	community_card = [deck[4],deck[5],deck[6],deck[7],deck[8]]
	return [p1,p2,community_card]

def countSuit(cards): 
	res = {}
	for suit in getSuit():
		res[suit] = 0
	for c in cards:
		res[c.suit] += 1
	return res 

def countRank(cards):
	res = {}
	for rank in range(1,14):
		res[rank] = 0
	for c in cards:
		res[c.rank] += 1
	return res

def getSuitCards(cards,suit):#return a list of cards with certain suit
	res = []
	for c in cards:
		if c.suit==suit:
			res.append(c)
	return res


def printcards(cards):
	for c in cards:
		print (c.rank,c.suit)

def findRoyalFlush(cards,suit,rank):
	for s in suit:
		if(suit[s]>=5):
			cards_suit = getSuitCards(cards,s) 
			rank = countRank(cards_suit)
			if rank[1]>0 and rank[10]>0 and rank[11]>0 and rank[12]>0 and rank[13]>0:
				return True
		return False

def findStraightFlush(cards,suit):
	suit = countSuit(cards)
	for s in suit:
		if(suit[s]>=5):
			cards_suit = getSuitCards(cards,s) 
			rank = countRank(cards_suit)
			for i in range(1,10): #only find straight starts from 1 to 9
				cond = True
				for j in range(5):
					if(rank[i+j]==0):
						cond = False
						break
				if(cond):
					return True;
	return False

def findFourOfAKind(cards,rank):#return true and the rank or false and -1
	for i in rank:
		if(rank[i]==4):
			return True
	return False

def findFullHouse(cards,suit,rank):
	for i in rank:
		if(rank[i]==3):
			for j in rank:
				if(rank[j]==2):
					return True
	return False

def findFlush(cards,suit,rank):
	for s in suit:
		if(suit[s]>=5):
			return True
	return False

def findStraight(cards,suit,rank):
	for i in range(1,10): #find straight starts from 1 to 9 first
				cond = True
				for j in range(5):
					if(rank[i+j]==0):
						cond = False
						break
				if(cond):
					return True;
	if rank[1]>0 and rank[10]>0 and rank[11]>0 and rank[12]>0 and rank[13]>0: #see if straight with Ace exists
		return True
	return False

def findThreeOfAKind(cards,rank):
	for i in rank:
		if (rank[i]==3):
			return True
	return False

def findTwoPairs(cards,rank):
	for i in rank:
		if (rank[i]==2):
			for j in range(i+1,14):
				if (rank[j]==2):
					return True
	return False

def findPair(cards,rank):
	for i in rank:
		if (rank[i]==2):
			return True
	return False










def detectHandValue(cards):
	suit = countSuit(cards)
	rank = countRank(cards)
	if(findRoyalFlush(cards,suit,rank)):
		print ('Royal Flush')
		return 10
	elif(findStraightFlush(cards,suit)):
		print ('Straight Flush')
		return 9
	elif (findFourOfAKind(cards,rank)):
		print ('Four of a Kind')
		return 8
	elif (findFullHouse(cards,suit,rank)):
		print ('Full House')
		return 7
	elif (findFlush(cards,suit,rank)):
		print ('Flush')
		return 6
	elif (findStraight(cards,suit,rank)):
		print ('Straight')
		return 5
	elif (findThreeOfAKind(cards,rank)):
		print ('Three of a Kind')
		return 4
	elif (findTwoPairs(cards,rank)):
		print ('Two Pair')
		return 3
	elif(findPair(cards,rank)):
		print ('Pair')
		return 2
	else: 
		print ('High Card')
		return 1

def test_detectHandValue():
	[p1,p2,p3]=table()
	p3 += p1
	printcards(p3)
	ans = detectHandValue(p3)
	print (ans)
	return p3

# [p1,p2,community_card]=table()
card1=card('Diamond',9)
card2=card('Spades',9)
card3=card('Clubs',9)
card4=card('Hearts',9)
card5=card('Diamond',12)


cc=[card1,card3,card2,card4,card5]
detectHandValue(cc)
