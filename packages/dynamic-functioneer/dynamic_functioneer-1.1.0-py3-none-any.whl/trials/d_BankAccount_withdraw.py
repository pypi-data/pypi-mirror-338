def withdraw(self, amount):
    """
    Withdraws the given amount from the account.

    Args:
        amount (float): The amount to withdraw.

    Returns:
        float: The updated balance after the withdrawal.

    Raises:
        ValueError: If the withdrawal amount is negative.
        ValueError: If the account does not have sufficient funds.
    """
    # Check if the withdrawal amount is negative
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")

    # Check if the account has sufficient funds
    if self.balance < amount:
        raise ValueError("Insufficient funds in the account.")

    # Calculate the updated balance
    updated_balance = self.balance - amount

    # Update the balance
    self.balance = updated_balance

    # Return the updated balance
    return updated_balance