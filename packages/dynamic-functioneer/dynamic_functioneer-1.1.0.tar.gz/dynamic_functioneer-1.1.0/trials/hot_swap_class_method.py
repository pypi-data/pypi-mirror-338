from dynamic_functioneer.dynamic_decorator import dynamic_function

# 🔧 Custom prompt (inline string)
CUSTOM_PROMPT = """\
The following class method returns a list of even numbers. Your task is to improve it for large inputs \
by returning a generator expression instead of a list to improve memory efficiency.

Make sure to preserve the method's interface and documentation.

{code}
"""

class DataAnalyzer:
    """
    Analyzes numerical datasets with custom filtering logic.
    """

    @dynamic_function(
        model="gpt-4o-mini",
        hs_condition="len(numbers) > 10",  # Trigger hot-swap when input is large
        hs_model="gpt-4o-mini",
        hs_prompt=CUSTOM_PROMPT,
        extra_info="Filter even numbers from a list. Optimize for memory efficiency if input is large.",
        fix_dynamically=False
    )
    def filter_even_numbers(self, numbers):
        """
        Filters even numbers from the given list.

        Args:
            numbers (list of int): A list of integers.

        Returns:
            list or generator: The even numbers from the input.
        """
        pass


if __name__ == "__main__":
    analyzer = DataAnalyzer()

    print("=== BEFORE HOT-SWAP ===")
    print("Filtered (small list):", list(analyzer.filter_even_numbers([1, 2, 3, 4])))

    print("\n=== TRIGGERING HOT-SWAP ===")
    large_data = list(range(100))
    print("Filtered (large list):", list(analyzer.filter_even_numbers(large_data)))

    print("\n=== AFTER HOT-SWAP ===")
    print("Filtered (medium list):", list(analyzer.filter_even_numbers([10, 15, 18, 21, 22])))
