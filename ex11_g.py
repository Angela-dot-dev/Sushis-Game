from sys import exit
import os

history = open('ex11_g.txt', "r")


def clear():  # For the cleaning
    return os.system('cls')

# Begining of scenes


def pause():  # Makes the player press enter to unlock dialog
    input('Press enter to continue')
    clear()

# 1.- Waking up the cat


def question1():
    # Start Question (context).
    print("\t\tAt a normal house on the suburbs, a cat gently snorts\n\t\tIs a beautiful and sunny day, shall the cat awake yet?\n")
    answText = '\t[1] Wake up sleepy head!\t\t\t[2] Just a little bit longer...\n\t\t\t\t   Type Your Number'

    def question():
        print(answText)
        answ1 = input('\n> ')
        clear()
        return answ1
    answ1 = question()
    answ = answ1

    if answ1.isdigit() == True:  # Checks if you didnt answer an string
        if int(answ1) == 1:  # Checks if you answer correctly first.
            return
        else:  # Checks if you answered 2 it run this loop.
            # Answer checking loop, 5 tries and then gives up on you.
            for x in range(0, 5):

                if answ1.isdigit() == False:
                    print(
                        f'You waste time saying something incomprehensible...{x+1}st attempt\nWrite a 1 or a 2, or else the cat will stay sleeping!')
                    answ1 = question()
                elif int(answ1) == 2 and x == 3:  # Answer at 4st try
                    print(
                        f'You let the cat sleep for the {x+1}st time, he is just so cute when sleeping!')
                    answ1 = question()
                elif int(answ1) == 2 and x == 4:  # Answer at 5st try
                    print(
                        f'You let the cat sleep for the {x+1}st time. He seems to be reaching cuteness levels you will later cannot bring your self to disturb!')
                    answ1 = question()
                elif int(answ1) == 2:  # Answer to 1st to 3st
                    print(
                        f'You let the cat sleep for a little... now what? {x+1}st time')
                    answ1 = question()
                elif int(answ1) == 1:  # Checks if you answer 1
                    return
                else:  # Answer for if you type whatever, doesnt count as iteration.
                    print(
                        'Wait what did you do?\nWrite a 1 or a 2, or else the cat will stay sleeping!')
                    answ1 = question()
            else:
                pass
            # Checks if you answer correctly on your last try.
            if answ1.isdigit() == True:
                if int(answ1) == 1:
                    return
                else:
                    pass
            else:
                gameOver('The cat sleeps all day, goodbye adventure!')
        return
    elif answ1.isdigit() == False:  # Cheks if you did answer an string
        print(f'Error, you typed an "{answ}"')
        pause()
        exit(0)
    else:  # If you answered 1 it let you out
        pass


def question2():
    # Context
    for x in range(0, 5):
        x = x + 0  # <-- This was just to use the variable and make the pc shut up
        print(history.readline())
    else:
        print('\n')
    answText = "\t[1] Bump into her hand, pets!\t\t\t[2] Back away.\t\t\t [3] Don't do anything."

    def question():
        print(answText)
        answ1 = input('Type Your Number\n> ')
        clear()
        return int(answ1)
    answ1 = question()

    for x in range(0, 11):

        if answ1 == 1:
            history.seek(303)

            hist_txt()
            hist_txt()
            hist_txt()
            pause()
            hist_txt()
            hist_txt()
            hist_txt()
            pause()
            hist_txt()
            hist_txt()
            input('Press Enter to end Beta')
            break
        elif answ1 == 2:
            history.seek(931)

            hist_txt()
            hist_txt()
            hist_txt()
            pause()
            hist_txt()
            hist_txt()
            hist_txt()
            hist_txt()
            pause()
            input('Press Enter to end Beta')
            break
            # print(history.seek(history.tell())) = 1439
        elif answ1 == 3:
            history.seek(1457)

            hist_txt()
            hist_txt()
            input('Press Enter to end Beta')
            break
        else:
            print(f"Try again chum, you have {10-x} more tries")
            answ1 = question()
    else:
        pass


# End of scenes


# Ask for a game over reason and then tells you game over! Then exit.
def gameOver(why):
    print(why)
    input('Press Enter to end Beta')
    exit(0)


def hist_txt():  # Takes where the history been left in the file and print it.
    history.seek(history.tell())
    print(history.readline())


def start():
    print('')
    question1()
    question2()


start()
# py ex11_g.py
