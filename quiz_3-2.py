# Author: JAP (amdg) 1/12/2021

ledger = [['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]

bets = []
challengers = []

for ledgers in ledger:
    for index, names in enumerate(ledgers):
        if index == 0:
            challengers.append(names)
        else:
            bets.append(names)

print(bets, challengers)
