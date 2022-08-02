import random
import re
import turtle
import time


class Hagman_game:
    word_status = ""

    def __init__(self, wordlist):
        self.__wordlist = wordlist
        self.__attempts_remaining = 6
        self.__current_letter = ''
        self.__choosen_word = ''
        self.__already_guessed_letter = []

    def get_choosen_word(self):
        return self.__choosen_word

    def get_current_letter(self):
        return self.__current_letter

    def get_already_guessed_letter(self):
        return self.__already_guessed_letter

    def get_attempts_remaining(self):
        return self.__attempts_remaining

    def single_or_multiplayer(self):
        print("single player or multiple player?")
        single_or_multiplay = input("Please Enter the value: ")
        if single_or_multiplay == '1':
            self.choose_the_word()
        else:
            self.choose_the_word_multi()

    def choose_the_word(self):
        file = open(self.__wordlist, 'r')
        words = file.read().split("\n")
        word_count = len(words)
        self.__choosen_word = words[random.randrange(0, len(words))]
        self.word_status = ['_' for i in range(len(self.__choosen_word))]

    def choose_the_word_multi(self):
        self.__choosen_word = input("\nEnter the word your friend need to be guessed: ")
        #print(self.get_choosen_word())
        self.word_status = ['_' for i in range(len(self.__choosen_word))]

    def fill_the_letter_for_hint(self):
        no_of_letters_for_hint = random.randrange(1, 3)
        for i in range(no_of_letters_for_hint):
            position = random.randrange(0, len(self.__choosen_word))
            self.word_status[position] = self.__choosen_word[position]

    def guess_the_letter(self):
        if self.__attempts_remaining == 6:
            print("\n{} letter word need to guess : {}".format(len(self.__choosen_word), "".join(self.word_status)))
        start = time.time()
        letter = input("Guess the letter : ")
        end = time.time()
        flag = 1
        if end - start > 10:
            print("You have taken more than 10 seconds to guess letter")
            self.__attempts_remaining -= 1
            drawMan(6 - self.__attempts_remaining)
            flag = 0
        if letter in self.__already_guessed_letter:
            print("You have already guessed this letter.Your guesses are :{}".format(
                ''.join(self.__already_guessed_letter)))
            return

        if flag == 1:
            self.__already_guessed_letter.append(letter)
            occurence = re.finditer(letter, self.__choosen_word)
            occurences = []
            for m in occurence:
                occurences.append(m.start())

            if len(occurences) == 0:
                self.__attempts_remaining -= 1
                if 6 - self.__attempts_remaining == 1:
                    drawMan(0)
                drawMan(6 - self.__attempts_remaining)
            else:
                for position in occurences:
                    self.word_status[position] = self.get_choosen_word()[position]
                print("Correct letter guess")

    def get_word_status(self):
        print("Current status :{}\n".format(''.join(self.word_status)))


class Another_Hangman_Creator(Hagman_game):
    def fill_the_letter_for_hint(self):
        no_of_letters_for_hint = random.randrange(1, 3)

        for i in range(no_of_letters_for_hint):
            position = random.randrange(0, len(self.__choosen_word))
            self.word_status[position] = self.__choosen_word[position]

def drawMan(x):
    guess = x
    if guess == 0:
        wn = turtle.Screen()
        wn.bgcolor("SlateGray1")
        wn.bgpic("darkk.gif")
        wn.title("black")
        turtle.goto(-83, 224)
        turtle.pencolor("LightYellow")
        turtle.write('Hangman Game', False, align='left', font=('Arial', 15, 'bold'))
        turtle.penup()
        turtle.home()
        turtle.hideturtle()
        turtle.pencolor("LightYellow")
        turtle.color("LightYellow")
        turtle.pendown()
        turtle.begin_fill()
        turtle.pen(pencolor="LightYellow", fillcolor="LightYellow", pensize=5, speed=2)
        for i in range(4):
            turtle.forward(30)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(15)
        turtle.right(270)
        turtle.forward(31)
        turtle.pen(pencolor="DarkGoldenrod")
        turtle.forward(144)
        turtle.left(90)
        turtle.forward(95)
        turtle.left(180)
        turtle.forward(7)
        turtle.left(270)
        turtle.pensize(3)
        turtle.forward(35)
        turtle.penup()

    if guess == 1:
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.bgcolor("green")
        turtle.right(90)
        turtle.begin_fill()
        turtle.pen(pencolor="LightYellow", fillcolor="LightYellow", pensize=2)
        turtle.circle(15)
        turtle.end_fill()
        turtle.pencolor("DarkSlateGrey")
        turtle.penup()
        turtle.goto(-70, 130)
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.goto(-78, 130)
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.goto(-69, 120)
        turtle.pendown()
        turtle.goto(-79, 120)
        turtle.penup()
        turtle.pencolor("LightYellow")

    elif guess == 2:
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.bgcolor("light green")
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif guess == 3:
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.bgcolor("Gold")
        turtle.left(55)
        turtle.forward(45)
        turtle.dot(10)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 4:
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.bgcolor("orange")
        turtle.left(70)
        turtle.forward(45)
        turtle.dot(10)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 5:
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.bgcolor("Crimson")
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.dot(15)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
    elif guess == 6:
        turtle.goto(-74, 70)
        turtle.pendown()
        turtle.bgcolor("red4")
        turtle.right(120)
        turtle.forward(60)
        turtle.dot(15)
        turtle.penup()
        turtle.goto(-5, -150)
        turtle.write('Thanks for playing! Better luck next time', False, align='center', font=("Courier", 15, "normal"))
        time.sleep(5)
