from dynamic_functioneer.dynamic_decorator import dynamic_function

@dynamic_function(
    model="gpt-4o-mini",
    hs_condition="len(data) > 5",  # When this is True, it triggers the hot-swap
    hs_model="gpt-4o-mini",             # Can be same or different model
    # hs_prompt=None means: use default hot_swapping_prompt.txt
    extra_info="Returns the sum of even numbers in the list. Intended to be optimized for large lists."
)
def inefficient_sum_of_evens(data):
    """
    Returns the sum of even numbers in a list.

    Args:
        data (list of int): List of integers.

    Returns:
        int: Sum of even numbers.
    """
    pass


if __name__ == "__main__":
    print("=== BEFORE HOT-SWAP ===")
    print("Sum of evens [1, 2, 3, 4]:", inefficient_sum_of_evens([1, 2, 3, 4]))  # Should return 6

    print("\n=== TRIGGERING HOT-SWAP ===")
    large_input = list(range(100))  # Triggers the hs_condition: len(data) > 5
    print("Sum of evens (0 to 99):", inefficient_sum_of_evens(large_input))     # Should still return correct result

    print("\n=== AFTER HOT-SWAP ===")
    print("Sum of evens [10, 12, 13, 15]:", inefficient_sum_of_evens([10, 12, 13, 15]))  # Should still work
