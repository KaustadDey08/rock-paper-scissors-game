# import random 
# user input rock,paper,scissors.

# rock:
# rock=rock:draw
# rock=paper:lose
# rock=scissors:win

# paper:
# paper=paper:draw
# paper=rock:win
# paper=scissors:lose

#scissors: 
# scissors=scissors:draw
# scissors=rock:lose
# scissors=paper:win

# import random
import random

# taking  input from user as rock,paper,scissors
my_move=str(input("Enter your move(rock,paper,scissors):"))

my_list=["rock","paper","scissors"] 
comp_move=random.choice(my_list)
print(f"\nYou chose {my_move}, computer chose {comp_move}.\n")


# when match is draw.
if comp_move==my_move:
    print(f"Both players selected {my_move}. It's a tie!")

# win and lose logic using 
elif my_move=="rock":
    if comp_move=="scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

elif my_move=="paper":
    if comp_move=="rock":
         print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

elif my_move=="scissors":
    if comp_move=="paper":
      print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

print("\n Happy coding")
