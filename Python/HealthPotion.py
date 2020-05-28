import random

health = 50
difficulty = 1  #1:easy;2:amateur;3:hard

potionHealth = int(random.randint(25,50)/difficulty)
health+=potionHealth

print(health)

