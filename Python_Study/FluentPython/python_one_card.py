from collections import namedtuple
from random import choice
from typing import List, Union, Dict


Card: namedtuple = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks: List[str] = [str(card_number) for card_number in range(2, 11)] + list("JQKA")
    suits: List[str] = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position: str) -> Union[str, int]:
        return self._cards[position]


def spades_high(card: namedtuple) -> namedtuple:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    

if __name__ == "__main__":
    beer_card = Card("7", "diamonds")
    
    print(beer_card)

    deck: FrenchDeck = FrenchDeck()
    print(f"cards: {len(deck)}")

    # getitem by position number indexing
    print(f"index 0: {deck[0]}")
    print(f"index -1: {deck[-1]}")

    # getitem using random value
    for _ in range(1, 4):
        print(f"{_}st random value: {choice(deck)}")

    # magic methods(__getitem__) to slicing
    print(f"slicing: {deck[:3]}")
    print(f"slicing and use step: {deck[12::13]}")

    # magic method to loop
    print([card for card in deck])

    print([card for card in reversed(deck)])

    # if do not implement contains method
    print(f"is heart Q card exists : {Card('Q', 'hearts') in deck}")
    print(f"is beasts 7 card exists : {Card('7', 'beasts') in deck}")

    # sorting values
    suit_values: Dict[str, int] = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    for card in sorted(deck, key=spades_high):
        print(card)