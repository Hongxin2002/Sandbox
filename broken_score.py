"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(determine_level(score))

def determine_level(score):
    if score >= 0 and score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"
    else:
        return "Invalid Score"

main()