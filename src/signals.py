def calculate_vwap(prices: list[float], volumes: list[int]) -> float:
    """
    Function to calculate vwap.
    """
    weighted_sum: float = sum(price * volume for price, volume in zip(prices,volumes))
    return weighted_sum / sum(volumes)