import code 

def evenLetters(word):
    evens=""
    if len(word)>=3:
        for i in range(2,len(word),2):
            evens+=word[i]
        return evens
    else:
        return "the word is too short"

def halfWord(word):
    half=''
    if len(word)>=3:
        half = word[len(word)//2:len(word)]
        half_with_dashes = "-".join(half)
        return half_with_dashes
    else:
        return "the word is too short"


def guess(answer):
    while True:
        guess = int(input('guess the number between 1 and 10, inclusive: '))
        if guess < answer:
            print('Too low!')
        elif guess > answer:
            print('Too high!')
        else:
            print('You win!')
            break

        
code.interact(local=dict(globals(),**locals()))
