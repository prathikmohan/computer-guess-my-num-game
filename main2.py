
import random

def guess(x):
    low = 1
    high = x #1+x
    feedback = ''
    while feedback !='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high

        feedback = input(f"Is {guess} the correct number(c) or too high(h) or too low(l)??").lower()
        
        if feedback =='h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1
    
    print(f"Yay! I guessed the number {guess} correctly!")

guess(100)
