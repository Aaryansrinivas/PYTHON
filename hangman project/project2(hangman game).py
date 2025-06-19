import random
import hanggame_stages
import wordstore
computer_choice=random.choice(wordstore.words)
lives=6
display=[]
for i in range(len(computer_choice)):
    display+= '_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("enter a alphabet:").lower()
    for position in range(len(computer_choice)):
        letter=computer_choice[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in computer_choice:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose")
    if '_' not in display:
        game_over=True
        print("You won")
    print(hanggame_stages.stages[lives])
            
    
