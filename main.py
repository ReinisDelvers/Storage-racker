# Klašu importēšana no methods faila
from methods import Products, AppleProducts

# Grafiskā interfeisa inportēšana
import tkinter as tk 
from tkinter import ttk, END
from tkinter.messagebox import showinfo

# Galvanais saraksts
product_list = []

# Tkinter loga izveide
root = tk.Tk()
root.title('Ražas uzskaite')
root.geometry('540x720')
root.resizable(False, False)

# Rāmīša izveide
frame = ttk.Frame(root)

# Standarta iestatījumi 
options = {'padx': 5, 'pady': 5}

# Paskaidrojuma uzraksti un ievades lauki
def show_label():
    product_type1 = product_type.get()
    if product_type1 == "Dārzenis" or product_type1 == "Auglis":
        product_name_label.configure(text='Produkta nosaukums')
    elif product_type1 == "Ābols":
        product_name_label.configure(text='Ābolu šķirne')

product_type_label = ttk.Label(frame, text='Produkta tips')
product_type_label.grid(column=0, row=0, rowspan=3, sticky='W', **options)

product_type = tk.StringVar(value="None")
R1 = tk.Radiobutton(frame, text="Dārzenis", variable=product_type, value="Dārzenis", command=show_label)
R1.grid(column=1, row=0, **options)
R2 = tk.Radiobutton(frame, text="Auglis", variable=product_type, value="Auglis", command=show_label)
R2.grid(column=1, row=1, **options)
R3 = tk.Radiobutton(frame, text="Ābols", variable=product_type, value="Ābols", command=show_label)
R3.grid(column=1, row=2, **options)

product_name_label = ttk.Label(frame, width=19, text='Produkta nosaukums')
product_name_label.grid(column=0, row=3, sticky='W', **options)

product_breed_name = ttk.Entry(frame)
product_breed_name.grid(column=1, row=3, **options)
product_breed_name.focus()

product_amount_label = ttk.Label(frame, text='Produkta daudzums')
product_amount_label.grid(column=0, row=4, sticky='W', **options)

product_amount = ttk.Entry(frame)
product_amount.grid(column=1, row=4, **options)
product_amount.focus()

new_product_name = ttk.Entry(frame)
new_product_name.grid(column=0, row=6, **options)
new_product_name.focus()

new_product_amount = ttk.Entry(frame)
new_product_amount.grid(column=0, row=7, **options)
new_product_amount.focus()

jam_amount = ttk.Entry(frame)
jam_amount.grid(column=0, row=8, **options)
jam_amount.focus()

# Metodes
# Metode jauna produkta pievienošanai
def add_button_clicked():
    product_breed_name1 = product_breed_name.get()
    product_type1 = product_type.get()
    product_amount1 = product_amount.get()
    if not product_breed_name1:
        showinfo("Kļūda", "Lūdzu aizpildiet produkta nosaukuma/šķirnes lodziņu.")
        return
    if product_type1 not in ["Dārzenis", "Auglis", "Ābols"]:
        showinfo("Kļūda", "Lūdzu izvēlieties derīgu produkta veidu.")
        return
    try:
        product_amount1 = int(product_amount1)
    except ValueError:
        showinfo("Kļūda", "Lūdzu ievadiet skaitli produkta daudzuma lodziņā.")
        return
    if product_type1 == "Ābols":
        product_list.append(AppleProducts(product_breed_name1, product_amount1))
    else:
        product_list.append(Products(product_type1, product_breed_name1, product_amount1))
    change_list()

# Metode produkta nosaukuma maiņai
def name_change_button_clicked():
    new_product_name1 = new_product_name.get()
    if not new_product_name1:
        showinfo("Kļūda", "Lūdzu aizpildiet jaunā produkta nosaukuma/šķirnes lodziņu.")
        return
    selected = product_listbox.curselection()
    if not selected:
        showinfo("Kļūda", "Lūdzu izvēlieties produktus, kuru nosaukumu vēlaties mainīt.")
        return
    for i in selected:
        product_type1 = product_list[i].type_repeater()
        if product_type1 == "Ābols":
            for a in selected:
                product_list[a].name_change(new_product_name1)
        else:
            for a in selected:
                product_list[a].name_change(new_product_name1)
    change_list()

# Metode produkta tipa maiņai
def type_change_button_clicked():
    selected = product_listbox.curselection()
    if not selected:
        showinfo("Kļūda", "Lūdzu izvēlieties produktu, ko vēlaties pārvērst ievārījumā.")
        return
    for i in selected:
        product_list[i].type_change()
    change_list()

