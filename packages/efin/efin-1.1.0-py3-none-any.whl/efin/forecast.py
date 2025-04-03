import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import logging

logger = logging.getLogger(__name__)

def _get_time_series(ticker, start_date):
    """
    Download historical stock data for the given ticker and return the Adjusted Close series.

    Parameters:
      ticker (str): Stock ticker (e.g., "AAPL").
      start_date (str): Start date for historical data (format 'YYYY-MM-DD').

    Returns:
      pandas.Series: Time series of Adjusted Close prices.

    Raises:
      ValueError: If neither 'Adj Close' nor 'Close' is found in the data.
    """
    data = yf.download(ticker, start=start_date, auto_adjust=False)
    if "Adj Close" in data.columns:
        return data["Adj Close"]
    elif "Close" in data.columns:
        logger.warning("'Adj Close' not found; falling back to 'Close'.")
        return data["Close"]
    else:
        raise ValueError("Neither 'Adj Close' nor 'Close' found in the downloaded data.")

def forecast_arima(ticker, order=(1, 1, 1), forecast_period=5, start_date='2010-01-01'):
    """
    Forecast stock Adjusted Close prices using an ARIMA model.

    Parameters:
      ticker (str): Stock ticker symbol (e.g., "AAPL").
      order (tuple): The (p, d, q) order for the ARIMA model.
      forecast_period (int): Number of periods to forecast.
      start_date (str): Start date for historical data.

    Returns:
      pandas.Series: Forecasted values.
    """
    try:
        ts = _get_time_series(ticker, start_date)
        model = ARIMA(ts, order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=forecast_period)
        return forecast
    except Exception as e:
        logger.error(f"ARIMA forecast error for {ticker}: {e}")
        raise

def forecast_sarima(ticker, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12), forecast_period=5, start_date='2010-01-01'):
    """
    Forecast stock Adjusted Close prices using a SARIMA model.

    Parameters:
      ticker (str): Stock ticker symbol (e.g., "AAPL").
      order (tuple): The (p, d, q) order for the model.
      seasonal_order (tuple): The seasonal order (P, D, Q, s).
      forecast_period (int): Number of periods to forecast.
      start_date (str): Start date for historical data.

    Returns:
      pandas.Series: Forecasted values.
    """
    try:
        ts = _get_time_series(ticker, start_date)
        model = SARIMAX(ts, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
        forecast = model_fit.forecast(steps=forecast_period)
        return forecast
    except Exception as e:
        logger.error(f"SARIMA forecast error for {ticker}: {e}")
        raise

def forecast_sarimax(ticker, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12),
                     forecast_period=5, exog=None, start_date='2010-01-01'):
    """
    Forecast stock Adjusted Close prices using a SARIMAX model with optional exogenous variables.

    Parameters:
      ticker (str): Stock ticker symbol (e.g., "AAPL").
      order (tuple): The (p, d, q) order.
      seasonal_order (tuple): The seasonal order (P, D, Q, s).
      forecast_period (int): Number of periods to forecast.
      exog (pandas.DataFrame, optional): Exogenous variables aligned with the time series.
      start_date (str): Start date for historical data.

    Returns:
      pandas.Series: Forecasted values.

    Note:
      If exogenous variables are used, future exog values must be provided for forecasting.
    """
    try:
        ts = _get_time_series(ticker, start_date)
        if exog is not None:
            model = SARIMAX(ts, exog=exog, order=order, seasonal_order=seasonal_order)
        else:
            model = SARIMAX(ts, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
        forecast = model_fit.forecast(steps=forecast_period, exog=exog)
        return forecast
    except Exception as e:
        logger.error(f"SARIMAX forecast error for {ticker}: {e}")
        raise
