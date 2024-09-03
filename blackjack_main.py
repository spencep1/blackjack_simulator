import card
import game

def main():
    play_game = game.Game(2)
    play_game.deal_cards()
    play_game.take_turns()
    play_game.end_game()
   
   
if __name__ == "__main__":
    main()
