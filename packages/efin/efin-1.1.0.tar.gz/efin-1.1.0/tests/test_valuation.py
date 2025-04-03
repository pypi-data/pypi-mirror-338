import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import efin

def test_ddm():
    # Use a known ticker with dividend data (e.g., "KO" for Coca-Cola)
    price = efin.dividend_discount_model("KO", growth_rate=0.03, discount_rate=0.1)
    assert price > 0

def test_comparable_analysis():
    result = efin.comparable_company_analysis("AAPL", ["MSFT", "GOOGL"], multiple="trailingPE")
    assert "target_ticker" in result
    assert "interpretation" in result

def test_residual_income():
    # This test assumes that bookValue and trailingEps data are available for "AAPL"
    value = efin.residual_income_model("AAPL", cost_of_equity=0.1, growth_rate=0.05, forecast_period=5)
    assert value > 0
