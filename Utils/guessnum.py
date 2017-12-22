import random

def guest():
    answer = random.randint(0,10)
    flag = True
    user_guest_num = int(input('guess num'))
    while flag:
        if answer == user_guest_num:
            flag = False
            print("you win")
        elif user_guest_num > answer:
            user_guest_num = int(input('too high, guess against'))
        elif user_guest_num < answer:
            user_guest_num = int(input('too low , guess against'))

guest()

