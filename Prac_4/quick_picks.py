import random
def main():
    quick_pick_number = int(input("How many quick_picks you want?"))
    while quick_pick_number < 0:
        print("Invalid")
        quick_pick_number = int(input("How many quick_picks you want?"))

    for i in range(quick_pick_number):
        quick_picks = []
        for j in range(6):
            number = random.randint(1, 45)
            while number in quick_picks:
                number = random.randint(1, 45)
            quick_picks.append(number)
        quick_picks.sort()

        print(" ".join("{:2}".format(number) for number in quick_picks))

if __name__ == '__main__':
    main()