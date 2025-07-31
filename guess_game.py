import random
secret_number=random.randint(1,100)
guess=None
print(secret_number)
while guess!=secret_number:
    guess=int(input("Enter a number between 1 and 100 :"))
    if(guess>secret_number):
        print("TOO big try again.")
    elif(guess<secret_number):
        print("TOO small try again." )
    else:
        print("CONGRALUTIONS YOU WON!")
    