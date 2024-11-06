from module_george import generate_road
from module_vlad import play_stage

def play_game():
    starting_point, ending_point, stage = generate_road()
    print("""
      _____ _            _       _                 _                        
     |_   _| |__   ___  / \   __| |_   _____ _ __ | |_ _   _ _ __ ___ _ __  
       | | | '_ \ / _ \/ _ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ '__| 
       | | | | | |  __/ ___ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ |    
       |_| |_| |_|\___/_/   \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|_|    

        """)
    print("This is the story of an unfortunate man who went to the best "
          "mechanic in the village, after he left the mechanic his way "
          "to home depended more on Pure Luck:D")
    print("SO LET THE ADVENTURE BEGIN !")
    print(f"You start from {starting_point} to {ending_point}.")
    for i, stage in enumerate(stage):
        stage_name = ["west", "center", "east"][i]
        print(f" You are in the {stage_name} side of the country")

        # play current city
        if not play_stage(stage, stage_name):
            return  # game over  if the player loses his life in a stage
    # the player wins If he arrives in iasi
    print("You arrived in Iasi!")
