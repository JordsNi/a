from random import randint   # nag import ug pang random sa integers nga module

while True:   # While loop nga e padayun ang dula until na ma pul an ang user

    P1 = int(input("\n'Humpyang Game'\nType 1 for 'Fold' or 2 for 'Unfold' (or '0' to Quit): "))   # nangayog input sa user 
    C2 = randint(1,2)   
    C3 = randint(1,2)   # gi randomize ang value nga e hatag sa C2 ug C3 kung 1 or 2 ba
    
    if P1 == 0:   # if statement na kung mag input si user ug 0,stop na ang program
        print("Humpyang Game Stopped, Ciao!")   # goodbye message awww
        break   # break na daw AWWWWW
    
    if P1 not in (1, 2):  #if dili 1, 2 or 0 ang gi type gi input
        print("Invalid input! Please enter 1, 2, or 0.")   # e print ni
        continue   #balik mangayo ug input sa user
    
    print(f"P1 picks: {'Fold' if P1 == 1 else 'Unfold'}\nC2 picks: {'Fold' if C2 == 1 else 'Unfold'}\nC3 picks: {'Fold' if C3 == 1 else 'Unfold'}")   #kung 1 ang mapilian, "Fold" and e print. "Unfold" naman kung C2. Credits kay BINI Javier kay siya nagtudlo sa ako ani nga code
    
    #if statements (dagan sa dula)
    if P1 == C2 == C3:   #if pareha sila tanan ug result, tabla ang dula
        print("Draw!")
    elif P1 != C2 == C3:   #if lahi ang choice ni P1 ug parehas ang choice ni C2 ug C3, daog si P1
        print("Player 1 Wins!")
    elif P1 != C2 != C3:   #if dili parehas si P1 ug C2 ug dili pud parehas si C2 ug C3, daog si C2
        print("Computer 2 Wins!")
    elif P1 == C2 != C3:   #if parehas si P1 ug C2 pero lahi si C3, daog si C3
        print("Computer 3 Wins!")
    else:   
        ...   #from 35 line originally nahimog 29 nalang sheeshable!!!