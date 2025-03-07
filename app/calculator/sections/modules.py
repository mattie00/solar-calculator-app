import customtkinter as ctk
from utils.helpers import create_label, create_section_label, create_entry, \
    create_combobox, create_active_label, safe_float, safe_int


class PVModulesFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)

        self.db_instance = db_instance

        self.selected_installation_direction_price = 0
        self.selected_module_price = 0
        self.selected_module_power = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Moduły fotowoltaiczne", 0, 0)

        if self.db_instance:
            modules_list = self.db_instance.fetch_combobox_values("modules", "name")
        else:
            modules_list = ["Brak danych"]

        modules_list.insert(0, "Brak")

        create_label(self, "Wybierz moduł", 1, 0)
        self.module = create_combobox(self, 1, 1, values=modules_list, command=self.update_info)

        create_label(self, "Gwarancja produktu", 2, 0)
        self.module_product_warranty = create_active_label(self, 2, 1, text="Wybierz moduł")

        create_label(self, "Gwarancja liniowa", 3, 0)
        self.module_linear_warranty = create_active_label(self, 3, 1, text="Wybierz moduł")

        create_label(self, "Ilość modułów", 4, 0)
        self.number_of_modules = create_entry(self, 4, 1)
        self.number_of_modules.bind("<KeyRelease>", lambda event: self.update_total_power(self))

        create_label(self, "Moc modułów (kW)", 5, 0)
        self.power = create_active_label(self, 5, 1, text="Wybierz moduł i wprowadź ilość")

        if self.db_instance:
            direction_list = self.db_instance.fetch_combobox_values("installation_direction", "direction")
        else:
            direction_list = ["Brak danych"]

        direction_list.insert(0, "Nie określono")

        create_label(self, "Kierunek instalacji", 6, 0)
        self.installation_direction = create_combobox(self, 6, 1, values=direction_list, command=self.update_direction_price)

        create_label(self, "Kąt nachylenia dachu (w °)", 7, 0)
        self.roof_angle = create_entry(self, 7, 1)

    def update_info(self, event):
        selected_module = self.module.get()
        if self.db_instance:
            query = "SELECT product_warranty, performance_warranty, power, price FROM modules WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_module,))
            row = cur.fetchone() if cur else None
            if row:
                self.module_product_warranty.configure(text=row["product_warranty"])
                self.module_linear_warranty.configure(text=row["performance_warranty"])
                self.selected_module_power = row["power"]
                self.selected_module_price = row["price"]
        self.update_total_power(self)

    def update_total_power(self, event):
        try:
            count = int(self.number_of_modules.get())
        except ValueError:
            count = 0
        total_power = self.selected_module_power * count
        self.power.configure(text=f"{int(total_power)} kW")

    def update_direction_price(self, selected_direction):
        if self.db_instance:
            query = "SELECT price FROM installation_direction WHERE direction = ?"
            cur = self.db_instance.execute_query(query, (selected_direction,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_installation_direction_price = row["price"]
            else:
                self.selected_installation_direction_price = 0
        else:
            self.selected_installation_direction_price = 0

    def get_modules_data(self):
        module_value = self.module.get()
        if module_value == "Wybierz z listy":
            module_value = "Brak"
        count_modules = safe_int(self.number_of_modules.get())

        data = {
            "module_name": module_value,
            "module_price": safe_float(getattr(self, "selected_module_price", 0)),
            "module_count": count_modules,
            "module_product_warranty": self.module_product_warranty.cget("text"),
            "module_performance_warranty": self.module_linear_warranty.cget("text"),
            "module_total_power": int(self.selected_module_power * count_modules),
            "installation_direction": self.installation_direction.get(),
            "installation_direction_price": safe_float(getattr(self, "selected_installation_direction_price", 0)),
            "roof_angle": self.roof_angle.get()
        }
        return data
