import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# Define the menu data
data = {
    'Menu Item': ['Burgers', 'Nachos', 'Ribs', 'Pizza'],
    '01/03/2023': [36, 5, 45, 12],
    '02/03/2023': [12, 10, 16, 15],
    '03/03/2023': [25, 8, 20, 18],
    '04/03/2023': [30, 15, 40, 22],
    'Price': [8.99, 6.99, 12.99, 9.99]  # Added Price column
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Set 'Menu Item' column as the index
df.set_index('Menu Item', inplace=True)


def option1():
    # Find the highest and lowest menu items
    highest_demand = df.idxmax().values[0]
    lowest_demand = df.idxmin().values[0]

    # Visualize the menu item demand
    df.plot(kind='bar', figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.title('Menu Item Demand')
    plt.legend(title='Menu Item')
    plt.show()

    messagebox.showinfo("Menu Item Demand",
                        f"The menu item with the highest demand is: {highest_demand}\n"
                        f"The menu item with the lowest demand is: {lowest_demand}")


def option2():
    # Calculate the percentage increase over the period of time
    df['Percentage Increase'] = (df['04/03/2023'] - df['01/03/2023']) / df['01/03/2023'] * 100
    df.sort_values(by='Percentage Increase', ascending=False, inplace=True)

    # Visualize the percentage increase
    df['Percentage Increase'].plot(kind='bar', figsize=(10, 6))
    plt.xlabel('Menu Item')
    plt.ylabel('Percentage Increase')
    plt.title('Menu Item Percentage Increase')
    plt.xticks(rotation=45)
    plt.show()

    messagebox.showinfo("Menu Item Percentage Increase", str(df))


def option3():
    def show_selected_item():
        selected_item = item_var.get()

        if selected_item in df.index:
            # Calculate the total quantity sold for the selected item
            total_quantity = df.loc[selected_item].sum()

            # Create a pie chart to visualize the total quantity
            plt.figure(figsize=(6, 6))
            plt.pie(df.loc[selected_item][:-1], labels=df.columns[:-1], autopct='%1.1f%%')

            plt.title(f"Total Quantity Sold for {selected_item}")
            plt.show()

            messagebox.showinfo("Total Quantity Sold",
                                f"The total quantity sold for {selected_item} is: {total_quantity}")
        else:
            messagebox.showerror("Invalid Selection", "Invalid menu item selected.")

    window = Tk()
    window.title("Total Quantity of a Selected Item")

    item_var = StringVar()
    item_var.set(df.index[0])

    item_label = Label(window, text="Select a menu item:")
    item_label.pack()

    item_optionmenu = OptionMenu(window, item_var, *df.index)
    item_optionmenu.pack()

    show_button = Button(window, text="Show Total Quantity", command=show_selected_item)
    show_button.pack()

    window.mainloop()


def option4():
    # Calculate the total quantity sold for all menu items
    total_quantity_all = df.sum()

    # Create a pie chart to visualize the total quantity for all items
    plt.figure(figsize=(6, 6))
    plt.pie(total_quantity_all[:-1], labels=df.columns[:-1], autopct='%1.1f%%')
    plt.title("Total Quantity Sold for All Menu Items")
    plt.show()

    messagebox.showinfo("Total Quantity Sold",
                        f"The total quantity sold for all menu items is: {total_quantity_all.sum()}")


def option5():
    # Calculate the total profit for each menu item
    df['Profit'] = (df.iloc[:, :-1] * df['Price']).sum(axis=1)

    # Visualize the total profit for each menu item
    df['Profit'].plot(kind='bar', figsize=(10, 6))
    plt.xlabel('Menu Item')
    plt.ylabel('Profit')
    plt.title('Total Profit for Each Menu Item')
    plt.xticks(rotation=45)
    plt.show()

    messagebox.showinfo("Total Profit for Each Menu Item", str(df))


def option6():
    def show_selected_item():
        selected_item = item_var.get()

        if selected_item in df.index:
            # Calculate the total profit for the selected item
            total_profit = (df.loc[selected_item] * df['Price']).sum()

            # Create a pie chart to visualize the total profit
            plt.figure(figsize=(6, 6))
            plt.pie(df.loc[selected_item][:-1], labels=df.columns[:-1], autopct='%1.1f%%')

            plt.title(f"Total Profit for {selected_item}")
            plt.show()

            messagebox.showinfo("Total Profit",
                                f"The total profit made for {selected_item} is: {total_profit}")
        else:
            messagebox.showerror("Invalid Selection", "Invalid menu item selected.")

    window = Tk()
    window.title("Total Profit of a Selected Item")

    item_var = StringVar()
    item_var.set(df.index[0])

    item_label = Label(window, text="Select a menu item:")
    item_label.pack()

    item_optionmenu = OptionMenu(window, item_var, *df.index)
    item_optionmenu.pack()

    show_button = Button(window, text="Show Total Profit", command=show_selected_item)
    show_button.pack()

    window.mainloop()


# User input for option selection
def get_option():
    try:
        option = int(option_entry.get())
        if option < 1 or option > 6:
            raise ValueError
        process_option(option)
    except ValueError:
        messagebox.showerror("Invalid Option", "Please enter a number between 1 and 6.")


def process_option(option):
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        option6()


window = Tk()
window.title("Restaurant Menu Analysis")

option_label = Label(window, text="Enter an option (1-6):")
option_label.pack()

option_entry = Entry(window)
option_entry.pack()

option_button = Button(window, text="Submit", command=get_option)
option_button.pack()

window.mainloop()
