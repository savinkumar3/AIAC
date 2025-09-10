def process_scores(scores):
    total = sum(scores)
    avg = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
process_scores([85, 92, 78, 90, 88])