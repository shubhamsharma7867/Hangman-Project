import Player
import time
import math

start = time.time()
obj1 = Player.Hangman_Player()
obj1.start_game()
end = time.time()
print("The time taken to guess the word : {}".format(end-start))
