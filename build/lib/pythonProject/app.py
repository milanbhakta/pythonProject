
# # Input a number
# user_input = input("Enter a number: ")
#
# # Convert the input to a float (assuming it's a decimal number)
# try:
#     number = float(user_input)
#
#     # Calculate 35% of the number
#     result = number * 0.35
#
#     # Print the result
#     print(f"35% of {number} is {result}")
#
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#
#

# total_result = 0
#
# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")
#
#     if user_input.lower() == 'q':
#         break  # Exit the loop if the user enters 'q'
#
#     try:
#         number = float(user_input)
#         result = number * 0.35
#         total_result += result
#         print(f"35% of {number} is {result}")
#
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# print(f"Sum of all results: {total_result}")

# total_sum = 0
#
# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")
#
#     if user_input.lower() == 'q':
#         break  # Exit the loop if the user enters 'q'
#
#     try:
#         number = float(user_input)
#         total_sum += number
#
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# print(f"Sum of all numbers entered: {total_sum}")


# total_sum = 0
#
# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")
#
#     if user_input.lower() == 'q':
#         break  # Exit the loop if the user enters 'q'
#
#     try:
#         number = float(user_input)
#         total_sum += number
#
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# percentage_list = []
#
# while True:
#     user_input = input("Enter a number to calculate its percentage (or 'q' to quit): ")
#
#     if user_input.lower() == 'q':
#         break  # Exit the loop if the user enters 'q'
#
#     try:
#         number = float(user_input)
#         percentage = (number / total_sum) * 100
#         percentage_list.append((number, percentage))
#         print(f"{number} is {percentage}% of the total")
#
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# print(f"Sum of all numbers entered: {total_sum}")
#
# # Display percentages for all numbers
# print("Percentages of individual numbers:")
# for number, percentage in percentage_list:
#     print(f"{number} is {percentage}% of the total")


from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_todo_list(pdf_filename, tasks):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    title = "To-Do List"

    for date, task_list in tasks.items():
        c.setFont("Helvetica-Bold", 18)
        c.drawString(100, 750, title)
        c.setFont("Helvetica", 12)
        c.drawString(100, 730, f"Date: {date}")

        y_position = 700

        for task in task_list:
            checkbox = "☐"  # Unchecked checkbox symbol
            c.drawString(100, y_position, checkbox)
            c.drawString(120, y_position, task)
            y_position -= 20

        c.showPage()  # Start a new page for the next date

    c.save()


def collect_tasks():
    tasks = {}

    while True:
        task_date = input("Enter task date (YYYY-MM-DD) or 'done' to finish: ")
        if task_date.lower() == "done":
            break

        try:
            task_date = datetime.strptime(task_date, "%Y-%m-%d")
            task_description = input(f"Enter task for {task_date.strftime('%Y-%m-%d')}: ")

            # Create a new page for each date
            date_str = task_date.strftime('%Y-%m-%d')
            if date_str not in tasks:
                tasks[date_str] = []

            tasks[date_str].append(task_description)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")

    return tasks


if __name__ == "__main__":
    pdf_filename = "../todo_list.pdf"
    tasks = collect_tasks()
    generate_todo_list(pdf_filename, tasks)
    print(f"PDF '{pdf_filename}' has been generated.")
