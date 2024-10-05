"""
In Main.py only put startup code -> when package is installed
which methods you want to run on initilization

"""
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

def main():
    # Initializing Main Application Window
    root = Tk()
    root.title("Employment Database")

    # Creating Content Frame
    mainframe = ttk.Frame(root, padding="20 20 20 20")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Welcome Widget
    welcome_message = "Welcome to Your's Employment Search directory. How may i assist you?"
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



    # Adding Polish 
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    root.bind("<Return>")

    # Start Event Loop 
    root.mainloop()



if __name__ == "__main__":
    main()