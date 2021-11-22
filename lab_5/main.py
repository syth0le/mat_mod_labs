from numpy import std
from rich.console import Console
from rich.table import Table

from accuracy import Accuracy
from draw_graphic import drawGraphic
from integration import Analytical, MonteCarloFirst, MonteCarloSecond, Trapezium


def main():
    console = Console()
    table_nodes = Table(title='Number of nodes for getting 1 percent accuracy for each method.')
    table_nodes.add_column('Method name', justify='right', style='cyan', no_wrap=True)
    table_nodes.add_column('Number of nodes', style='magenta')

    table_integration = Table(title='Main Table Info')
    table_integration.add_column('Title', justify='right', style='cyan', no_wrap=True)
    table_integration.add_column('Title', style='magenta')

    trapezium = Accuracy.investigate_num_of_nodes_to_1_percent_accuracy(Trapezium.count)
    monte_carlo_first = Accuracy.investigate_num_of_nodes_to_1_percent_accuracy(MonteCarloFirst.count)
    monte_carlo_second = Accuracy.investigate_num_of_nodes_to_1_percent_accuracy(MonteCarloSecond.count)

    table_nodes.add_row('Num of nodes', str(trapezium))
    # table_nodes.add_row(str(Trapezium()), str(trapezium))
    # table_nodes.add_row(str(MonteCarloFirst()), str(monte_carlo_first))
    # table_nodes.add_row(str(MonteCarloSecond()), str(monte_carlo_second))

    table_integration.add_row('Analytic count', str(round(Analytical.count(), 3)))
    table_integration.add_row('Trapezium method count', str(round(Trapezium.count(trapezium), 3)))
    table_integration.add_row()
    table_integration.add_row('Monte-Carlo 1st method count', str(round(MonteCarloFirst.count(trapezium), 3)))
    table_integration.add_row('Monte-Carlo 2nd method count', str(round(MonteCarloSecond.count(trapezium), 3)))
    table_integration.add_row()
    table_integration.add_row('Standard deviation for 1st method',
                              str(round(std([MonteCarloFirst.count(trapezium) for _ in range(100)]), 3)))  # trapezium
    table_integration.add_row('Standard deviation for 2nd method',
                              str(round(std([MonteCarloSecond.count(trapezium) for _ in range(100)]), 3)))  # trapezium

    console.print(table_nodes)
    console.print(table_integration)
    drawGraphic()


if __name__ == '__main__':
    main()
