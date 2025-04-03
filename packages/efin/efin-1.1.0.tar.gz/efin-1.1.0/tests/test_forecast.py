import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import efin
import pandas as pd

def test_forecast_arima():
    forecast = efin.forecast_arima("AAPL", order=(1,1,1), forecast_period=3)
    # Check that forecast is a pandas Series and has expected length
    assert hasattr(forecast, 'shape')
    assert len(forecast) == 3

def test_forecast_sarima():
    forecast = efin.forecast_sarima("AAPL", order=(1,1,1), seasonal_order=(1,1,1,12), forecast_period=3)
    assert hasattr(forecast, 'shape')
    assert len(forecast) == 3

def test_forecast_sarimax():
    forecast = efin.forecast_sarimax("AAPL", order=(1,1,1), seasonal_order=(1,1,1,12), forecast_period=3)
    assert hasattr(forecast, 'shape')
    assert len(forecast) == 3
