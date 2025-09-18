def rolling_mean(xs, w):
    if w <= 0 or w > len(xs):
        return []
    means = []
    for i in range(len(xs) - w + 1):
        window = xs[i:i+w]
        means.append(sum(window) / w)
    return means

if __name__ == "__main__":
    # Take input from user
    xs_input = input("Enter the list of numbers (comma separated): ")
    xs = [float(x.strip()) for x in xs_input.split(",") if x.strip()]
    w = int(input("Enter window size: "))
    result = rolling_mean(xs, w)
    print("Rolling means:", result)
