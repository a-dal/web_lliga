from django.shortcuts import render
from django.http import HttpResponse

rounds = [
    {
        "number": "1",
        "players": [
            {"name": "Aleix Dominguez", "points": 10, "deck":"Atraxa, Grand Unifier", "icons": ["g", "w", "u", "b"]},
            {"name": "Eros Montero", "points": 9, "deck":"Legolas, Master Archer", "icons": ["g"]},
            {"name": "Beto Berdegal", "points": 8, "deck":"Ghyrson Starn, Kelermorph", "icons": ["r", "u"]},
            {"name": "Carlos Pedrosa", "points": 7, "deck":"Ghyrson Starn, Kelermorph", "icons": ["r", "u"]},
            {"name": "Alex Garcia", "points": 6, "deck":"Malcom, Truhan Seductor", "icons": ["u"]},
            {"name": "Victor Pedrosa", "points": 5, "deck":"Zoyowa, Lava-tongue", "icons": ["b", "r"]},
            {"name": "Eudald Cumalat", "points": 4, "deck":"Emmara, Soul of the Accord", "icons": ["g", "w"]},
            {"name": "Marcos Aguilar", "points": 3, "deck":"Marchesa, Dealer of Death", "icons": ["r", "u", "b"]},
            {"name": "Marc Pelegri", "points": 2, "deck":"Ghyrson Starn, Kelermorph", "icons": ["r", "u"]},
            {"name": "Codina", "points": 1, "deck":"Hazel of the Rootbloom", "icons": ["g", "b"]}
        ]
    },
    {
        "number": "2",
        "players": [
            {"name": "Marcos Aguilar", "points": 10, "deck":"Marchesa, Dealer of Death", "icons": ["r", "u", "b"]},
            {"name": "Beto Berdegal", "points": 9, "deck":"Ghyrson Starn, Kelermorph", "icons": ["r", "u"]},
            {"name": "Alex Garcia", "points": 8, "deck":"Malcom, Truhan Seductor", "icons": ["u"]},
            {"name": "Javier Ruiz", "points": 7, "deck":"The Ancient One", "icons": ["u", "b"]},
            {"name": "Aleix Dominguez", "points": 6, "deck":"Atraxa, Grand Unifier", "icons": ["g", "w", "u", "b"]},
            {"name": "Codina", "points": 5, "deck":"Laughing Jasper Flint", "icons": ["b", "r"]}
        ]
    },
    {
        "number": "3",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "4",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "5",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "6",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "7",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "8",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "9",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    },
    {
        "number": "10",
        "players": [
            {"name": "", "points": 10, "deck":""},
            {"name": "", "points": 9, "deck":""},
            {"name": "", "points": 8, "deck":""},
            {"name": "", "points": 7, "deck":""},
            {"name": "", "points": 6, "deck":""},
            {"name": "", "points": 5, "deck":""},
            {"name": "", "points": 4, "deck":""},
            {"name": "", "points": 3, "deck":""},
            {"name": "", "points": 2, "deck":""},
            {"name": "", "points": 1, "deck":""}
        ]
    }
    ]

def home(request):
    player_totals = {}
    # Dictionary to store the count of rounds for each player
    player_rounds = {}

    # Iterate over each round
    for round_data in rounds:  # 'rounds' is accessible here
        for player in round_data["players"]:
            if player["name"] != "":
                player_name = player["name"]
                player_points = player["points"]
            else:
                break
            # Initialize the player's total points and rounds if not already present
            if player_name not in player_totals:
                player_totals[player_name] = []
                player_rounds[player_name] = 0  # Initialize round count

            # Append the points to the player's total points list
            player_totals[player_name].append(player_points)
            player_rounds[player_name] += 1  # Increment round count

    # Dictionary to store the best 7 results for each player
    best_player_totals = {}

    for player_name, points in player_totals.items():
        # Sort points and take the best 7 results
        best_points = sorted(points, reverse=True)[:7]
        best_player_totals[player_name] = sum(best_points)

    # Create an ordered list of players by their total points (descending order)
    ordered_players = sorted(best_player_totals.items(), key=lambda x: x[1], reverse=True)

    # Create a summary of players with their total points and rounds
    player_summary = [
        (name, total_points, player_rounds[name]) for name, total_points in ordered_players
    ]


    return render(request, 'standings/home.html', {'standings': player_summary})

def tornejos(request):
    return render(request, 'standings/rondes.html', {'rounds': rounds})
# Create your views here.
