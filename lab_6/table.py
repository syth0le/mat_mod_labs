from rich.console import Console
from rich.table import Table


def print_table(gss: tuple, fib: tuple) -> None:
    console = Console()
    table = Table(title='Find Function Extremum')
    table.add_column('Method name', justify='right', style='cyan', no_wrap=True)
    table.add_column('function in Xm value', style='magenta')
    table.add_column('Xm dot value', style='red')
    table.add_column('Counted iterations number', style='green')

    table.add_row('Golden-Section Method', *list(map(str, gss)))
    table.add_row('Fibonacci Method', *list(map(str, fib)))
    console.print(table)
