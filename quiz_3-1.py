# Author: JAP (amdg) 1/12/2021

# Prints everything correctly, but it repeats the list adding a name each time

younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']

future_jedi = []
for index, padawans in enumerate(younglings):
    name = padawans + ", " + race[0] + "."
    del race[0]
    future_jedi.append(name)
    print(future_jedi)
