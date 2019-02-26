'''
Self Check
Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem?
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time
will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we
replace a monkey with a Python function. How long do you think it would take for a Python function to generate
just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll
simulate this is to write a function that generates a string that is 28 characters long by choosing random
letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each
generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s
progress this third function should print out the best string generated so far and its score every 1000 tries.

'''

import random

def random_string(lans):
    letters = "abcdefghijklmnopqrstuvwxyz "
    guess = ""

    while len(guess) <= lans - 1:
        guess += random.choice(letters)

    return guess

def monkey_score(ans, guess):
    score = 0

    i = 0
    j = 0

    while i <= len(ans) - 1:
        if ans[i] == guess[j]:
            score += 1
        i += 1
        j += 1

    return score

def main():
    ans = "methinks it is a weasel"
    count = 0
    final_score = 0
    current_best_string = ""

    while count <= 20000:
        count += 1
        new_guess = random_string(len(ans))
        new_guess_score = monkey_score(ans, new_guess)

        if count % 1000 == 0:
            print(f"current count: {count} \n"
                  f"current best score {final_score} \n"
                  f"current closest string ={current_best_string}")
        if new_guess_score > final_score:
            final_score = new_guess_score
            current_best_string = new_guess

    return final_score, current_best_string
