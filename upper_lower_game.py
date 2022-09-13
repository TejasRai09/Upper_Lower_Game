from game_data import data
import random
from art import logo
from art import vs
print(logo)
score = 0
def compare(guess,count_1,count_2):
  if a_count>b_count:
    return guess == 'a'
  else:
    return guess == 'b'
def select(account):
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_description}, from {account_country}"
account_b= random.choice(data)
game_should_continue = True
while game_should_continue:
        account_a = account_b
        account_b= random.choice(data)
        if account_a == account_b:
          account_b = random.choice(data)
        
        print(f"Comapre A: {select(account_a)}")
        print(vs)
        print(f"Comapre B: {select(account_b)}")
        
        a_count = account_a['follower_count']
        b_count = account_b['follower_count']
        guess = input("Make a guess: A or B").lower()
        is_correct = compare(guess,a_count,b_count)
        if is_correct:
          score += 1
          print(f"You are correct and your score is {score}")
        else:
          print(f"Sorry, that's wrong and your final score is {score}")
          game_should_continue = False