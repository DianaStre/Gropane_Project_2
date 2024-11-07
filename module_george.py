from random import randrange


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
    starting_point = "Timisoara"
    ending_point = "Iasi"

    """Level 1"""
    # Aici am pus un random de range -1 , 3 pentru mai multe sanse de castig
    harta_vest_romania = {
        "Arad": randrange(-1, 3, 1),
        "Oradea": randrange(-1, 3, 1),
        "Satu Mare": randrange(-1, 3, 1),
        "Sighetu Marmatiei": randrange(-1, 3, 1),
        "Craiova": randrange(-1, 3, 1),
        "Zalau": randrange(-1, 3, 1),
        "Deva": randrange(-1, 3, 1),
        "Drobeta-Turnu Severin": randrange(-1, 3, 1),
        "Baia Mare": randrange(-1, 3, 1),
        "Caransebes": randrange(-1, 3, 1),
        "Lugoj":-4,
        "Resita": randrange(-1, 3, 1)
    }

    """Level 2"""
    # Aici am pus un random de range -1 , 2 pentru sanse moderate
    harta_centru_romania = {
        "Cluj-Napoca": randrange(-1, 2, 1),
        "Targu Mures": randrange(-1, 2, 1),
        "Ramnicu Valcea": randrange(-1, 2, 1),
        "Bucuresti": -4,
        "Brasov": randrange(-1, 2, 1),
        "Miercurea Ciuc": randrange(-1, 2, 1),
        "Targoviste": randrange(-1, 2, 1),
        "Turda": randrange(-1, 2, 1),
        "Pitesti": randrange(-1, 2, 1),
        "Ploiesti": randrange(-1, 2, 1),
        "Orastie": -2,
        "Dej": randrange(-1, 2, 1),
        "Bistrita": randrange(-1, 2, 1),
        "Sighisoara": randrange(-1, 2, 1)
    }

    """Level 3"""
    # Aici am pus un random de range -1 , 1 pentru un nivel mai dificil
    harta_est_romania = {
        "Constanta": randrange(-1, 1, 1),
        "Braila": randrange(-1, 1, 1),
        "Galati": randrange(-1, 1, 1),
        "Focsani": randrange(-1, 1, 1),
        "Botosani": randrange(-1, 1, 1),
        "Suceava": randrange(-1, 1, 1),
        "Piatra Neamt": randrange(-1, 1, 1),
        "Bacau": randrange(-1, 1, 1),
        "Ramnicu Sarat": randrange(-1, 1, 1),
        "Vaslui": randrange(-1, 1, 1),
        "Tecuci": -3,
        "Barlad": -5,
        "Roman": randrange(-1, 1, 1),
        "Husi": randrange(-1, 1, 1),
        "Pascani": randrange(-1, 1, 1),
        "Gura Humorului": randrange(-1, 1, 1)
    }

    return starting_point, ending_point, [harta_vest_romania, harta_centru_romania, harta_est_romania]
