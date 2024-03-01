# Pilkuk Edwin Chung


# Define the global lists for employees and items
employees = []
item_list = []


# function that will display the output for the menu page
def display_options():
    # Define menu options as a list of strings
    menu_options = [
        "1- Create Employee",
        "2- Create Item",
        "3- Make Purchase",
        "4- All Employees Summary",
        "5- Exit"
    ]

    # Approximate value of half size of the computer screen
    menu_width = 80
    # Create a dash border for top and bottom
    updown_border = "-" * menu_width
    print("\n" + updown_border)

    # Loop through each option and print it with padding
    for option in menu_options:
        # Calculate the padding so the menu is displayed in the middle
        # -2 is the meaning so doesn't calculate the "|" that we'll be using for the borders
        left_padding = (menu_width - len(option) - 2) // 2  # divided so padding is evenly distributed on both sides
        right_padding = menu_width - len(option) - 2 - left_padding
        print("|" + " " * left_padding + option + " " * right_padding + "|")
    print(updown_border)


# main function
def main():
    is_running = True
    while is_running:
        display_options()
        choice = input("Please enter your choice ")
        print()

        if choice == "1":
            is_running = create_employees()
        elif choice == "2":
            is_running = create_item()
        elif choice == "3":
            is_running = make_purchase()
        elif choice == "4":
            display_employee_summary()
            is_running = ask_return_to_menu()
        elif choice == "5":
            print("Thank you for using my program")
            print("Exiting...")
            is_running = False
        else:
            print("Invalid input. Please enter a number from 1 to 5")


# function to create employee
def create_employees():
    is_continue = True
    while is_continue:
        employee_id = get_employee_id("Enter Employee ID: ")
        employee_name = get_valid_value("Enter Employee Name: ")
        employee_type = get_valid_type("Enter Employee Type: ", ["manager", "hourly"])
        employee_years = get_valid_number("Enter Employee Years Worked: ")
        employee_discount_num = get_valid_discount_number("Enter Employee Discount Number: ")
        employees.append([employee_id, employee_name, employee_type, employee_years, 0, 0, employee_discount_num])
        print("Employee with ID " + str(employee_id) + " is successfully added.")
        print()
        loop_answer = get_valid_type("Do you wish to add another employees (Y/N): ", ["y", "n"])[0].upper()
        if loop_answer != "Y":
            return ask_return_to_menu()


