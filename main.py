"""
In Main.py only put startup code -> when package is installed
which methods you want to run on initilization

"""
from tkinter import * 
import tkinter as tk
from tkinter import ttk, messagebox, StringVar, Toplevel
from .employee_catalog import Employee
def main():
    # Initializing Main Application Window
    root = tk.Tk()
    root.title("Employment Database")

    # Creating Content Frame
    mainframe = ttk.Frame(root, padding="20 20 20 20")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Welcome Widget
    welcome_message = "Welcome to Your Employment Search directory. How may I assist you?"
    welcome_label = ttk.Label(mainframe, text=welcome_message, wraplength=300)
    welcome_label.grid(column=1, row=0, columnspan=3)

    # Creating Options Menu  
    option_label = ttk.Label(mainframe, text='What would you like to do?')
    option_label.grid(column=1, row=1)

    options = ['Select Option', 'Search Employee', 'Create Employee', 'Delete Employee', 'Update Employee']
    selected_option = StringVar()
    selected_option.set(options[0])

    option_menu = ttk.OptionMenu(mainframe, selected_option, *options)
    option_menu.grid(column=2, row=1)

    # Function to handle option selection
    def check_state():
        match selected_option.get():
            case 'Search Employee':
                print("Search Employee was clicked")
                
                # Creating a new window for search
                search_window = Toplevel(root)
                search_window.title("Search Employee")
                search_window.geometry("400x400")
                search_window.resizable(False, False)

                # Creating a search label
                search_label = ttk.Label(search_window, text='Enter Employee ID')
                search_label.grid(column=0, row=0)

                # Creating a search entry
                search_var = StringVar()
                search_entry = ttk.Entry(search_window, textvariable=search_var)
                search_entry.grid(column=1, row=0)

                # Function to be triggered when the search button is clicked
                def search_employee():
                    employee_id = search_var.get()
                    print(f"Searching for Employee ID: {employee_id}")
                    
                    
                # Creating a search button
                search_button = ttk.Button(search_window, text='Search', command=search_employee)
                search_button.grid(column=1, row=2) 

            case 'Create Employee':
                print("Create Employee was clicked")

                # Create a new window
                create_window = Toplevel(root) 
                create_window.title("Create Employee")
                create_window.geometry("400x400")
                create_window.resizable(True, True)

                # Add title to the create window
                create_title = ttk.Label(create_window, text='Create New Employee')
                create_title.grid(column=1, row=0)  
                # Add a create new employee label
                create_label = ttk.Label(create_window, text='Enter Employee Name')
                create_label.grid(column=0, row=1)

                # Create a name label box 
                create_employee  = StringVar()
                create_entry = ttk.Entry(create_window, textvariable=create_employee)
                create_entry.grid(column=1, row=1)

                # Create a new emplyee ID label 
                create_id_label = ttk.Label(create_window, text='Enter Employee ID')
                create_id_label.grid(column=0, row=2)

                # Create a new employee ID box search 
                create_id = StringVar() 
                create_id_entry = ttk.Entry(create_window, textvariable=create_id)
                create_id_entry.grid(column=1, row=2)

                # Create new employee email label 
                create_email_label = ttk.Label(create_window, text='Enter Employee Email')
                create_email_label.grid(column=0, row=3)

                # Create search bar
                create_email = StringVar()
                create_email_entry = ttk.Entry(create_window, textvariable=create_email)
                create_email_entry.grid(column=1, row=3)

                # Create check button 
                def create_employee_input():
                    try:
                        employee_name = create_employee.get()
                        employee_id = create_id.get()
                        employee_email = create_email.get()
                        print(f"Creating Employee: {employee_name}, {employee_id}, {employee_email}")
                        employee = Employee()
                        new_employee = employee(employee_name, employee_id, employee_email)
                        messagebox.showinfo("Employee Created", f"Employee {employee_name} has been created successfully!")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                # Create a button to create employee
                create_button = ttk.Button(create_window, text='Create Employee', command=_create_employee_input)
                create_button.grid(column=1, row=4)


            case 'Delete Employee': 
                print("Delete Employee was clicked")
            case 'Update Employee':
                print("Update Employee was clicked")
            case _:
                print("Invalid Option")

    # Creating a button to check the selected option
    check_button = ttk.Button(mainframe, text='Next', command=check_state)
    check_button.grid(column=2, row=2)

    # Adding Padding
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    # Bind "Enter" key to trigger check_state when pressed
    root.bind("<Return>", lambda event: check_state())

    # Start the main event loop
    root.mainloop()
    


if __name__ == "__main__":
    main()
