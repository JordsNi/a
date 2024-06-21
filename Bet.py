from random import randint   # nag import ug module nga pang random sa integers

while True:   # While loop nga e padayun ang dula until na ma pul an ang user
    
    bet = input("\n'Bet Game'\nEnter you 3 digit bet (or press 0 to quit): ").strip()   # nangayo ug input sa user
    win = str(randint(000,999))   # string na randomized number na ihatag ni win
    
    if bet == 0:   # if ang input is 0 lang
        print("Bet game stopped! ayaw nag sugal")   # e print ni
        break   # so sad
    
    if len(bet) != 3 or not bet.isdigit():   #gina check kung 3 ka digits ba ang gi input or letters
        print("Invalid input! Basahag tarung")   #kung true, e print ni
        continue   #balik mangayo ug input 
    
    print("\nYour bet is:",bet ,"\nThe winning bet is:",win)   #print ang imong bet ug ang winning bet
    
    if bet == win:   # if same ang bet ug win, daog ka
        print("You win!")
    elif sorted(bet) == sorted(win):   #if same silag numbers pero different placements, partially win ra
        print("You partially win!")
    else:   # kung walay ni tugma, wala jud!
        print("You lose!")   #from 19 to 23. ni taas ang lines pero automated(char?) na niya mas hinlo(?) tan awon