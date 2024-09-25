from django.shortcuts import render
from django.http import HttpResponse

rounds = [
    {
        "number": "1",
        "players": [
            {"name": "Player 1", "points": 10},
            {"name": "Player 2", "points": 9},
            {"name": "Player 3", "points": 8},
            {"name": "Player 4", "points": 7},
            {"name": "Player 5", "points": 6},
            {"name": "Player 6", "points": 5},
            {"name": "Player 7", "points": 4},
            {"name": "Player 8", "points": 3},
            {"name": "Player 9", "points": 2},
            {"name": "Player 10", "points": 1}
        ]
    },
    {
        "number": "2",
        "players": [
            {"name": "Player 1", "points": 10},
            {"name": "Player 2", "points": 9},
            {"name": "Player 3", "points": 8},
            {"name": "Player 4", "points": 7},
            {"name": "Player 5", "points": 6},
            {"name": "Player 6", "points": 5},
            {"name": "Player 7", "points": 4},
            {"name": "Player 8", "points": 3},
            {"name": "Player 9", "points": 2},
            {"name": "Player 10", "points": 1}
        ]
    },
    {
        "number": "3",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "4",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "5",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "6",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "7",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "8",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "9",
        "players": [
            {"name": "Player 1", "points": 10}
        ]
    },
    {
        "number": "10",
        "players": [
            {"name": "Player 1", "points": 10}
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
            player_name = player["name"]
            player_points = player["points"]

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
