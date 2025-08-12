class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Hand:
    def __init__(self, card_indices):
        self.card_indices = card_indices


class Game:
    def __init__(self):
        self.face_value = {str(i):i for i in range(2, 11)}
        self.face_value.update({
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 1,
            "Joker": 14 
        })
        self.deck = []
        self.hands = []

    def add_card(self, suit: str, value: str) -> None:
        self.deck.append(Card(suit, value))

    def card_string(self, card: int) -> str:
        card_val = self.deck[card].value
        card_suit = self.deck[card].suit
        if card_val == "Joker":
            return f"{card_suit} {card_val}"
        else:
            return f"{card_val} of {card_suit}"

    def card_beats(self, card_a: int, card_b: int) -> bool:
        val_a = self.face_value[self.deck[card_a].value]
        val_b = self.face_value[self.deck[card_b].value]
        return val_a > val_b

    def add_joker(self, color: str) -> None:
        self.deck.append(Card(color, "Joker"))
        
    def add_hand(self, card_indices):
        self.hands.append(Hand(card_indices))
    
    def hand_string(self, hand: int) -> str:
        card_indices = self.hands[hand].card_indices
        htxt = ", ".join(self.card_string(idx) for idx in card_indices)
        return htxt

    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        a_cards = self.hands[hand_a].card_indices
        b_cards = self.hands[hand_b].card_indices
        hand_a_vals = [self.face_value[self.deck[card].value] for card in a_cards]
        hand_b_vals = [self.face_value[self.deck[card].value] for card in b_cards]
        hand_a_vals.sort(reverse=True)
        hand_b_vals.sort(reverse=True)
        smaller_hand = min(len(a_cards), len(b_cards))
        for i in range(0, smaller_hand):
            if hand_a_vals[i] > hand_b_vals[i]:
                return True
        return False

if __name__ == "__main__":
    game = Game()
    suit, value = "Spades 3".split()
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = "Hearts K".split()
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
