import random

num1 = random.randint(0,10)

for i in range(3):
    num = int(input("Guess the number! : "))
    if num == num1:
        print(f"Congratulations! You guessed the right number {num1}!")
        break
    else:
        if num1 > num:
            print("Too low! try higher number :*)")
        elif num1 < num:
            print("Too High! try lower number :*)")
else:
    print(f"The correct number was : {num1}")