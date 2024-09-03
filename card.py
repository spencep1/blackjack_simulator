import random

class Card:
    suit_str = ["♠", "♡", "♢", "♣"]    
    rank_str = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.show = False
        
    def __str__(self):
        if self.show:
            return self.suit_str[self.suit] + self.rank_str[self.rank]
        else:
            return "[]"
        
    def set_show(self):
        self.show = True
        
class Deck:
    def __init__(self):
        self.deck = []
        
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        rtn_string = ""
        for i in range(len(self.deck)):
            rtn_string = rtn_string + self.deck[i].__str__() + " "
        rtn_string = rtn_string + "\n"
        return rtn_string
    
    def shuffle(self):
        new_deck = []
        
        card_num = len(self.deck)
        for i in range(card_num):
            remove_index = random.randint(0, len(self.deck)-1)
            
            new_deck.append(self.deck[remove_index])
            self.deck.pop(remove_index)
        self.deck = new_deck
    
    def draw_one(self):
        return self.deck.pop(0)  
        
class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        i = 0
        while i < len(self.cards) and card.rank > self.cards[i].rank:
            i = i + 1
            
        self.cards.insert(i, card)        
    
    def hand_total(self):
        total = 0
        for i in range(len(self.cards)-1, -1, -1):
            if self.cards[i].rank == 0:
                num_aces = i+1
                
                num_eleven = num_aces
                while num_eleven*11 + total > 21:
                    num_eleven = num_eleven - 1
                total = total + num_eleven*11 + (num_aces-num_eleven)
                break
            elif self.cards[i].rank >= 9:
                total = total + 10
            else:
                total = total + (self.cards[i].rank + 1)           
        return total
    
    def __str__(self):
        rtn_string = ""
        for i in range(len(self.cards)):
            rtn_string = rtn_string + self.cards[i].__str__() + " "
            
        return rtn_string    
    
  
