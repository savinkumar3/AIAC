def fare(rides, base_per_km=22.0, surgeMultiplier=2.0):
    """
    Calculate fares for a list of rides.
    Each ride is a dict with 'time' (HH:MM, 24h) and 'km' (float).
    Surge applies strictly after 18:00 (i.e., 18:01 and later).
    Returns a list of fares, rounded to 2 decimals.
    """
    result = []
    for ride in rides:
        # Validate keys
        if 'time' not in ride or 'km' not in ride:
            raise KeyError("Each ride must have 'time' and 'km' keys")
        time_str = ride['time']
        km = ride['km']
        # Parse time
        try:
            hour_str, min_str = time_str.split(":")
            hour = int(hour_str)
            minute = int(min_str)
        except Exception:
            raise ValueError(f"Invalid time format: {time_str}")
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError(f"Invalid time value: {time_str}")
        # Determine if surge applies
        if hour > 18 or (hour == 18 and minute > 0):
            multiplier = surgeMultiplier
        else:
            multiplier = 1.0
        # Calculate fare
        fare_val = km * base_per_km * multiplier
        # Round to 2 decimals
        fare_val = round(fare_val + 1e-8, 2)
        result.append(fare_val)
    return result

if __name__ == "__main__":
    # Quick test
    test_rides = [
        {'time': '08:00', 'km': 3.0},
        {'time': '18:01', 'km': 3.0},
        {'time': '18:00', 'km': 3.0},
        {'time': '20:30', 'km': 5.0}
    ]
    print("Test fares:", fare(test_rides))
    # User input
    n = int(input("Enter number of rides: "))
    user_rides = []
    for i in range(n):
        t = input(f"Enter time for ride {i+1} (HH:MM): ")
        k = float(input(f"Enter km for ride {i+1}: "))
        user_rides.append({'time': t, 'km': k})
    print("Calculated fares:", fare(user_rides))

