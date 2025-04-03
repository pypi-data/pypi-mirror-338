import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import efin  # Now Python should find the package

def test_dcf():
    result = efin.dcf("AAPL", 5)
    expected_keys = {"forecast_fcfs", "discounted_fcfs", "terminal_value", "discounted_terminal_value", "total_dcf_value"}
    assert set(result.keys()) == expected_keys
