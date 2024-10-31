import random

def play_stage(stage, stage_name):
    """
    Vlad: Handles the gameplay for a single stage, managing HP and city encounters.
    """
    cities = list(stage.keys())  # List of cities in the current stage
    hp = 5  # Player's HP for each stage
    tries = 0  # Reset tries for each new stage

    while cities and hp > 0 and tries < 10:
        city = random.choice(cities)

        # Display player information
        print(f"\nCurrent HP: {hp} | A city is ahead!")
        print("Choose direction: 'a' (left), 'w' (straight), 'd' (right)")

        # Get player's move
        move = input("Your move: ").strip().lower()
        if move not in ["a", "w", "d"]:
            print("Invalid move. Please enter 'a', 'w', or 'd'.")
            continue

        # If player chooses 'a' or 'd', select a random different city
        if move in ["a", "d","w"]:
            alt_city = random.choice(cities)
            while alt_city == city:
                alt_city = random.choice(cities)
            city = alt_city

        # Get damage value and update HP
        city_damage = stage[city]
        hp += city_damage

        # Inform the player of their outcome
        print(f"Entered {city}. Your HP is now {hp}.")

        # Remove the city from the list to avoid revisiting
        cities.remove(city)

        # Update the number of tries for the stage
        tries += 1

        # Check if player has lost
        if hp <= 0:
            print("Your car has been totaled! Game over.")
            return False

    # If 10 tries are reached without losing all HP, proceed to next stage
        if tries == 10:
            print(f"Stage {stage_name.capitalize()} complete! Moving to the next region...\n")
    return True
