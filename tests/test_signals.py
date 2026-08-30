from src.signals import calculate_vwap

def test_calculate_vwap():
    """
    Function to test vwap function that it is not None.
    """
    prices = [50,51,52]
    volumes = [100,200,150]

    result = calculate_vwap(prices, volumes)

    assert result is not None