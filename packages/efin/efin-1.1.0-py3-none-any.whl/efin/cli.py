import click
import efin

@click.group()
def cli():
    """Efin: A Financial Analysis Toolkit"""
    pass

@cli.command()
@click.argument('ticker')
@click.option('--years', default=5, help='Number of years for DCF calculation.')
def dcf(ticker, years):
    """Calculate DCF valuation for a given TICKER."""
    result = efin.dcf(ticker, years)
    click.echo(f"DCF Valuation for {ticker}: {result['total_dcf_value']:.2f} billion USD")

@cli.command()
@click.argument('ticker')
@click.option('--model', default='arima', help='Forecast model (arima, sarima, sarimax, prophet).')
@click.option('--period', default=5, help='Forecast period (number of days).')
def forecast(ticker, model, period):
    """Forecast stock prices for a given TICKER."""
    if model.lower() == 'arima':
        forecast = efin.forecast_arima(ticker, forecast_period=period)
    elif model.lower() == 'sarima':
        forecast = efin.forecast_sarima(ticker, forecast_period=period)
    elif model.lower() == 'sarimax':
        forecast = efin.forecast_sarimax(ticker, forecast_period=period)
    elif model.lower() == 'prophet':
        forecast = efin.forecast_prophet(ticker, forecast_period=period)
    else:
        click.echo("Invalid model specified.")
        return
    click.echo(f"Forecast for {ticker}:")
    click.echo(forecast)

if __name__ == '__main__':
    cli()
