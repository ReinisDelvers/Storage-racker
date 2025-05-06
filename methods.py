# Klase visiem productiem
class Products:  
    # Iniciē visus produktus
    def __init__(self, type, name, amount = 0):
        self.name = name
        self.type = type
        self.amount = amount

    # Maina produkta nosaukumu
    def name_change(self, new_product_name):
        self.name = new_product_name

    # Maina produkta tipu
    def type_change(self):
        if self.type == "Auglis":
            self.type = "Dārzenis"
        elif self.type == "Dārzenis":
            self.type = "Ābols"
            self. name = f"Šķirne - {self.name}"
        elif self.type == "Ābols":
            self.type = "Auglis"
            self.name = self.name.strip("Šķirne - ")

    # Maina produkta daudzumu
    def amount_change(self, new_product_amount):
        self.amount = new_product_amount
    
    # Daudzuma aprēķināšana pēc ievārījuma taisīšanas
    def jam(self, jam_amount):
        self.amount = self.amount-jam_amount*2
    
    # Atgriež produkta nosaukumu
    def name_repeater(self):
        return self.name

    # Atgriež produkta daudzumu
    def amount_repeater(self):
        return self.amount
    
    # Atgriež produkta tipu
    def type_repeater(self):
        return self.type

    # Saskaita produkta daudzumus
    def amount_adder(self, amountading):
        self.amount = int(self.amount) + int(amountading)

# Klase priekš āboliem
class AppleProducts(Products):
    # Iniciē ābolu produktus
    def __init__(self, name, amount=0):
        super().__init__("Ābols", name, amount)
        self.name = f"Šķirne - {name}"

    # Ābolu šķirnes nosaukuma maiņa
    def name_change(self, new_product_name):
        self.name = f"Šķirne - {new_product_name}"