# checks if employee id is a number, not null and unique
def get_employee_id(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isdigit():
            user_id = int(user_input)
            if not any(employee[0] == user_id for employee in employees):
                return user_id
            else:
                print("The ID already exists. Please enter another number.")
        else:
            print("Invalid input. Please enter a valid number.")


# checks if the value is not null
def get_valid_value(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input:
            return user_input
        print("Input can not be empty. Please enter a value")


# checks if the value is not null and
# for the employee type, checks that the only options are "manager" or "hourly"
def get_valid_type(prompt_message, types):
    while True:
        user_input = input(prompt_message).lower()
        if user_input and user_input in types:
            return user_input
        print("Please enter one of the following values: " + ", ".join(types))


# checks if the value is not null and a number
def get_valid_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isnumeric():
            return int(user_input)
        print("Please enter a valid number")


# the same function with get_employee_id
# but with the discount number
def get_valid_discount_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isdigit():
            discount_number = int(user_input)
            if not any(employee[6] == discount_number for employee in employees):
                return discount_number
            else:
                print("The number already exists. Please enter another number.")
        else:
            print("Invalid input. Please enter a valid number.")


# function to create an item
def create_item():
    is_continue = True
    while is_continue:
        item_number = get_item_number("Enter Item Number: ")
        item_name = get_valid_value("Enter Item Name: ")
        item_cost = get_valid_number("Enter Item Cost: ")
        item_list.append([item_number, item_name, item_cost])
        print("Item with number " + str(item_number) + " is successfully added.")
        print()
        loop_answer = get_valid_type("Do you wish to add another item (Y/N): ", ["y", "n"])[0].upper()
        if loop_answer != "Y":
            return ask_return_to_menu()


# checks if the item number is a number, not null and unique
def get_item_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isdigit():
            item_id = int(user_input)
            if not any(items[0] == item_id for items in item_list):
                return item_id
            else:
                print("The ID already exists. Please enter another number.")
        else:
            print("Invalid input. Please enter a valid number.")


# function to make a purchase
def make_purchase():
    while True:
        # first will display all the items
        display_items()
        print()
        discount_number = check_discount_number("Please enter employee discount number ")
        employee = next(emp for emp in employees if emp[6] == discount_number)
        print("Discount number " + str(discount_number) + " found.")
        print("Welcome " + str(employee[1]).upper())
        item_number = check_item_number("Please enter the item number ")
        item = next(itm for itm in item_list if itm[0] == item_number)
        print("Item number " + str(item_number) + " found: " + "'" + item[1].upper() + "'")
        confirm_answer = get_valid_type("Do you confirm your purchase (Y/N): ", ["y", "n"])[0].upper()
        print()
        if confirm_answer == "N":
            print("Purchase cancelled")
        else:
            final_cost, applied_discount = calculate_discount(employee, item)
            print(f"Discount applied: ${applied_discount}. Final cost after discount: ${final_cost}.")
        if not new_purchase_confirmation():
            display_employee_summary()
            return ask_return_to_menu()


# function that checks if discount number
# is not null, a number and already exists
def check_discount_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isdigit():
            discount_number = int(user_input)
            if not any(employee[6] == discount_number for employee in employees):
                print("Employee not found. Please enter a valid discount number")
            else:
                return discount_number
        else:
            print("Invalid input. Please enter a valid number.")


# the same function as check_discount_number
# but with the item number
def check_item_number(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input and user_input.isdigit():
            item_number = int(user_input)
            if not any(items[0] == item_number for items in item_list):
                print("The item doesn't exist. Please enter a valid number")
            else:
                return item_number
        else:
            print("Invalid input. Please enter a valid number.")


# calculates the discount according to the exercise
def calculate_discount(employee, item):
    base_discount = min(10, 2 * employee[3])  # it's going to pick the lowest from those two values
                                              # so we make sure it doesn't exceed the 10%
    if employee[2] == "manager":
        base_discount += 10  # it's going to add 10% on the top if it's manager
    elif employee[2] == "hourly":
        base_discount += 2  # it's going to add 2% on the top if it's hourly

    potential_discount = item[2] * (base_discount / 100)  # this calculates the discount
    remaining_discount = max(200 - employee[5], 0)  # make sure that doesn't exceed $200
    discount_amount = min(potential_discount, remaining_discount)  # it's going to choose the fewer value

    final_cost = item[2] - discount_amount

    employee[4] += final_cost  # append the total purchased in the employee array
    employee[5] += discount_amount  # append the total discount in the employee array

    return final_cost, discount_amount


# checks if the user wants to buy another product
def new_purchase_confirmation():
    user_input = get_valid_type("Do you want to go make a new purchase (Y/N): ", ["y", "n"])[0].upper()
    if user_input == "Y":
        return True
    elif user_input == "N":
        return False


# display all the item
def display_items():
    headers = ["Item Number", "Item Name", "Item Cost"]

    # checks the max range for the header or each data of the item_list
    column_widths = [max(len(str(items[i])) for items in item_list + [headers]) for i in range(len(headers))]

    # Print the headers with appropriate spacing
    for i, header in enumerate(headers):
        print(f"{header.ljust(column_widths[i])} |", end=" ")
    print()  # Print a newline after the headers

    # Iterate over each item in the item list and print each attribute with proper formatting
    for items in item_list:
        for i, attribute in enumerate(items):
            # Convert everything to string and left-justify in the column
            print(f"{str(attribute).ljust(column_widths[i])} |", end=" ")
        print()  # Print a newline after each item


# the same function with display_items
def display_employee_summary():
    headers = ["Employee ID", "Employee Name", "Employee Type", "Years Worked",
               "Total Purchased", "Total Discount", "Employee Discount Number"]

    # Determine the width of each column based on the longest string in each column
    column_widths = [max(len(str(employee[i])) for employee in employees + [headers]) for i in range(len(headers))]

    # Print the headers with appropriate spacing
    for i, header in enumerate(headers):
        print(f"{header.ljust(column_widths[i])} |", end=" ")
    print()  # Print a newline after the headers

    # Iterate over each employee in the employees list and print each attribute with proper formatting
    for employee in employees:
        for i, attribute in enumerate(employee):
            # Convert everything to string and left-justify in the column
            print(f"{str(attribute).ljust(column_widths[i])} |", end=" ")
        print()  # Print a newline after each employee


# function that will ask the user if he wants to return to the menu
# at the end of every option in the main menu
def ask_return_to_menu():
    answer = get_valid_type("Do you want to go back to the main menu (Y/N): ", ["y", "n"])[0].upper()
    print()
    if answer != "Y":
        print("Thank you for using my program")
        print("Exiting...")
        return False
    else:
        return True


# This is the way python calls the name of the environment
# where top-level code is run
if __name__ == "__main__":
    main()
