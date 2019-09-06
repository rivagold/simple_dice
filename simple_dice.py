import random

def roll(sides):
    num_rolled = random.randint(1,sides)
    return num_rolled



def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? Enter=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("you rolled a", num_rolled)
        else:
            rolling = False

        print("Thank you for playing")

if __name__ == '__main__':
    main()