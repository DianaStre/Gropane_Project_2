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
    starting_point = "Timisoara"
    ending_point = "Iasi"

    harta_vest_romania = {
        "Arad": 0,
        "Oradea": 1,
        "Satu Mare": -1,
        "Sighetu Marmatiei": 0,
        "Craiova": 1,
        "Zalau": -1,
        "Deva": 0,
        "Drobeta-Turnu Severin": 1,
        "Baia Mare": -1,
        "Caransebes": 0
    }

    harta_centru_romania = {
        "Cluj-Napoca": 0,
        "Targu Mures": 0,
        "Ramnicu Valcea": -1,
        "Bucuresti": 0,
        "Brasov": 0,
        "Miercurea Ciuc": -1,
        "Targoviste": 0,
        "Turda": 0,
        "Pitesti": -1,
        "Ploiesti": 0
    }

    harta_est_romania = {
        "Constanta": -1,
        "Braila": -1,
        "Galati": 0,
        "Focsani": -1,
        "Botosani": -1,
        "Suceava": 0,
        "Piatra Neamt": -1,
        "Bacau": -1,
        "Ramnicu Sarat": 0,
        "Vaslui": 1,
        "Tecuci": 0,  # New city with 0 damage
        "Barlad": 1,  # New city with +1 HP
        "Roman": 1  # New city with +1 HP
    }

    return starting_point, ending_point, [harta_vest_romania, harta_centru_romania, harta_est_romania]
