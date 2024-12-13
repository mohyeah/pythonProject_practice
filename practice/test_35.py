from enum import Enum
import random

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face # 同花色比点数
        return self.suite.value < other.suite.value # 异花色比点数

class Poker:
    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0
    def shuffle(self):
        '''洗牌'''
        self.current = 0
        random.shuffle(self.cards)
    def deal(self):
        '''发牌'''
        card = self.cards[self.current]
        self.current += 1
        return card
    @property
    def has_next(self):
        '''还有没有牌可发'''
        return self.current < len(self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    def get_one(self, card):
        '''摸牌'''
        self.cards.append(card)
    def arrange(self):
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('LY'), Player('SL'), Player('ND'), Player('BG')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}:', end='')
    print(player.cards)