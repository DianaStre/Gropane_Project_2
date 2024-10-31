from module_george import generate_road
from module_vlad import play_stage

def play_game():
    """
    Aidan: Manages the overall game flow, transitioning through stages from start to end.
    """
    starting_point, ending_point, stages = generate_road()
    print ("This is the story of an unfortunate man that left with his car from the best mechanic in the city, and his life depends on his luck on the way home.")

    print ("Hope you will be a lucky man because you're car wasn't that lucky")
    print(f"Starting your journey from {starting_point} to {ending_point}.\n")

    for i, stage in enumerate(stages):
        stage_name = ["vest", "centru", "est"][i]
        print(f"--- Entering {stage_name.capitalize()} Romania ---")

        # Play the current stage
        if not play_stage(stage, stage_name):
            return  # End game if the player loses all HP in any stage

    # If all stages are completed, the player wins
    print("Congratulations! You have successfully reached Iasi and completed the game!")
