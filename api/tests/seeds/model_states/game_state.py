state_1 = {
            "gameId": "aFKeajFE",
            "players": ["player_1", "player_2"],
            "boards": [
                {
                    "size": 7,
                    "ships": [
                        {
                            "name": "Cruiser",
                            "coordinates": [[0, 0], [0, 1], [0, 2]],
                            "alive": [True, True, False],
                        },
                        {
                            "name": "Destroyer",
                            "coordinates": [[3, 3], [4, 3]],
                            "alive": [False, True],
                        },
                    ],
                    "missed_shots": [[0, 4], [2, 3], [5, 5]],
                },
                {
                    "size": 7,
                    "ships": [
                        {
                            "name": "Cruiser",
                            "coordinates": [[2, 0], [2, 1], [2, 2]],
                            "alive": [True, False, True],
                        },
                        {
                            "name": "Destroyer",
                            "coordinates": [[1, 5], [2, 5]],
                            "alive": [True, True],
                        },
                    ],
                    "missed_shots": [[3, 5], [0, 0], [4, 2], [6, 1]],
                },
            ],
            "ready": True,
            "turn": 7,
            "who_started": 1,
            "allowed_ships": {"Cruiser": 1, "Destroyer": 1},
            "who_won": None,
        }
