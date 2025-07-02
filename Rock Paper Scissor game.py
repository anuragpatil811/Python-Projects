"""
WORKFLOW OF PROJECT:
1-Input from user(Rock, paper, scissor)
2-Computer choice(Computer will choose randomly not conditionally)
3-Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - paper = Paper win
Rock - scissor = Rock Wins

B- Paper
Paper - Paper = tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor Win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Paper Win
"""
import random 
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor=")
comp_choice = random.choice(item_list)
print(f"User Choice = {user_choice}, Computer choice = {comp_choice}")