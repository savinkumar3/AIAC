def run_test_cases():
    test_cases = [
        # (input, expected_output or expected_exception)
        ("2023-12-31", "31-12-2023"),
        ("1999-01-01", "01-01-1999"),
        ("2020-02-29", "29-02-2020"),
        ("0001-01-01", "01-01-0001"),
        ("2023-6-7", "7-6-2023"),
        ("2023-06-07", "07-06-2023"),
        ("2023-13-01", "01-13-2023"),  # No month validation in logic
        ("2023-00-00", "00-00-2023"),  # No validation in logic
        ("2023-12", ValueError),
        ("2023/12/31", ValueError),
        ("", ValueError),
        ("2023-12-31-01", ValueError),
        ("2023-12-31\n", "31-12-2023\n"),  # If input has newline, will be part of output
        ("abcd-ef-gh", "gh-ef-abcd"),
        ("2023-12-31-00", ValueError),
        ("2023--12-31", ValueError),
    ]

    from task_5 import convert_date_format

    passed = 0
    for idx, (input_str, expected) in enumerate(test_cases, 1):
        try:
            result = convert_date_format(input_str)
            if isinstance(expected, type) and issubclass(expected, Exception):
                print(f"Test case {idx}: '{input_str}' -> Expected exception {expected.__name__}, but got result '{result}' [FAIL]")
            elif result == expected:
                print(f"Test case {idx}: '{input_str}' -> Expected: '{expected}', Got: '{result}' [PASS]")
                passed += 1
            else:
                print(f"Test case {idx}: '{input_str}' -> Expected: '{expected}', Got: '{result}' [FAIL]")
        except Exception as e:
            if isinstance(expected, type) and isinstance(e, expected):
                print(f"Test case {idx}: '{input_str}' -> Expected exception {expected.__name__}, Got exception {type(e).__name__} [PASS]")
                passed += 1
            else:
                print(f"Test case {idx}: '{input_str}' -> Expected: '{expected}', Got exception {type(e).__name__} [FAIL]")

    print(f"\n{passed}/{len(test_cases)} test cases passed.")

if __name__ == "__main__":
    run_test_cases()





