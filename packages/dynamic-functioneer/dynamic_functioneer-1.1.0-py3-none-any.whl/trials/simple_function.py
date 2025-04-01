# import sys
# print("Interactive shell sys.path:")
# for p in sys.path:
#     print(p)



# import sys
# print(sys.executable)


from dynamic_functioneer.dynamic_decorator import dynamic_function

@dynamic_function(
        model="gemini-2.0-flash"
)
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list of float): A list of numeric values.

    Returns:
        float: The average of the list.
    """
    pass


print(calculate_average([1, 3, 7]))
