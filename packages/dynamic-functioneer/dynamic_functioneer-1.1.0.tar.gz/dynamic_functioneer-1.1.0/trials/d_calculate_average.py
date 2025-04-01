def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list of float): A list of numeric values.

    Returns:
        float: The average of the list.
    """
    # Ensure the list is not empty to avoid division by zero.
    if not numbers:
        return 0.0

    # Calculate the sum of the numbers.
    total = sum(numbers)

    # Calculate the average by dividing the sum by the number of elements.
    average = total / len(numbers)

    return average