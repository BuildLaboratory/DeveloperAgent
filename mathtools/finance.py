"""Simple financial calculations."""


def simple_interest(principal: float, rate_percent: float, years: float) -> float:
    """Return the interest earned with simple interest."""
    return principal * rate_percent / 100 * years


def compound_interest(principal: float, rate_percent: float, years: int) -> float:
    """Return the final amount (principal + interest) with yearly compounding."""
    return principal * (1 + rate_percent / 100) ** years


def annuity_payment(principal: float, rate_percent: float, years: int) -> float:
    """Return the yearly payment to repay a loan in equal instalments."""
    if years <= 0:
        raise ValueError("years must be > 0.")
    rate = rate_percent / 100
    if rate == 0:
        return principal / years
    return principal * rate / (1 - (1 + rate) ** -years)


def break_even_units(fixed_costs: float, price: float, variable_cost: float) -> float:
    """Return the number of units needed to cover all costs."""
    contribution_margin = price - variable_cost
    if contribution_margin <= 0:
        raise ValueError("price must be higher than variable_cost.")
    return fixed_costs / contribution_margin