# Metode produkta daudzuma maiņai
def amount_change_button_clicked():
    new_product_amount1 = new_product_amount.get()
    try:
        new_product_amount1 = int(new_product_amount1)
    except ValueError:
        showinfo("Kļūda", "Lūdzu ievadiet skaitli jaunā produkta daudzuma lodziņā.")
        return
    selected = product_listbox.curselection()
    if not selected:
        showinfo("Kļūda", "Lūdzu izvēlieties produktu, kuru daudzumu vēlaties mainīt.")
        return
    for i in selected:
        product_list[i].amount_change(new_product_amount1)
    change_list()

# Metode ievārījuma taisīšanai
def jam_button_clicked():
    jam_amount1 = jam_amount.get()
    try:
        jam_amount1 = int(jam_amount1)
    except ValueError:
        showinfo("Kļūda", "Lūdzu ievadiet skaitli ievārījuma daudzuma lodziņā.")
        return
    selected = product_listbox.curselection()
    if not selected:
        showinfo("Kļūda", "Lūdzu izvēlieties produktu, ko vēlaties pārvērst ievārījumā.")
        return
    for i in selected:
        selected_product = product_list[i]
        if jam_amount1 <= selected_product.amount_repeater() / 2:
            if selected_product.type_repeater() not in ["Ievārījums - Dārzenis", "Ievārījums - Auglis", "Ievārījums - Ābols"]:
                jam_type = ""
                if selected_product.type_repeater() == "Dārzenis":
                    jam_type = "Ievārījums - Dārzenis"
                elif selected_product.type_repeater() == "Auglis":
                    jam_type = "Ievārījums - Auglis"
                elif selected_product.type_repeater() == "Ābols":
                    jam_type = "Ievārījums - Ābols"
                if jam_type:
                    selected_product.jam(jam_amount1)
                    product_list.append(Products(selected_product.name_repeater(), jam_type, jam_amount1))
                    change_list()
            else:
                showinfo("Kļūda", "No ievārījuma nevar izgatavot ievārījumu.")
        else:
            showinfo("Kļūda", "Nav pietiekami daudz produkta, lai izgatavotu tik daudz ievārījuma.")

# Metode produktu izdēšanai
def delete_button_clicked():
    selected = product_listbox.curselection()
    if not selected:
        showinfo("Kļūda", "Lūdzu izvēlieties produktu, ko vēlaties dzēst.")
        return
    for i in reversed(selected):
        product_list.pop(i)
    change_list()

# Metode vienādo produkta saskaitīšanai
def combine_button_clicked():
    combined_products = {}
    for product in product_list:
        what_need_to_be_same = (product.name_repeater(), product.type_repeater())
        if what_need_to_be_same in combined_products:
            combined_products[what_need_to_be_same].amount_adder(product.amount_repeater())
        else:
            combined_products[what_need_to_be_same] = product
    product_list.clear()
    product_list.extend(combined_products.values())
    change_list()

# Metode listboxa atjaunināšanai
def change_list():
    product_listbox.delete(0, END)
    for product in product_list:
        product_listbox.insert("end", f"{product.name},{product.type},{product.amount}")

# Pogas
adding_button = ttk.Button(frame, text='Pievienot produktu sarakstam', command=add_button_clicked)
adding_button.grid(column=2, row=0, **options)

product_name_change_button = ttk.Button(frame, text='Produkta nosaukuma/šķirnes maiņa', command=name_change_button_clicked)
product_name_change_button.grid(column=1, sticky="W", row=6, **options)

product_type_change_button = ttk.Button(frame, text='Produkta veida maiņa', command=type_change_button_clicked)
product_type_change_button.grid(column=2, row=6, **options)

product_amount_button = ttk.Button(frame, text='Produkta daudzuma maiņa', command=amount_change_button_clicked)
product_amount_button.grid(column=1, row=7, sticky="W", **options)

jam_button = ttk.Button(frame, text='Taisīt ievārījumu', command=jam_button_clicked)
jam_button.grid(column=1, row=8, sticky="W", **options)

combine_button = ttk.Button(frame, text='Savienot dublikātus', command=combine_button_clicked)
combine_button.grid(column=2, row=7, **options)

delete_button = ttk.Button(frame, text='Izdzēst no saraksta', command=delete_button_clicked)
delete_button.grid(column=2, row=8, **options)

# Listbox izveide
product_listbox = tk.Listbox(frame, height=20, width=80, selectmode=tk.EXTENDED)
product_listbox.grid(column=0, columnspan=3, row=5, **options)

# Rāmīša iestatījumi
frame.grid(padx=10, pady=10)

# palaiž Tkinter cilpu
root.mainloop()