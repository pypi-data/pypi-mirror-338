from dynamic_functioneer.dynamic_decorator import dynamic_function

# Define your own custom hot-swapping prompt as a string (instead of a file)
CUSTOM_HOTSWAP_PROMPT = """\
Improve the following Python function to return the square root of x (use x**0.5), \
instead of squaring it. The current code is:

{code}
"""

@dynamic_function(
    model="gemini-2.0-flash",
    hs_condition="x > 1000",  # The hot-swap should trigger only when x is large
    hs_model="gpt-4o-mini",
    hs_prompt=CUSTOM_HOTSWAP_PROMPT,
    extra_info="Returns the square of x. If x is large, change behavior to return square root.",
    fix_dynamically=False  # disable recovery retries for clarity in this test
)
def square_or_root(x):
    """
    Returns x squared unless x is very large, in which case the function will be hot-swapped to return the square root.
    """
    pass


if __name__ == "__main__":
    # This should trigger initial LLM-based code generation (returns x**2)
    print("Before hot-swap (x = 10):", square_or_root(10))

    # This should trigger a hot-swap (since x > 1000), and LLM will rewrite the logic to return x**0.5
    print("Triggering hot-swap (x = 2025):", square_or_root(2025))

    # Now calling with a small number should use the updated logic (x**0.5 instead of x**2)
    print("After hot-swap (x = 100):", square_or_root(100))
