import random #This line imports the random module, which will be used to make random selections.

def play_stage(stage, stage_name):  #
    #This defines a function named play_stage that takes two parameters: stage
    #(a dictionary of cities and their damage values) and stage_name (the name of the current stage).
    """
    Vlad: Handles the gameplay for a single stage, managing HP and city encounters.
    """
    # nivel nou generat cu replenished life (5 HP)
    # player input is a, w, d
    cities = list(stage.keys())  # This creates a list of all cities
                                 # in the current stage by getting the keys from the stage dictionary.
    hp = 5  # Player's HP for each stage
    moves = 0  # Counter for the number of moves made

    while hp > 0 and moves < 10:   # This starts a loop that continues as long as the
                                  # player has HP and hasn't made 10 moves yet.
        city = random.choice(cities)  #This randomly selects a city from the list of available cities.

        # Display player information and we announce the player keys for playing
        print(f"\nCurrent \033[94mHP: {hp}\033[0m | A city is ahead!")
        print("Choose direction: 'a' (left), 'w' (straight), 'd' (right)")


        move = input("Your move: ").strip().lower() # Get player's move
        if move not in ["a", "w", "d"]:
            print("Invalid move. Please enter 'a', 'w', or 'd'.")
            continue
              # This gets the player's move, converts it to lowercase, and checks if it's valid.
              #If not, it prints an error message and continues to the next iteration of the loop.

        if move in ["a", "d", "w"]:  # If player chooses 'a', "w" or 'd', select a random different city
            alt_city = random.choice(cities)
            while alt_city == city and len(cities) > 1:
                alt_city = random.choice(cities)
            city = alt_city

        # Get damage value and update HP by each city we move
        city_damage = stage[city]
        hp += city_damage

        # Inform the player of their outcome
        print(f"Entered \033[35m{city}\033[0m. Your HP is now \033[94m{hp}\033[0m.")

        # Remove the city from the list to avoid revisiting
        if city in cities:
            cities.remove(city)

        # Update the number of moves
        moves += 1

        # Check if player has lost,we used less than 0 if by any chance his live will go less than 0(-1 or -2...)
        if hp <= 0:
            print("Your car has been totaled! Game over.")
            return False

    # Check if the stage is complete
    if hp > 0:
        print(f"Stage {stage_name.capitalize()} completed! You've made {moves} moves. Moving to the next region...\n")
        return True
    else:
        print("Your car has been totaled! Game over.")
        return False