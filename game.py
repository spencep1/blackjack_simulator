import card

class Game:
    def __init__(self, num_players):
        
        self.players = []
        for i in range(num_players):
            self.players.append(Player())
            
        self.deck = card.Deck()
        self.deck.shuffle()
        self.dealer = card.Hand()
        
    def display_cards(self, dealer_score):
        print("dealer:", self.dealer, end = "")
        if dealer_score:
            print("", self.dealer.hand_total())
        else:
            print("")
        
        for i in range(len(self.players)):
            print("player " + str(i) + ":", self.players[i].hand, self.players[i].get_total())    
    
    def deal_cards(self):
        self.dealer.add_card(self.deck.draw_one())
        
        for i in range(len(self.players)):
            card_to_add = self.deck.draw_one()
            card_to_add.set_show()
            self.players[i].add_card(card_to_add)
        print("cards dealt")
        
        self.display_cards(False)
    
    def take_turns(self):
        num_players = len(self.players)
        
        while num_players > 0:
            for i in range(len(self.players)):
                if not self.players[i].waiting:
                    print("Player", i, end = " ")
                    player_move = self.players[i].take_turn(self.dealer)
                    if player_move == "stand":
                        self.players[i].lock_in_hand()
                        num_players = num_players - 1
                    else:
                        new_card = self.deck.draw_one()
                        new_card.set_show()
                        self.players[i].add_card(new_card)
                        if self.players[i].get_total() >= 21:
                            print("card values or reach 21")
                            self.players[i].lock_in_hand()
                            num_players = num_players - 1
            self.display_cards(False)
        
    def end_game(self):
        self.dealer.cards[0].set_show()
        total_draws = 0
        while self.dealer.hand_total() < 17:
            card_to_add = self.deck.draw_one()
            card_to_add.set_show()
            self.dealer.add_card(card_to_add)            
            total_draws = total_draws + 1
            
        print("dealer draws", total_draws, "cards")
        print("dealer:", self.dealer, self.dealer.hand_total(), end = "")   
        
        
        for i in range(len(self.players)):
            if self.players[i].get_total() > 21:
                print("player", i, "loses")
            elif self.players[i].get_total() == 21:
                print("player", i, "wins")
            else:
                if self.dealer.hand_total() > 21:
                    print("player", i, "wins")
                else:
                    if self.dealer.hand_total() > self.players[i].get_total():
                        print("player", i, "loses")
                    else:
                        print("player", i, "wins")                        
                        
class Player:
    def __init__(self):
        self.hand = card.Hand()
        self.waiting = False
        
    def lock_in_hand(self):
        self.waiting = True
        
    def add_card(self, card):
        self.hand.add_card(card)
        
    def get_total(self):
        return self.hand.hand_total()
    
    def take_turn(self, dealer_hand):
        turn_move = input("Stand or Hit: ")
        turn_move.strip()
        turn_move.lower()
        while turn_move != "stand" and turn_move != "hit":
            turn_move = input("Please enter stand or hit: ")
            turn_move.strip()
            turn_move.lower()  
        return turn_move
        
    