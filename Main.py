import pandas as pd
import matplotlib.pyplot as plt

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

    print(f"The menu item with the highest demand is: {highest_demand}")
    print(f"The menu item with the lowest demand is: {lowest_demand}")

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

    print(df)

def option3():
    # Get the user's selected menu item
    selected_item = input("Enter the name of the menu item: ")

    # Check if the selected item exists in the DataFrame
    if selected_item in df.index:
        # Calculate the total quantity sold for the selected item
        total_quantity = df.loc[selected_item].sum()

        # Create a pie chart to visualize the total quantity
        plt.figure(figsize=(6, 6))
        plt.pie(df.loc[selected_item][:-1], labels=df.columns[:-1], autopct='%1.1f%%')

        plt.title(f"Total Quantity Sold for {selected_item}")
        plt.show()

        print(f"The total quantity sold for {selected_item} is: {total_quantity}")
    else:
        print("Invalid menu item selected.")

def option4():
    # Calculate the total quantity sold for all menu items
    total_quantity_all = df.sum()

    # Create a pie chart to visualize the total quantity for all items
    plt.figure(figsize=(6, 6))
    plt.pie(total_quantity_all[:-1], labels=df.columns[:-1], autopct='%1.1f%%')
    plt.title("Total Quantity Sold for All Menu Items")
    plt.show()
    print(f"The total quantity sold for all menu items is: {total_quantity_all.sum()}")

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

    print(df)

def option6():
    # Get the user's selected menu item
    selected_item = input("Enter the name of the menu item: ")

    # Check if the selected item exists in the DataFrame
    if selected_item in df.index:
        # Calculate the total profit for the selected item
        total_profit = (df.loc[selected_item] * df['Price']).sum()

        # Create a pie chart to visualize the total profit
        plt.figure(figsize=(6, 6))
        plt.pie(df.loc[selected_item][:-1], labels=df.columns[:-1], autopct='%1.1f%%')

        plt.title(f"Total Profit for {selected_item}")
        plt.show()

        print(f"The total profit made for {selected_item} is: {total_profit}")
    else:
        print("Invalid menu item selected.")



# User input for option selection
option = None

while option is None:
    try:
        option = int(input("Enter 1 for highest and lowest demand, 2 for percentage increase, 3 for total quantity of a selected item, 4 for total quantity of all items, 5 for total profit of each menu item: 6 "))
        if option < 1 or option > 6:
            print("Invalid option selected. Please enter a number between 1 and 6.")
            option = None
    except ValueError:
        print("Invalid option selected. Please enter a number between 1 and 6.")
        option = None

# Call the respective function based on the user's input
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
