import click
from vedic_finance_engine.finance.simple_interest import calculate_simple_interest
from vedic_finance_engine.finance.emi import calculate_emi

@click.group()
def cli():
    pass

@cli.command()
@click.option("--p", required=True, type=float)
@click.option("--r", required=True, type=float)
@click.option("--t", required=True, type=float)
def si(p, r, t):
    result = calculate_simple_interest(p, r, t)
    click.echo(f"Simple Interest: {result}")

@cli.command()
@click.option("--p", required=True, type=float)
@click.option("--rate", required=True, type=float)
@click.option("--years", required=True, type=int)
def emi(p, rate, years):
    result = calculate_emi(p, rate, years)
    click.echo(f"EMI: {result}")