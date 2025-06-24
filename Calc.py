#!/usr/bin/env python3

startlvl = input("What level are you? | ")
endlvl = input("What level do you want to get to? | ")
print("")

vip = input("Do you have VIP? 1 for yes, 2 for no. | ")
print("")

time = input("How much hours do you need? Put 0 for plain results. | ")
print("")

mins = int(time) * 60
roundss = int(mins) / 5

lvlneed = int(endlvl) - int(startlvl)

startep = int(startlvl) * 10
startxp = int(startep) + 100

total = 0

for i in range(lvlneed):
    total = int(startxp) + int(total)
    startxp = int(startxp) + 10

if int(time) > 0:
    if int(vip) == 1:
        print("Rounds - ", roundss)
        puzzless = int(total) // 18.75
        killss = int(total) // 56.25
        print("XP - ", int(total) * 0.75)
        print("Puzzles - ", puzzless // roundss )
        print("Kills - ", killss // roundss)
        print("")
        
    else:
        print("Rounds - ", roundss)
        puzzless = int(total) // 15
        killss = int(total) // 45
        print("XP - ", int(total))
        print("Puzzles - ", puzzless // roundss )
        print("Kills - ", killss // roundss)
        print("")
        
        
if int(time) == 0:
    if int(vip) == 2:
        print("XP - ", int(total))
        print("Puzzles - ", int(total) // 15)
        print("Wins - ", int(total) // 120 )
        print("Kills - ", int(total) // 45)
        print("Killer Wins - ", int(total) // 180)  
        print("")
        
    else:
        print("XP - ", int(total) * 0.75)
        print("Puzzles - ", int(total) // 18.75)
        print("Wins - ", int(total) // 150.0)
        print("Kills - ", int(total) // 56.25)
        print("Killer Wins - ", int(total) // 225.0)
        print("")

input("Press Enter to exit.")

        
