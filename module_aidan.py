from module_george import generate_road
from module_vlad import play_stage

def play_game():
    starting_point, ending_point, stage = generate_road()
    print(f"You start from {starting_point} to {ending_point}.")
    for i, stage in enumerate(stage):
        stage_name = ["vest", "centru", "est"][i]
        print(f" You are in {stage_name} city ")

        # play current city
        if not play_stage(stage, stage_name):
            return  # game over  if the player loses his life in a stage
    # the player wins If he arrives in iasi
    print("You arrived in Iasi!")
