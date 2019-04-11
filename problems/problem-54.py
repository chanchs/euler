import math
import time
import lib.utilities as ut
import collections


class Card:
    def __init__(self, v, s):
        self.suite = s
        self.value = v

    def card(self):
        return self.value, self.suite


class Hand:

    def __init__(self, c):
        self.cards = []
        self.hand = c
        for crd_str in c:
            self.cards.append(Card(self.convert_to_value(crd_str), self.get_suite(crd_str)))
        self.hand_rank = self.rank()

    def get_suite(self, c):
        return c[1:]

    def get_hand(self):
        return self.hand

    def convert_to_value(self, c):
        temp = c[:1]
        # Ace is 14
        if temp is "T":
            return 10
        elif temp is "J":
            return 11
        elif temp is "Q":
            return 12
        elif temp is "K":
            return 13
        elif temp is "A":
            return 14
        else:
            return int(temp)

    def rank(self):
        r = []

        if self.is_royal_flush():
            r.append("Royal Flush")
            r.append(9)
            return r

        straight_flush = self.is_straight_flush()
        if straight_flush[0] > -1:
            r.append("Straight Flush")
            r.append(8)
            r.append(straight_flush)
            return r

        four_of_a_kind = self.is_four_of_a_kind()
        if four_of_a_kind[0] > 0 and four_of_a_kind[1] > 0:
            r.append("Four of a kind")
            r.append(7)
            r.append(four_of_a_kind)
            return r

        full_house = self.is_full_house()
        if full_house[0] > 0 and full_house[1] > 0:
            r.append("Full House")
            r.append(6)
            r.append(full_house)
            return r

        flush = self.is_flush()
        if flush[0] > 0:
            r.append("Flush")
            r.append(5)
            r.append(flush)
            return r

        straight = self.is_straight()
        if straight[0] > -1:
            r.append("Straight")
            r.append(4)
            r.append(straight)
            return r

        three_of_a_kind = self.is_three_of_a_kind()
        if three_of_a_kind[0] > 0:
            if three_of_a_kind[1] == three_of_a_kind[2]:
                r.append("Three of a kind with pair")
                r.append(3)
                r.append(three_of_a_kind)
            else:
                r.append("Three of a kind with high card")
                r.append(3)
                r.append(three_of_a_kind)
            return r

        two_pairs = self.is_two_pairs()
        if two_pairs[0] > 0 and two_pairs[1] > 0 and two_pairs[2] > 0:
            r.append("Two Pairs")
            r.append(2)
            r.append(two_pairs)
            return r

        one_pair = self.is_one_pair()
        if one_pair[0] > 0:
            r.append("One Pair")
            r.append(1)
            r.append(one_pair)
            return r

        high_card = self.high_card()
        if high_card[0] > 0:
            r.append("High Card")
            r.append(0)
            r.append(high_card)
            return r

        r.append("Error")
        return r

    def is_royal_flush(self):
        if self.is_same_suite() is False:
            return False
        else:
            v = []
            for c in self.cards:
                v.append(c.value)
            v.sort()
            if v[0] == 10 and v[1] == 11 and v[2] == 12 and v[3] == 13 and v[4] == 14:
                return True
        return False

    def is_straight_flush(self):
        result = [-1] * 5
        if self.is_same_suite() is False:
            return result
        else:
            v = []
            for c in self.cards:
                v.append(c.value)
            v.sort()
            if v[0] == v[1] - 1 and v[1] == v[2] - 1 and v[2] == v[3] - 1 and v[3] == v[4] - 1:
                result = v[::-1]
        return result

    def is_four_of_a_kind(self):
        v = []
        result = [-1] * 2
        for c in self.cards:
            v.append(c.value)
        v.sort()
        if v[0] == v[1] and v[1] == v[2] and v[2] == v[3]:
            result[0] = v[0]
            result[1] = v[4]
        elif v[1] == v[2] and v[2] == v[3] and v[3] == v[4]:
            result[0] = v[1]
            result[1] = v[0]
        return result

    def is_full_house(self):
        v = []
        result = [-1] * 2
        for c in self.cards:
            v.append(c.value)
        v.sort()
        if v[0] == v[1] and v[1] == v[2]:
            if v[3] == v[4]:
                result[0] = v[0]
                result[1] = v[3]
        elif v[1] == v[2] and v[2] == v[3]:
            if v[0] == v[4]:
                result[0] = v[1]
                result[1] = v[0]
        elif v[2] == v[3] and v[3] == v[4]:
            if v[0] == v[1]:
                result[0] = v[2]
                result[1] = v[0]
        return result

    def is_flush(self):
        result = [-1] * 5
        if self.is_same_suite():
            return self.high_card()
        else:
            return result

    def is_straight(self):
        result = [-1] * 5
        if self.is_same_suite():
            return result
        else:
            v = []
            for c in self.cards:
                v.append(c.value)
            v.sort()
            if v[0] == v[1] - 1 and v[1] == v[2] - 1 and v[2] == v[3] - 1 and v[3] == v[4] - 1:
                result = v[::-1]
        return result

    def is_three_of_a_kind(self):
        v = []
        result = [-1] * 3
        for c in self.cards:
            v.append(c.value)
        v.sort()
        if v[0] == v[1] and v[1] == v[2]:
            result[0] = v[0]
            result[1] = v[4]
            result[2] = v[3]
        elif v[1] == v[2] and v[2] == v[3]:
            result[0] = v[1]
            result[1] = v[4]
            result[2] = v[0]
        elif v[2] == v[3] and v[3] == v[4]:
            result[0] = v[2]
            result[1] = v[1]
            result[2] = v[0]
        return result

    def is_two_pairs(self):
        result = [-1] * 3
        v = []
        for c in self.cards:
            v.append(c.value)
        v.sort()
        seen = {}
        dupes = []
        for x in v:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1

        if len(dupes) == 2:
            result = dupes + list(set(v) - set(dupes))[::-1]
        return result

    def is_one_pair(self):
        v = []
        for c in self.cards:
            v.append(c.value)
        v.sort()
        result = [-1] * 5
        seen = {}
        dupes = []
        for x in v:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
        if len(dupes) == 1:
            result = list(set(v) - set(dupes))
            result.sort(reverse=True)
            result = dupes + result
        return result

    def high_card(self):
        v = []
        for c in self.cards:
            v.append(c.value)
        v.sort()
        result = v[::-1]
        return result

    def is_same_suite(self):
        crd = self.cards[0]
        for i in range(1, len(self.cards)):
            c1 = self.cards[i]
            if crd.suite != c1.suite:
                return False
        return True


