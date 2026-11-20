from tabulate import tabulate

def print_table(data):
    table = tabulate(
        data,
        headers='keys',
        tablefmt='fancy_grid',
        floatfmt=',.2f',
        missingval='N/A'
    )

    print(table)