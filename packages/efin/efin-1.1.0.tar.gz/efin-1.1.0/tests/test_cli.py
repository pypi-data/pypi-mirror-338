import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from click.testing import CliRunner
from efin import cli

def test_cli_dcf():
    runner = CliRunner()
    result = runner.invoke(cli, ["dcf", "AAPL", "--years", "5"])
    assert "DCF Valuation for AAPL" in result.output

def test_cli_forecast():
    runner = CliRunner()
    result = runner.invoke(cli, ["forecast", "AAPL", "--model", "arima", "--period", "5"])
    assert "Forecast for AAPL" in result.output