def compare_four_of_a_kind(h1, h2):
    if h1[0] > h2[0]:
        return "player1"
    elif h2[0] > h1[0]:
        return "player2"
    elif h1[0] == h2[0]:
        if h1[1] > h2[1]:
            return "player1"
        elif h2[1] > h1[2]:
            return "player2"
        elif h1[1] == h2[1]:
            return "Draw!"
    return ""


def compare_full_house(h1, h2):
    if h1[0] > h2[0]:
        return "player1"
    elif h2[0] > h1[0]:
        return "player2"
    elif h1[0] == h2[0]:
        if h1[1] > h2[1]:
            return "player1"
        elif h2[1] > h1[1]:
            return "player2"
        elif h1[1] == h2[1]:
            return "Draw!"
    return ""


def compare_three_of_a_kind(h1, h2):
    if h1[0] > h2[0]:
        return "player1"
    elif h2[0] > h1[0]:
        return "player2"
    elif h1[0] == h2[0]:
        if h1[1] > h2[1]:
            return "player1"
        elif h2[1] > h1[1]:
            return "player2"
        elif h1[1] == h2[1]:
            if h1[1] > h2[2]:
                return "player1"
            elif h2[2] > h1[2]:
                return "player2"
            elif h1[2] == h2[2]:
                return "Draw"
    return ""


