from typing import List, Tuple

def linear_search(arr: List[int], target: int, sorted_list: bool = False) -> Tuple[int, int]:
    comparisons = 0
    print("\n--- Comparison Steps ---")
    for i, val in enumerate(arr):
        comparisons += 1
        print(f"Step {comparisons}: Compare target({target}) with arr[{i}] = {val}", end="")
        if val == target:
            print(" → Match found!")
            return i, comparisons
        if sorted_list and val > target:
            print(" → Early exit: Cannot exist further.")
            return -1, comparisons
        print()
    print("→ Target not found.")
    return -1, comparisons

if __name__ == "__main__":
    print("---- Linear Search Program ----\n")
    sorted_list = input("Is the list sorted? (yes/no): ").strip().lower() == "yes"
    n = int(input("Enter number of elements: "))
    arr = [int(input()) for _ in range(n)]
    print(f"\nOriginal List: {arr}")
    if sorted_list:
        arr.sort()
        print(f"Sorted List: {arr}")
    target = int(input("\nEnter target value: "))
    idx, comps = linear_search(arr, target, sorted_list)
    print(f"\n---- Result ----\nTarget: {target}\nIndex: {idx}\nComparisons: {comps}")
