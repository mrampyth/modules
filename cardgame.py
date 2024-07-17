import random
from colorama import Fore
from colorama import Style

suits = ["♣", f"{Fore.RED}♦", f"{Fore.RED}♥", "♠"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
used_cards = []

player_score = 0
comp_score = 0
playing = True
roun = 1


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __str__(self):
        return f"{suits[self.suit]} {numbers[self.number]} {Style.RESET_ALL}"


def rand_card():
    generating = True
    
    while generating:
        new_suit = random.randrange(0, len(suits))
        new_number = random.randrange(0, len(numbers))
        new_card = Card(new_suit, new_number)
        
        if not str(new_card) in used_cards:
            generating = False
    
    return Card(new_suit, new_number)


print(f"{Fore.YELLOW}~ WELCOME TO CARDGAME! ~{Style.RESET_ALL}\n")
print("The rules are simple. You must pick a card. The player with the most valuable suit wins. If both players have the same suit, the more valuable number wins. When a player wins, they get 1 point. If both players have the exact same card, it's a tie. The first player to 5 points wins the game.\n")
print("Numbers (Worst to Best): 2 through 10, J, Q, K, and A.") 
print("Suits (Worst to Best): ♣, ♦, ♥, and ♠.\n")
input("Press ENTER to begin! \n")


while playing:
    player_card = rand_card()
    used_cards.append(str(player_card))
    
    comp_card = rand_card()
    used_cards.append(str(comp_card))
    
    print(f"{Fore.YELLOW}~ ROUND {str(roun)} ~{Style.RESET_ALL}\n")
    
    print("Player One's Card: " + str(player_card))
    print("Player Two's Card: " + str(comp_card))
    
    player_msg = f"{Fore.GREEN}~ PLAYER ONE WINS 1 POINT! ~{Style.RESET_ALL} \n"
    comp_msg = f"{Fore.RED}~ PLAYER TWO WINS 1 POINT! ~{Style.RESET_ALL} \n"
    
    if player_card.suit > comp_card.suit:
        print(player_msg)
        player_score += 1
    elif player_card.suit < comp_card.suit:
        print(comp_msg)
        comp_score += 1
    elif player_card.number > comp_card.number:
        print(player_msg)
        player_score += 1
    elif player_card.number < comp_card.number:
        print(comp_msg)
        comp_score += 1
    else:
        print(f"{Fore.YELLOW}~ TIE! GO AGAIN! ~{Style.RESET_ALL} \n")
    
    used_card_string = ""
    for card in used_cards:
        used_card_string += str(card) + " "
    
    print("Used Cards: " + used_card_string)
    print("Player One's Score: " + str(player_score))
    print("Player Two's Score: " + str(comp_score) + "\n")
    
    if player_score >= 5:
        print(f"{Fore.GREEN}~ PLAYER ONE WINS! ~{Style.RESET_ALL}")
        playing = False
    elif comp_score >= 5:
        print(f"{Fore.RED}~ PLAYER TWO WINS! ~{Style.RESET_ALL}")
        playing = False
    else:
        input("Press ENTER for the next round!\n")
        roun += 1



