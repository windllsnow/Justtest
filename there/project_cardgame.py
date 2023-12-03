import random

deck = 20
p_won_score = (deck/2)+1


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.cards = list(range(1, deck+1, 1))

        random.shuffle(self.cards)

    def picked_card(self):
        picked_card = self.cards[0]
        self.cards.remove(picked_card)
        print(f"{self.name}card is {picked_card}")
        return picked_card

    def add_point(self):
        self.points += 1
        print(f"A point has been added to {self.name}")

    def is_game_over(self):
        return len(self.cards) == 0 or self.points == p_won_score


p01 = Player(name="Player 1")
p02 = Player(name="Player 2")


print("Game start")
while True:
    input("Press enter to pick a card !\n")
    p1_card = p01.picked_card()
    p2_card = p02.picked_card()
    if p1_card > p2_card:
        p01.add_point()
    elif p2_card > p1_card:
        p02.add_point()
    else:
        print("tie!")
    if p01.is_game_over() or p02.is_game_over():
        print("game over!\n")
        if p01.points > p02.points:
            print(f"{p01.name} wins!\n")
        elif p02.points > p01.points:
            print(f"{p02.name} wins!\n")
        else:
            print(f"Score is TIE!\n")

        print(f"the final Score:{p01.points}-{p02.points}")
        break
    print(f"Score:{p01.points}-{p02.points}")
