import click
from terminaltables import AsciiTable
from model import Product,Category,Employee,session

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

# DISPLAY CATEGORIES
@main.command() 
def show_categories():
    """Shows all available categories in Category Table"""
    all_categories = session.query(Category).all()
    click.secho("All Available Categories shown below",fg="yellow")

    category_data = [["Category Id", "Category Name"]]
    for category in all_categories:
        category_data.append([category.id, category.category_name])

    category_table = AsciiTable(category_data)
    
    click.echo(category_table.table)

# UPDATE CATEGORIES
@main.command()
@click.option('--originalname','-on',prompt=True)
@click.option('--newname','-nn',prompt=True)

def update_category(originalname, newname):
    """Update Category Name"""
    category_update = session.query(Category).filter(Category.category_name == originalname).first()
    category_update.category_name = newname
    session.commit()

    click.secho("Category Name Updated",fg="green")

# ADD EMPLOYEES
@main.command()
@click.option('--fname','-fn',prompt=True)
@click.option('--lname','-ln',prompt=True)
@click.option('--email','-em',prompt=True)

def add_employee(fname,lname,email):
    """Add Employees to Database"""

    employee_data = [
        ['Employee Data','Employee Values'],
        ['First Name',fname],
        ['Last Name',lname],
        ['Email',email]
    ]

    employee_table = AsciiTable(employee_data)

    click.echo(employee_table.table)

    new_employee = Employee(employee_firstname = fname, employee_lastname = lname, employee_email = email)
    session.add(new_employee)
    session.commit()

    click.secho("Saved Input to Employee Table",fg="yellow")

# DISPLAY EMPLOYEES
@main.command()
def show_employees():
    """Show all employees Available"""
    all_employees = session.query(Employee).all()
    click.secho("All Available Employees shown below",fg="yellow")

    employee_data = [["Employee Id", "Employee First Name","Employee Last Name","Employee Email"]]
    for employee in all_employees:
        employee_data.append([employee.id, employee.employee_firstname,employee.employee_lastname,employee.employee_email])

    employee_table = AsciiTable(employee_data)
    
    click.echo(employee_table.table)

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

# DISPLAY PRODUCTS

@main.command()
def show_products():
    """Show all Products available in Database"""
    all_products = session.query(Product).all()
    click.secho("All Available Products shown below",fg="yellow")

    product_data = [["Product Id", "Product Name","Product Size","Product Quantity","Added By"]]
    for product in all_products:
        product_data.append([product.id, product.product_name, product.product_size, product.product_quantity, product.product_category])

    product_table = AsciiTable(product_data)
    
    click.echo(product_table.table)

if __name__ == "__main__":
    main()