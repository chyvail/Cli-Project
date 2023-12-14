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

# ADD PRODUCTS

@main.command()
@click.option('--name','-pn',prompt=True)
@click.option('--size','-ps',prompt=True)
@click.option('--quantity','-pq',prompt=True)
@click.option('--category','-pc',prompt=True)
@click.option('--added_by','-ab',prompt=True)

def add_product(name,size,quantity,category,added_by):
    """Adds Products to Database"""

    product_data = [
        ['Product Data','Values'],
        ['Product Name',name],
        ['Product Size',size],
        ['Product Quantity',quantity],
        ['Product Category',category],
        ['Added By',added_by]
    ]

    product_table = AsciiTable(product_data)
    
    click.echo(product_table.table)

    new_product = Product(product_name=name,
                          product_size=size,
                          product_quantity=quantity,
                          product_category=category,
                          added_by=added_by)
    
    session.add(new_product)
    session.commit()

    click.secho("Saved Input to Product Table",fg="yellow")

if __name__ == "__main__":
    main()