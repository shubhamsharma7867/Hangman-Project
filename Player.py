import Hangman_Creator
import time


class Hangman_Player:

    def start_game(self):
        hangman = Hangman_Creator.Another_Hangman_Creator('C:\\Users\localadmin\PycharmProjects\words.txt')
        hangman.single_or_multiplayer()
        hangman.guess_the_letter()
        while True:
            hangman.get_word_status()
            hangman.guess_the_letter()
            if hangman.get_attempts_remaining() == 0:
                print("Out of attempts.Game Over...!!! The word was :{}".format(hangman.get_choosen_word()))
                break
            elif hangman.get_choosen_word() == ''.join(hangman.word_status):
                print("Congratulations! You won the game !!!")
                break
