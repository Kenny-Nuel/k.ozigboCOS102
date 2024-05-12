# CA - 1 Project For COS 102
import tkinter as tk
from tkinter import *
from tkinter import simpledialog

window = tk.Tk()
window.title("PAU CAFETERIA - MENU")
window.geometry("800x700")
window.configure(bg="lightblue")
window.iconbitmap('pau-logo.ico')

label = tk.Label(window, text="MENU", font=("Varela Round Regular", 30))
label.grid(row=0,column=1)

first_section = LabelFrame(window, text="RICE/PASTA", padx=50, pady=80, borderwidth=0)
first_section.grid(row=1, column=1, padx=10, pady=10)

# First section labels
first_label_1 = tk.Label(first_section, text="Jollof Rice     -     ₦350")
first_label_1.grid()
first_label_2 = tk.Label(first_section, text="Coconut Fried Rice     -     ₦350")
first_label_2.grid()
first_label_3 = tk.Label(first_section, text="Jollof Spaghetti     -     ₦350")
first_label_3.grid()

second_section = LabelFrame(window, text="Proteins", padx=50, pady=50,borderwidth=0)
second_section.grid(row=1,column=2, padx=10,pady=10)

second_label_1 = tk.Label(second_section, text="Sweet Chill Chicken  -     ₦1100")
second_label_1.grid()
second_label_2 = tk.Label(second_section, text="Grilled Chicken Wings  -     ₦400")
second_label_2.grid()
second_label_3 = tk.Label(second_section, text="Fried Beef  -   ₦400")
second_label_3.grid()
second_label_4 = tk.Label(second_section, text="Fried Fish - ₦400")
second_label_4.grid()
second_label_5 = tk.Label(second_section, text="Boiled Egg - ₦200")
second_label_5.grid()
second_label_6 = tk.Label(second_section, text="Sauced Sausages - ₦200")
second_label_6.grid()

third_section = LabelFrame(window, text="Soups & Swallows", padx=70, pady=80, borderwidth=0)
third_section.grid(row=2, column=1, padx=10,pady=10)

third_label_1 = tk.Label(third_section, text="Eba  -  ₦100")
third_label_1.grid()
third_label_2 = tk.Label(third_section, text="Poundo Yam  -  ₦100")
third_label_2.grid()
third_label_3 = tk.Label(third_section, text="Semo  -   ₦100")
third_label_3.grid()
third_label_4 = tk.Label(third_section, text="Atama Soup - ₦450")
third_label_4.grid()
third_label_5 = tk.Label(third_section, text="Egusi Soup - ₦480")
third_label_5.grid()

fourth_section = LabelFrame(window, text="Side Dishes", padx=50, pady=80, borderwidth=0)
fourth_section.grid(row=2,column=2,padx=10,pady=10)

fourth_label_1 = tk.Label(fourth_section, text="Savoury Beans  -  ₦350")
fourth_label_1.grid()
fourth_label_2 = tk.Label(fourth_section, text="Roasted Sweet Potatoes  -  ₦300")
fourth_label_2.grid()
fourth_label_3 = tk.Label(fourth_section, text="Fried Plantains  -   ₦150")
fourth_label_3.grid()
fourth_label_4 = tk.Label(fourth_section, text="Mixed Vegetable Salad - ₦150")
fourth_label_4.grid()
fourth_label_5 = tk.Label(fourth_section, text="Boiled Yam - ₦150")
fourth_label_5.grid()

fifth_section = LabelFrame(window, text="Beverages", padx=50, pady=30, borderwidth=0)
fifth_section.grid(row=1,column=3,padx=10,pady=10)

fifth_label_1 = tk.Label(fifth_section, text="Water  -  ₦200")
fifth_label_1.grid()
fifth_label_2 = tk.Label(fifth_section, text="Glas Drink (35 Cl)  -  ₦150")
fifth_label_2.grid()
fifth_label_3 = tk.Label(fifth_section, text="Pet Drink(35 Cl)  -   ₦300")
fifth_label_3.grid()
fifth_label_4 = tk.Label(fifth_section, text="Glass/ Canned Malt - ₦500")
fifth_label_4.grid()
fifth_label_5 = tk.Label(fifth_section, text="Fresh Yo - ₦600")
fifth_label_5.grid()
fifth_label_6 = tk.Label(fifth_section, text="Pineapple Juice - ₦350")
fifth_label_6.grid()
fifth_label_7 = tk.Label(fifth_section, text="Mango Juice - ₦600")
fifth_label_7.grid()
fifth_label_8 = tk.Label(fifth_section, text="Zobo - ₦350")
fifth_label_8.grid()


user_name = simpledialog.askstring("Input Required",
                                           "Please enter your name")

# Function to handle placing orders
def order():
    food_prices = {
        "jollof_rice": 350,
        "cocoanut_fried_rice": 350,
        "jollof_spaghetti": 350,
        "sweet_chilli_chicken": 900,
        "grilled_chicken": 400,
        "fried_beef": 400,
        "fried_fish": 500,
        "boiled_egg": 200,
        "sausages": 200,
        "savoury_beans": 350,
        "roasted_sweet_potatoes": 300,
        "fried_plantains": 150,
        "mixed_vegetable_salad": 150,
        "boiled_yam": 150,
        "eba": 300,
        "poundo_yam": 100,
        "semo": 100,
        "acama_soup": 450,
        "egusi_soup": 450,
        "water": 200,
        "glass_drink": 150,
        "pet_drink_35cl": 300,
        "pet_drink_50cl": 350,
        "glass/canned_malt": 500,
        "fresh_yo": 600,
        "pineapple_juice": 350,
        "mango_juice": 350,
        "zobo": 350,
    }

    ticket = []
    total_price = 0

    while True:
        user_input = simpledialog.askstring("Place your order", "Input the food and quantity needed (E.g Poundo_yam)").lower()

        if user_input:
            item_name, quantity_str = user_input.split()
            if item_name in food_prices and quantity_str.isdigit():
                quantity = int(quantity_str)
                item_price = food_prices[item_name]
                ticket.append(f"{quantity} x {item_name.capitalize()}")
                total_price += item_price * quantity
            else:
                tk.messagebox.showerror("Invalid Input", "Please enter a valid item and quantity.")

        continue_order = simpledialog.askstring("Continue Ordering", "Anything else ? (Yes/No)").lower()
        if continue_order != "yes":
            break

    # Display order summary
    summary = tk.Toplevel(window)
    summary.title("Order Summary")
    summary.geometry("400x300")

    tk.Label(summary, text="Your order and bill is:").pack()

    for item in ticket:
        tk.Label(summary, text=item).pack()

    tk.Label(summary, text=f"Total: ₦{total_price}").pack()

    tk.Label(summary, text="Enjoy It ! ").pack()


# Create the "Place Order" button
place_order = tk.Button(window, text="Place Order", command=order)
place_order.grid(row=8, column=0, columnspan=2, pady=10)

window.mainloop()