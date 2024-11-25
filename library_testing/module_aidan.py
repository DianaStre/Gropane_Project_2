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
    print("\033[92mThis is the story of an unfortunate adventurer who went to the best "
          "mechanic in the village, but after he left the mechanic his way"
          "home depended more on Pure Luck:D\033[0m")
    print("\033[1;92mSO LET THE ADVENTURE BEGIN !\033[0m")
    print(f"You start from {starting_point} and you want to go home to {ending_point}.")
    for i, stage in enumerate(stage):
        stage_name = ["western", "central", "eastern"][i]
        print(f"\033[93mYou are in the \033[38;5;166m{stage_name}\033[93m side of the country\033[0m")

        # play current city
        if not play_stage(stage, stage_name):
            return  # game over  if the player loses his life in a stage
    # the player wins If he arrives in iasi
    print(f"\033[1m\033[38;5;82mCongratulations! \033[0m")
    print(f"✨\033[1m\033[38;5;220mYou arrived in \033[1m\033[38;5;82mIasi\033[0m")
    print(f"\033[1m\033[38;5;220mwith your 🚗 intact!\033[0m✨")
