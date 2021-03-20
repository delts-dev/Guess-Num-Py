import random
num = random.randrange(1, 100)

def guess():
    print('Guess the number')
    print 'Higher than ', int(num-random.randrange(5, 10))
    print 'Lower than ', int(num+random.randrange(5, 10))
    ans()

def ans():
    if input('>>') == num:
        print("Correct")
    else:
        print("Wrong")
        guess()

guess()