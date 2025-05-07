import tkinter as tk
from tkinter import ttk, END, messagebox
from tkinter.messagebox import showerror

from data import add_category, add_item, get_category, get_item, remove_category, remove_item, update_category, update_item

options = {"padx": 5, "pady": 5}

class MainGUI:
    def __init__(self):

        self.window = tk.Tk()
      
        window_width = 1280
        window_height = 720

        # get the screen dimension
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.window.title("Storage tracker")


        category_list = get_category()
        if len(category_list)+1 > 5:
            for i in range(len(category_list)+1):
                self.window.columnconfigure(i, weight=1)
        else:
            for i in range(5):
                self.window.columnconfigure(i, weight=1)
        
        selected_category_id = None
        selected_item_id = None
        categoryoritem = 0
        categorychoice = -1

        def change_list():
            nonlocal categorychoice
            category_list = get_category()
            item_list = get_item()
            item_list_remade = []
            category_list_remade = []

            for i in range(len(category_list)):
                category_list_remade.append(category_list[i][1])
            for i in range(len(item_list)):
                if categorychoice == -1:
                    temp = []
                    temp.append(item_list[i][1])
                    temp.append(item_list[i][2])
                    for b in range(len(category_list)):
                        if item_list[i][3] == category_list[b][0]:
                            temp.append(category_list[b][1])                    
                    item_list_remade.append(temp)
                    print("---")
                elif categorychoice > 0:
                    if categorychoice == item_list[i][3]:
                        temp = []
                        temp.append(item_list[i][1])
                        temp.append(item_list[i][2])
                        for b in range(len(category_list)):
                                if item_list[i][3] == category_list[b][0]:
                                    temp.append(category_list[b][1])   
                        item_list_remade.append(temp)
                        print("---3333")
            categorychoice = -1

            
            category_listbox.delete(0, END)
            item_listbox.delete(0, END)

            for item in category_list_remade:
                category_listbox.insert("end", f"{item}")
            for item in item_list_remade:
                item_listbox.insert("end", f"{item}")

            
            category_listbox.delete(0, END)
            item_listbox.delete(0, END)

            for item in category_list_remade:
                category_listbox.insert("end", f"{item}")
            for item in item_list_remade:
                item_listbox.insert("end", f"{item}")


        def item_add():
            nonlocal selected_category_id
            category_list = get_category()
            item_list = get_item()
            item_name = ent1.get()
            item_count = ent2.get()
    
            for i in range(len(item_list)):
                if  item_name == item_list[i][1]:
                    showerror("Error", "This item already exists.")
                    return
            try:
                int(item_count)
            except:
                showerror("Error", "Item count needs to be an number.")
                return
            if item_name and item_count and selected_category_id:
                add_item(item_name, item_count, selected_category_id)
                change_list()
            else:
                showerror("Error", "You need to select category and write a item name.")
                return
            
        def category_add():
            category_list = get_category()
            category_name = ent1.get()
            for i in range(len(category_list)):
                if  category_name == category_list[i][1]:
                    showerror("Error", "This category already exists.")
                    return
            if category_name:
                add_category(category_name)
                change_list()
            else:
                showerror("Error", "You need write a category name.")
                return        

        
        def edit():
            nonlocal selected_category_id, selected_item_id, categoryoritem
            item_list = get_item()
            category_list = get_category()
            category_selected = list(category_listbox.curselection())
            item_selected = list(item_listbox.curselection())
            if not (category_selected or item_selected):
                showerror("Error", "Select category or item to edit.")
                return
            elif category_selected and item_selected:
                showerror("Error", "Select category or item to edit not both.")
                return
            elif len(category_selected) > 1 or len(item_selected) > 1 :
                showerror("Error", "Select only one to edit.")
                return

            if categoryoritem == 1:
                selected_category_id = category_list[category_selected[0]][0]
                
                for i in selected_category_id:
                    for b in range(len(category_list)):
                        if i == category_list[b][0]:
                            category_listbox.selection_set(b)       

            elif categoryoritem == 2:
                selected_category_id = category_list[category_selected[0]][0]
                selected_item_id = item_list[item_selected[0]][1]
               
                for i in selected_item_id:
                    for b in range(len(item_list)):
                        if i == item_list[b][0]:
                            item_listbox.selection_set(b)


        def remove():
            nonlocal categoryoritem
            if categoryoritem == 1:
                category_selected = list(category_listbox.curselection())
                if not category_selected:
                    showerror("Error", "Select something to remove from category.")
                    return
                category_list = get_category()
                selected_id = [] 
                for i in category_selected:
                    selected_id.append(category_list[i][0])
                remove_category(selected_id)
            if categoryoritem == 2:
                item_selected = list(item_listbox.curselection())
                if not item_selected:
                    showerror("Error", "Select something to remove from item.")
                    return
                item_list = get_item()
                selected_id = [] 
                for i in item_selected:
                    selected_id.append(item_list[i][0])
                remove_item(selected_id)
            categoryoritem == 0
            change_list()

        def confirm_edit():
            nonlocal selected_category_id, selected_item_id, categoryoritem
            item_list = get_item()
            category_list = get_category()
            if categoryoritem == 1:
                category_name = ent1.get()
                for i in range(len(category_list)):
                    if  selected_category_id == category_list[i][1]:
                        showerror("Error", "This category already exists.")
                        return
                if selected_category_id != None:
                    update_category(selected_category_id, category_name)
                    selected_category_id = None
                    categoryoritem = 0
                else:
                    showerror("Error", "Select something to edit.")
                    return
            elif categoryoritem == 2:
                item_name = ent1.get()
                item_count = ent2.get()
                for i in range(len(item_list)):
                    if  selected_item_id == item_list[i][1]:
                        showerror("Error", "This category already exists.")
                        return
                if selected_item_id != None:
                    update_item(selected_item_id, item_name, item_count, selected_category_id)
                    selected_item_id = None
                    categoryoritem = 0
                else:
                    showerror("Error", "Select something to edit.")
                    return

            change_list()


        def category_on_selection(useless):
            nonlocal selected_category_id, categoryoritem, categorychoice
            category_list = get_category()
            categoryoritem = 1
            selected = list(category_listbox.curselection())
            try:
                selected_category_id = category_list[selected[0]][0]
                categorychoice = category_list[selected[0]][0]
                print(categorychoice)
                change_list()
            except:
                return

                        
        def item_on_selection(useless):
            nonlocal selected_item_id, selected_category_id, categoryoritem
            item_list = get_item()
            selected = list(item_listbox.curselection())
            try:
                selected_item_id = item_list[selected[0]][0]
                selected_category_id = item_list[selected[0]][3]
                change_list()
                
            except:
                return

            
            
        btn1 = tk.Button(self.window, text="Add category", font=("Arial", 18), command=category_add)
        btn1.grid(row=0, column=2, sticky=tk.W+tk.E, **options)

        btn2 = tk.Button(self.window, text="Add item", font=("Arial", 18), command=item_add)
        btn2.grid(row=0, column=3, sticky=tk.W+tk.E, **options)

        btn3 = tk.Button(self.window, text="Edit", font=("Arial", 18), command=edit)
        btn3.grid(row=1, column=2, sticky=tk.W+tk.E, **options)

        btn4 = tk.Button(self.window, text="Confirm edit", font=("Arial", 18), command=confirm_edit)
        btn4.grid(row=1, column=3, sticky=tk.W+tk.E, **options)

        btn5 = tk.Button(self.window, text="Remove", font=("Arial", 18), command=remove)
        btn5.grid(row=1, column=4, sticky=tk.W+tk.E, **options)


        ent1 = tk.Entry(self.window,  font=("Arial", 18))
        ent1.grid(row=1, column=0, sticky=tk.W+tk.E, **options)

        ent2 = tk.Entry(self.window,  font=("Arial", 18))
        ent2.grid(row=1, column=1, sticky=tk.W+tk.E, **options)

        label1 = tk.Label(self.window, text="Name", font=("Arial", 18))
        label1.grid(row=0, column=0, sticky=tk.W+tk.E, **options)

        label2 = tk.Label(self.window, text="Amount", font=("Arial", 18))
        label2.grid(row=0, column=1, sticky=tk.W+tk.E, **options)


        category_listbox = tk.Listbox(self.window, selectmode=tk.EXTENDED, font=("Arial", 18))
        category_listbox.grid(row=2, column=0, columnspan=2, sticky="nsew", **options)
        category_listbox.bind("<<ListboxSelect>>", category_on_selection)

        item_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE, font=("Arial", 18))
        item_listbox.grid(row=2, column=2, columnspan=2, sticky="nsew", **options)
        item_listbox.bind("<<ListboxSelect>>", item_on_selection)

        change_list()
        self.window.mainloop()


MainGUI()