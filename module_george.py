from random import random, randint


def generate_road():
    """
    George: Defines the game map with cities and damage values for each region of Romania.
    """
    # player starts in Timisoara, having just repaired their car
    # player wants to go home to Iasi
    # each section of the map contains 10 cities (local clusters)
    # inpartim tara in 3, vest/ centru/ est
    # plecam din vest, cand terminam vestul (cu viata), trecem la urmatorul nivel (centru), etc.
    # player must cross a total of 3 sections
    # din cele 3 optiuni,
    #       la nivelul 1: 1 neutra (0 damage), 1 buna (+1 damage), 1 rea (-1 damage)
    #       la nivelul 2: 2 neutre (0 damage), 1 rea (-1 damage)
    #       la nivelul 3: 2 rele (-1 damage), 1 neutra (0 damage)
    # fiecare oras prin care am trecut, se suprima din lista dictionarului
    # new line
    starting_point = "Timisoara"
    ending_point = "Iasi"

    harta_vest_romania = {
        "Arad": random.choice([-1, 0, 1]),
        "Oradea": random.choice([-1, 0, 1]),
        "Satu Mare": 1,
        "Sighetu Marmatiei": random.choice([-1, 0, 1]),
        "Craiova": random.choice([-1, 0, 1]),
        "Zalau": 1,
        "Deva": random.choice([-1, 0, 1]),
        "Drobeta-Turnu Severin": random.choice([-1, 0, 1]),
        "Baia Mare": 1,
        "Caransebes": random.choice([-1, 0, 1]),
        "Lugoj":-5,
        "Resita":1
    }

    harta_centru_romania = {
        "Cluj-Napoca": random.choice([-1, 0, 1]),
        "Targu Mures": 0,
        "Ramnicu Valcea": random.choice([-1, 0, 1]),
        "Bucuresti": random.choice([-1, 0, 1]),
        "Brasov": random.choice([-1, 0, 1]),
        "Miercurea Ciuc": 0,
        "Targoviste": random.choice([-1, 0, 1]),
        "Turda": random.choice([-1, 0, 1]),
        "Pitesti": random.choice([-1, 0, 1]),
        "Ploiesti": 0,
        "Orastie": -5,
        "Dej": -5,
        "Bistrita": 0,
        "Sighiisoara": random.choice([-1, 0, 1])
    }

    harta_est_romania = {
        "Constanta": random.choice([-1, 0, 1]),
        "Braila": random.choice([-1, 0, 1]),
        "Galati": random.choice([-1, 0, 1]),
        "Focsani": -1,
        "Botosani": -1,
        "Suceava": random.choice([-1, 0, 1]),
        "Piatra Neamt": -1,
        "Bacau": -1,
        "Ramnicu Sarat": random.choice([-1, 0, 1]),
        "Vaslui": random.choice([-1, 0, 1]),
        "Tecuci": -5,
        "Barlad": -5,
        "Roman": -5,
        "Husi": random.choice([-1, 0, 1]),
        "Pascani": random.choice([-1, 0, 1]),
        "Gura Humorului": random.choice([-1, 0, 1])
    }

    return starting_point, ending_point, [harta_vest_romania, harta_centru_romania, harta_est_romania]
