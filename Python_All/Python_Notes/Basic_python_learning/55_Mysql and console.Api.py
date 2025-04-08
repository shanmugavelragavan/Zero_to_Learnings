from tabulate import tabulate
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from datetime import datetime
import mysql.connector


# rich output
console = Console()


# Connect to the database
def connect_to_database():
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="Fresh$321", database="python_db"
        )
        console.print("[bold green]Connected to the database successfully![/]")
        return con
    except mysql.connector.Error as e:
        console.print(f"[bold red]Database Connection Error: {e}[/]")
        exit()


# Insert data into the database
def insert_data(con, name, age, city):
    try:
        cursor = con.cursor()
        sql = "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, city))
        con.commit()
        console.print("[bold green]Data Inserted Successfully![/]")
    except mysql.connector.Error as e:
        console.print(f"[bold red]Error: {e}[/]")


# Update data in the database
def update_data(con, name, age, city, user_id):
    try:
        cursor = con.cursor()
        sql = "UPDATE users SET name=%s, age=%s, city=%s WHERE id=%s"
        cursor.execute(sql, (name, age, city, user_id))
        con.commit()
        console.print("[bold green]Data Updated Successfully![/]")
    except mysql.connector.Error as e:
        console.print(f"[bold red]Error: {e}[/]")


# Fetch and display data using rich's Table
def display_data(con):
    cursor = con.cursor()
    cursor.execute("SELECT ID, NAME, AGE, CITY FROM users")
    result = cursor.fetchall()


    # Create a table using rich's Table class
    table = Table(title="User Data")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Age", justify="right", style="green")
    table.add_column("City", style="yellow")


    # Add rows to the table
    for row in result:
        table.add_row(str(row[0]), row[1], str(row[2]), row[3])


    # Print the table
    console.print(table)


# Delete data from the database
def delete_data(con, user_id):
    try:
        cursor = con.cursor()
        sql = "DELETE FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))
        con.commit()
        console.print("[bold green]Data Deleted Successfully![/]")
    except mysql.connector.Error as e:
        console.print(f"[bold red]Error: {e}[/]")


# Prompt for user input with validation
def get_user_input(prompt_text, input_type=str, choices=None, default=None):
    if input_type == int:
        while True:
            user_input = Prompt.ask(prompt_text, default=default)
            if user_input.isdigit():
                return int(user_input)
            console.print("[bold red]Invalid input, please enter a number.[/]")
    elif input_type == str:
        return Prompt.ask(prompt_text, choices=choices, default=default)
    return None


# Display the menu options
def display_menu():
    console.print("[bold cyan]1.[/] Insert Data")
    console.print("[bold cyan]2.[/] Update Data")
    console.print("[bold cyan]3.[/] Select Data")
    console.print("[bold cyan]4.[/] Delete Data")
    console.print("[bold cyan]5.[/] Exit")
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    console.print(f"[bold green]Current Time: {current_time}[/]")


# Main program loop
def main():
    con = connect_to_database()

    while True:
        display_menu()
        choice = get_user_input("Enter Your Choice", int, choices=[1, 2, 3, 4, 5])

        if choice == 1:
            name = get_user_input("Enter Name: ")
            age = get_user_input("Enter Age: ", int)
            city = get_user_input("Enter City: ")
            insert_data(con, name, age, city)

        elif choice == 2:
            user_id = get_user_input("Enter The ID to Update: ", int)
            name = get_user_input("Enter Name: ")
            age = get_user_input("Enter Age: ", int)
            city = get_user_input("Enter City: ")
            update_data(con, name, age, city, user_id)

        elif choice == 3:
            display_data(con)

        elif choice == 4:
            user_id = get_user_input("Enter The ID to Delete: ", int)
            delete_data(con, user_id)

        elif choice == 5:
            console.print("[bold red]Exiting Program. Goodbye![/]")
            break

# Start the program
if __name__ == "__main__":
    main()
