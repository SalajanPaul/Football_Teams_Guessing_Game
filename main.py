import random

name = input("Welcome to the Football Teams Guessing game from Romania, what is your name? ")
print("--- Good luck", name, "----")

teams_names = ["FCSB", "CFR Cluj", "Rapid Bucuresti", "CS Universitatea Craiova", "Sepsi OSK",
               "Farul Constanta", "Universitatea Cluj", "Petrolul Ploiesti", "FC Hermannstadt", "Otelul Galati",
               "FC U Craiova 1948", "FC Voluntari", "UTA Arad", "CSM Politehnica Iasi", "Dinamo Bucuresti" "FC Botosani"]


team = random.choice(teams_names).upper()


guesses = ""
turns = 12

while turns > 0:
    failed = 0

    for i in team:
        if i in guesses:
            print(i, end=" ")
        elif i == " ":
            continue
        else:
            print("_", end=" ")
            failed += 1

    print("Remaining turns:", turns)

    if failed == 0:
        print("You won!")
        print(f"The team is {team}.")
        break

    print()
    guess = input("Enter a character: ").upper()

    guesses += guess

    if guess not in team:
        turns -= 1
        print("Wrong")

        print(f"You have {turns} more guesses")

        if turns == 0:
            print(f"You lost, the name of the team was {team}")
