def calculate_vwap(prices: float, volume: int) -> float:
    """
    Function to calculate vwap.
    """
    return (prices * volume).sum() / volume.sum()