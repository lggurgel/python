import random

sort_number = random.randrange(1,100)
tries = 0

while True:
    guess = int(input("guess number: "))

    if guess == sort_number:
        print("won")
        break
    elif guess < sort_number:
        tries+=1
        print("more")
    elif guess > sort_number:
        tries+=1
        print("less")

print("your random number is", sort_number)
print("you needed", tries, "tries to win")