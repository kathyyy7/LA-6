

"""""

To start, we will generate a random integer between 1 and 20, and
based on the result of the random number, we check to see if it falls under certain range
if the number is greater than 15, then the result will be "Cherries"
otherwise if the number is > 10, then the result will be "Orange"
otherwise if the number is > 5, then the result will be "Plum"
otherwise if the number is > 2, then the result will be "Melon"
otherwise if the number is > 1, then the result will be "Bell"
if the number is not any of the above, then the result will be "Bar"

We iterate over using a loop three time and print the result to use. As an example, "Plum Cherries Melon"


"""""
"""""

num = generate random number

if the num is greater than 15,
    then the result will be "Cherries"
otherwise if num is > 10,
    then the result will be "Orange"
otherwise if num is > 5, 
    then the result will be "Plum"
otherwise if num is > 2, 
    then the result will be "Melon"
otherwise if num is > 1, 
    then the result will be "Bell"
if num is not any of the above, 
    then the result will be "Bar"
loop three times
    print the output (fruit) to the user


"""""

import random

def main():
    results = []
    for i in range(0,3):
        results.append(spin())

print("results", results)
winner = jackpot(results)

if (winner):
    print("Winner! you win")
else:
    print("Sorry try again")

def spin():
    rand_num = random.randint(1,20)
    output = ""
if(rand_num > 15):
    output ="Cherries"
elif(rand_num > 10):
    output = "Orange"
elif(rand_num > 5):
    output = "Orange"
elif(rand_num > 2):
    output = "Orange"
elif(rand_num > 1):
    output = "Orange"
else:
    output = "Bar"

print(output, end="")

def jackpot(results):
    return results[0] == results[1] == results[2]

def count(results):
    money_dict = {
        "Cherries": 1,
        "Orange": .7,
        "Plum": .6,
        "Bell": .4,
        "Melon": .2,
        "Bar": .1
    }

for i in results:
    total += money_dict[i]
print("total: ", total)
