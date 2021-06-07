from random import shuffle
from matplotlib import pyplot as plt

ranks = 'Ace King Queen Jack 10 9 8 7 6 5 4 3 2'.split(' ')
suits = 'Heart Diamond Spade Club'.split(' ')

cards = [(j+'_of_'+i) for i in suits for j in ranks]

shuffle(cards)
shuffle(cards)
shuffle(cards)
shuffle(cards)
shuffle(cards)
shuffle(cards)

deck1 = cards[0:int(len(cards)/2)]
deck2 = cards[int(len(cards)/2):]

class player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def pull_cards(self):
        try:
            card = self.deck.pop(0)
            return card
        except:
            return None

    def add_cards(self, cards):
        self.deck.extend(cards)

    def show_deck(self):
        print(self.deck)


class game:
    def __init__(self):
        pass
    def both_pull_cards(self, p1, p2):
        card1 = p1.pull_cards()
        card2 = p2.pull_cards()
        return card1, card2
    def both_pull_war_cards(self, p1, p2):
        war_cards = []
        war_cards.extend(self.both_pull_cards(p1, p2))
        war_cards.extend(self.both_pull_cards(p1, p2))
        war_cards.extend(self.both_pull_cards(p1, p2))
        return war_cards
    def compare_cards(self, card1, card2):
        if card1 == None or card2==None:
            return None
        else: 
            print('Comparing: ', card1, '   ',card2)
            card1 = card1.split('_of_')[0]
            card2 = card2.split('_of_')[0]
            
            d = {'Ace':14, 'King':13, 'Queen':12, 'Jack':11}

            if (card1) in d:
                card1 = d[card1]
            if (card2) in d:
                card2 = d[card2]   

            if int(card1)>int(card2):
                return 'Player 1 won round!!'
            elif int(card1)==int(card2):
                return 'Draw!!'
            else:
                return 'Player 2 won round!!'

    def pull_and_compare(self, p1, p2):
        card1, card2 = self.both_pull_cards(p1,p2)
        res = self.compare_cards(card1, card2)
        return res, card1, card2

    def on_table_cards(self):
        count=0
        for i in cards_on_table:
            if i != None:
                count+=1
        return count
p1 = player('Player1',deck1)
p2 = player('Player2',deck2)

g = game()
round = 1
cards_on_table = []
p1_len_hist = []
p2_len_hist = []

while(1):
    print('---------------------------------------')
    print('Round: ',round)
    round=round+1
    p1_len_hist.append(len(p1.deck))
    p2_len_hist.append(len(p2.deck))
    print('Deck sizes:  ', len(p1.deck), '   ', len(p2.deck))
    
    res, card1, card2 = g.pull_and_compare(p1,p2)
    if res == None:
        if len(p1.deck)>len(p2.deck):
            print('On Table: ', g.on_table_cards())
            print('>>>>>>>>>>>>>>  Player 1 Won The Game!!  <<<<<<<<<<<<<<<<')
        else:
            print('On Table: ', g.on_table_cards())
            print('>>>>>>>>>>>>>>  Player 2 Won The Game!!  <<<<<<<<<<<<<<<<')
        break
    else:
        cards_on_table.extend([card1, card2])
        print(res)
        
        if res == 'Player 1 won round!!':
            p1.add_cards(cards_on_table)
            cards_on_table.clear()

        elif res == 'Player 2 won round!!':
            p2.add_cards(cards_on_table)
            cards_on_table.clear()
        
        elif res == 'Draw!!':
            war_cards = g.both_pull_war_cards(p1, p2)
            cards_on_table.extend(war_cards)
plt.figure(figsize=(12,5))
plt.plot(p1_len_hist, label='Player 1')
plt.plot(p2_len_hist, label='Player 2')
plt.legend(loc='upper right')
plt.show()