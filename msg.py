
import random

with open("umbrella.txt", 'r') as file:
    quote = file.readlines()

s_quote = random.choice(quote).replace("â€™", "'")

with open("nickname.txt", 'r') as file:
    nickname = file.readlines()

s_name = random.choice(nickname)
