# Warehouse CLI Project

## Overview

This is a simple command-line interface (CLI) for managing a warehouse. It allows users to interact with the database by performing various operations related to categories, employees, and products.

***

## Prerequisites

- **Python 3.x**: Python is a high-level, general-purpose programming language.

## Entity Relationship Diagram

The ERD diagram was built using `dbdiagram.io` and can be seen through this [link](https://dbdiagram.io/d/Simple-WareHouse-Inventory-System-657c1ef656d8064ca016b86f)

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/chyvail/Cli-Project.git

2. Change directory to folder

   ```bash
   cd Cli-Project

3. Set up a virtual environment using pipenv

   ```bash
   pipenv install && pipenv shell

4. Change directory to lib and apply migation to database

   ```bash
   cd lib;alembic upgrade head

5. Alternatively you can use the existing `wharehouse.db` file if you dont want to generate yours. Skip step 4 for this

***

## Features and Usage

Present features and how to use the `click cli`

1. Add Category

   ```bash
   python3 main.py add_category --name <category_name>

2. Show Category

   ```bash
   python3 main.py show_categories

3. Update Category

   ```bash
   python3 main.py update_category --originalname <original_category_name> --newname <new_category_name>

4. Delete Category

   ```bash
   python3 main.py delete_category --categoryname <category_name>

5. Add Employee

   ```bash
   python3 main.py add_employee --fname <first_name> --lname <last_name> --email <employee_email>

6. Show Employees

   ```bash
   python3 main.py show_employees

7. Update Employee

   ```bash
   python3 main.py update_employee --oldemail <old_email> --newemail <new_email>

8. Delete Employee

   ```bash
   python3 main.py delete_employee --employee_email <employee_email>

9. Add Product

   ```bash
   python3 main.py add_product --name <product_name> --size <product_size> --quantity <product_quantity> --category <category_id> --added_by <employee_id>

10. Show Products

   ```bash
   python main.py show_products

11. Update Product

   ```bash
   python main.py update_product --productid <product_id> --newquantity <new_quantity>


















