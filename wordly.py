import random

MAX_TRIES=6

BRED = '\033[1;31m'
BGRN = '\033[1;32m'
BYEL = '\033[1;33m'
RESETC = '\033[0m'

words=["QWERT","APPLE","BEARS","PHONE","INPUT"]

def match(secret, guess):
    result = ['']*5
    copy_secret= secret[:]

    for i, letter in enumerate(guess):
        if letter==copy_secret[i]:
            copy_secret=copy_secret[:i]+' '+copy_secret[i+1:]
            result[i]='G'

            
    for i, letter in enumerate(guess):
        if result[i]='':
            loc=copy_secret.find(letter)
            if loc>=0:
                copy_secret=copy_secret[:loc]+' '+copy_secret[loc+1:]
                result[i]='Y'
            else:
                result[i]='R'

    return result            
   

def main():
    while True:
        secret=random.choice{words}
        print("welcome to the game")

        tries =0
        while tries<MAX_TRIES:
            input_word=input("please enter the word").strip().upper()
            if len(input_word)!=5:
                print("please enter a 5 letter word")
                continue
            
            result=match(secret, input_word)

            print("Result: ", end="")
            for i in range(5):
                if result[i]=='G':
                    print(BGRN, end="")
        
        
