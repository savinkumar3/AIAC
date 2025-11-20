"""
Gaming Leaderboard Sorting using Quick Sort
-------------------------------------------
This script demonstrates an AI-assisted implementation of Quick Sort
to sort a list of players based on their scores in descending order.

Author: THALLAPELLI SAVIN KUMAR
Date: 20-Nov-2025
"""

# Sample data structure: list of dictionaries
players = [
    {"name": "Alice", "score": 1500},
    {"name": "Bob", "score": 3000},
    {"name": "Charlie", "score": 2500},
    {"name": "David", "score": 2000},
    {"name": "Eve", "score": 3500}
]

# -------------------------------
# Quick Sort Implementation
# -------------------------------
def quick_sort(players_list):
    """
    Quick Sort function to sort players by score in descending order.
    
    Parameters:
    players_list (list of dict): List of player dictionaries with 'score' key
    
    Returns:
    list of dict: Sorted list of players by descending score
    """
    if len(players_list) <= 1:
        return players_list  # Base case: list with 0 or 1 element is already sorted

    # Choose pivot (last element)
    pivot = players_list[-1]
    pivot_score = pivot["score"]

    # Partition into left and right lists
    left = [player for player in players_list[:-1] if player["score"] >= pivot_score]
    right = [player for player in players_list[:-1] if player["score"] < pivot_score]

    # Recursively sort left and right, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

# -------------------------------
# Sort the leaderboard
# -------------------------------
sorted_leaderboard = quick_sort(players)

# Display results
print("Leaderboard (Highest Score First):")
for idx, player in enumerate(sorted_leaderboard, start=1):
    print(f"{idx}. {player['name']} - {player['score']}")

# -------------------------------
# Optional: Test Case
# -------------------------------
def test_quick_sort():
    test_players = [
        {"name": "A", "score": 50},
        {"name": "B", "score": 20},
        {"name": "C", "score": 30}
    ]
    sorted_test = quick_sort(test_players)
    expected_scores = [50, 30, 20]
    assert [p["score"] for p in sorted_test] == expected_scores
    print("Test passed!")

# Run test
test_quick_sort()
