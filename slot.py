import random
import time

h = ["A", "B", "C", "D"]

def main():
    money = 0
    depo = int(input("Deposit amount: "))
    money += depo

    while True:
        play = input("Press enter to play, (q) to quit: ").lower()
        if play == "":
            money = mon(money)

        elif play == "q":
            print(f"You left with ${money}")
            break
        else:
            pass

def mon(money):
    while True:
        line = int(input("Enter the number of lines to bet on: "))
        if line <= 3 and line >= 1:
            break
        else:
            pass
    betamo = int(input("Enter the amount you would like bet: "))
    bet = line*betamo
    if money < bet:
        print("Not enough funds.")
    else:
        print(f"You are betting ${betamo} in {line} lines. Total bet is equal to: ${bet}.")
        money, betamo, line, bet = slot(money, betamo, line, bet)
        print(f"Balance: {money}")
        return money

def slot(money, betamo, line, bet):
    money -= bet
    h = ["A", "B", "C", "D"]
    win = 0
    a1 = random.choice(h)
    b2 = random.choice(h)
    c3 = random.choice(h)
    d4 = random.choice(h)
    e5 = random.choice(h)
    f6 = random.choice(h)
    g7 = random.choice(h)
    h8 = random.choice(h)
    i9 = random.choice(h)
    if line == 1:
        time.sleep(1)
        print(f"|{a1}|{b2}|{c3}|")
        if a1 == b2 == c3 == "D":
            win += betamo * 2
        elif a1 == b2 == c3 == "C":
            win += betamo * 3

        elif a1 == b2 == c3 == "B":
            win += betamo * 4
        elif a1 == b2 == c3 == "A":
            win += betamo * 5

    if line == 2:
        time.sleep(1)
        print(f"|{a1}|{b2}|{c3}|")
        print(f"|{d4}|{e5}|{f6}|")
        if a1 == b2 == c3 == "C":
            win += betamo * 3
        if d4 == e5 == f6 == "C":
            win += betamo * 3
        if a1 == b2 == c3 == "D":
            win += betamo * 2
        if d4 == e5 == f6 == "D":
            win += betamo * 2
        if a1 == b2 == c3 == "B":
            win += betamo * 4
        if d4 == e5 == f6 == "B":
            win += betamo * 4
        if a1 == b2 == c3 == "A":
            win += betamo * 5
        if d4 == e5 == f6 == "A":
            win += betamo * 5

    if line == 3:
        time.sleep(1)
        print(f"|{a1}|{b2}|{c3}|")
        print(f"|{d4}|{e5}|{f6}|")
        print(f"|{g7}|{h8}|{i9}|")
        if a1 == b2 == c3 == "D":
            win += betamo * 2
        if d4 == e5 == f6 == "D":
            win += betamo * 2
        if g7 == h8 == i9 == "D":
            win += betamo * 2
        if a1 == b2 == c3 == "C":
            win += betamo * 3
        if d4 == e5 == f6 == "C":
            win += betamo * 3
        if g7 == h8 == i9 == "C":
            win += betamo * 3
        if a1 == b2 == c3 == "B":
            win += betamo * 4
        if d4 == e5 == f6 == "B":
            win += betamo * 4
        if g7 == h8 == i9 == "B":
            win += betamo * 4
        if a1 == b2 == c3 == "A":
            win += betamo * 5
        if d4 == e5 == f6 == "A":
            win += betamo * 5
        if g7 == h8 == i9 == "A":
            win += betamo * 5
    time.sleep(1)
    print(f"you win ${win}")
    money += win
    return money, betamo, line, bet
if __name__ == "__main__":
    main()
