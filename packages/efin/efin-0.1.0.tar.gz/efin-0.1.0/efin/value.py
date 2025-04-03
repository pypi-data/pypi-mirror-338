"""
Module: value
Provides valuation calculations such as a DCF model using real financial data.
"""

import yfinance as yf

def _get_real_fcf(ticker):
    """
    Retrieve the most recent free cash flow (FCF) from Yahoo Finance using yfinance.
    FCF is calculated as:
    
        FCF = Total Cash From Operating Activities + Capital Expenditures
    
    Returns the value in billions USD.
    """
    try:
        data = yf.Ticker(ticker)
        cashflow = data.cashflow
        operating_cf = cashflow.loc["Operating Cash Flow"].iloc[0]
        capex = cashflow.loc["Capital Expenditure"].iloc[0]
        free_cash_flow = operating_cf + capex
        free_cash_flow_billion = free_cash_flow / 1e9
        return free_cash_flow_billion
    except Exception as e:
        print(f"Error retrieving FCF data for {ticker}: {e}")
        return 50.0  # Default value if an error occurs

def dcf(ticker, years, discount_rate=0.10, growth_rate=0.05, terminal_growth_rate=0.02):
    """
    Calculate the Discounted Cash Flow (DCF) valuation.
    
    Parameters:
      ticker (str): Stock ticker (e.g., "AAPL").
      years (int): Number of forecast years.
      discount_rate (float): Discount rate (default: 10%).
      growth_rate (float): Annual growth rate of FCF (default: 5%).
      terminal_growth_rate (float): Perpetual growth rate for terminal value (default: 2%).
    
    Returns:
      dict: Contains forecasted FCFs, discounted FCFs, terminal value, and total DCF value.
    """
    base_fcf = _get_real_fcf(ticker)
    
    forecast = {}
    discounted_forecast = {}
    total_discounted_value = 0.0

    # Forecast and discount FCF for each year.
    for i in range(1, years + 1):
        forecast[i] = base_fcf * ((1 + growth_rate) ** i)
        discounted_value = forecast[i] / ((1 + discount_rate) ** i)
        discounted_forecast[i] = discounted_value
        total_discounted_value += discounted_value

    # Terminal value using the Gordon Growth Model.
    terminal_cash_flow = base_fcf * ((1 + growth_rate) ** years)
    terminal_value = terminal_cash_flow * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)
    total_discounted_value += discounted_terminal_value

    return {
        "forecast_fcfs": forecast,
        " "
        "discounted_fcfs": discounted_forecast,
        " "
        "terminal_value": terminal_value,
        " "
        "discounted_terminal_value": discounted_terminal_value,
        " "
        "total_dcf_value": total_discounted_value
    }
