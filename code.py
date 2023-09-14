
import random as ra
from demo4 import *

print("Welcome to hangman game!")

list_of_str = ['apple','ballon','capital','Doll','Elevate']
let = ra.choice(list_of_str).lower()

n = len(let)
list = ["-"]*n

print("no.of lives you have 6")
print("find these letters:",list)
si= 6
ch=0
while(si>0):

    i = input("guess a letter for the word:").lower()

    if i in let:
        for pos in range(n):
            ltr = let[pos]
            if ltr==i:
                list[pos]=i
        print(list,'\t'"lives:",si)
        print(states[si])
    if i not in let:
        si-=1
        print(list,'\t'"lives:",si)
        print(states[si])

    if '-' not in list:
        break


if '-' in list:
    print("you lose")
else:
    print("you win")