def compare_two_pairs(h1, h2):
    if h1[0] > h2[0] and h1[1] > h2[1]:
        return "player1"
    elif h2[0] > h1[0] and h2[1] > h1[1]:
        return "player2"
    elif h1[0] > h2[0] and h2[1] > h1[1]:
        if h1[2] > h2[2]:
            return "player1"
        elif h2[2] > h1[2]:
            return "player2"
    elif h2[0] > h1[0] and h1[1] > h2[1]:
        if h1[2] > h2[2]:
            return "player1"
        elif h2[2] > h1[2]:
            return "player2"
    elif h1[0] == h2[0] and h1[1] > h2[1]:
        return "player1"
    elif h1[0] > h2[0] and h1[1] == h2[1]:
        return "player1"
    elif h1[0] == h2[0] and h2[1] > h1[1]:
        "player2"
    elif h2[0] > h1[0] and h1[1] == h2[1]:
        return "player2"
    elif h1[0] == h2[0] and h1[1] == h2[1]:
        if h1[2] > h2[2]:
            return "player1"
        elif h2[2] > h1[2]:
            return "player2"
        elif h1[2] == h2[2]:
            return "Draw"
    return ""


def compare_high_card(h1, h2):
    for i in range(len(h1)):
        if h1[i] > h2[i]:
            return "player1"
        elif h2[i] > h1[i]:
            return "player2"
    return "Draw"


def compare_one_pair(h1, h2):
    if h1[0] > h2[0]:
        return "player1"
    elif h2[0] > h1[0]:
        return "player2"
    elif h1[0] == h2[0]:
        return compare_high_card(h1[1:], h2[1:])
    return ""


def compare_straight(h1, h2):
    return compare_high_card(h1, h2)


def compare_flush(h1, h2):
    return compare_high_card(h1, h2)


def compare_straight_flush(h1, h2):
    return compare_high_card(h1, h2)


def winner(p1, p2):
    if p1.hand_rank[1] > p2.hand_rank[1]:
        #print(p1.hand_rank[0])
        return "player1"
    elif p2.hand_rank[1] > p1.hand_rank[1]:
        #print(p2.hand_rank[0])
        return "player2"
    elif p1.hand_rank[1] == p2.hand_rank[1]:
        #print(p1.hand_rank[0])
        if p1.hand_rank[1] == 8:
            return compare_straight_flush(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 7:
            return compare_four_of_a_kind(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 6:
            return compare_full_house(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 5:
            return compare_flush(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 4:
            return compare_straight(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 3:
            return compare_three_of_a_kind(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 2:
            return compare_two_pairs(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 1:
            return compare_one_pair(p1.hand_rank[2], p2.hand_rank[2])
        elif p1.hand_rank[1] == 0:
            return compare_high_card(p1.hand_rank[2], p2.hand_rank[2])
    return "player1"


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    f = open("problem-54.txt")

    c = []
    player1_win_count = 0
    for line in f:
        ln = line.split()
        player1 = Hand([ln[0], ln[1], ln[2], ln[3], ln[4]])
        player2 = Hand([ln[5], ln[6], ln[7], ln[8], ln[9]])

        w = winner(player1, player2)

        if w == "player1":
            player1_win_count += 1
            print("player 1 {0} :: player 2 {1} :: winner : {2} :: rank {3} :: {4}".format(player1.get_hand(),
                                                                                           player2.get_hand(),
                                                                                           w,
                                                                                           player1.rank(),
                                                                                           player2.rank()))
            #print("{0} :: {1}".format(player1.rank(),
            #                          player2.rank()))
    f.close()
    print("Player 1 wins : {}".format(player1_win_count))

    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))