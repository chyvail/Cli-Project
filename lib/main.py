import click
from terminaltables import AsciiTable
from model import Product,Category,session

@click.group() # decorator used to define a group of commands
@click.version_option(version="1.0",prog_name="WhareHouse Manager CLI") # run python3 main.py --help or --version to see:

def main():
    """Simple WhareHouse Manager CLI"""
    pass

# ADD CATEGORY
@main.command() 
@click.option('--name','-cn',prompt=True)

def add_category(name):
    """Adds Product Categories to Database"""

    category_data = [
        ['Category Data','Category Value'],
        ['Category Name',name]
    ]

    category_table = AsciiTable(category_data)

    click.echo(category_table.table)

    new_category = Category(category_name = name)

    session.add(new_category)
    session.commit()

    click.secho("Saved Input to Category Table",fg="yellow")

if __name__ == "__main__":
    main()