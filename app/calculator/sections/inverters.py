import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_entry, \
    create_combobox, create_active_label, safe_int, safe_float


class InvertersFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)

        self.db_instance = db_instance

        self.selected_inverter_price = 0
        self.selected_warehouse_price = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Inwerter PV", 0, 0)

        create_label(self, "Typ inwertera", 1, 0)

        if self.db_instance:
            inverters_list = self.db_instance.fetch_combobox_values("inverters", "name")
        else:
            inverters_list = ["Brak"]

        inverters_list.insert(0, "Brak")

        self.inverter = create_combobox(self, 1, 1, values=inverters_list, command=self.update_inverter_info)

        create_label(self, "Gwarancja producenta", 2, 0)
        self.inverter_producer_warranty = create_active_label(self, 2, 1, text="Brak danych")

        create_label(self, "Ilość faz", 3, 0)
        self.inverter_phases = create_active_label(self, 3, 1, text="Brak danych")

        create_label(self, "Ilość sztuk", 4, 0)
        self.number_of_inverters = create_entry(self, 4, 1)

        create_label(self, "Typ magazynu", 5, 0)

        if self.db_instance:
            warehouse_list = self.db_instance.fetch_combobox_values("warehouses", "name")
        else:
            warehouse_list = ["Brak"]

        warehouse_list.insert(0, "Brak")

        self.warehouse = create_combobox(self, 5, 1, values=warehouse_list, command=self.update_warehouse_info)

        create_label(self, "Gwarancja producenta", 6, 0)
        self.warehouse_producer_warranty = create_active_label(self, 6, 1, text="Brak danych")

        create_label(self, "Ilość sztuk", 7, 0)
        self.number_of_warehouses = create_entry(self, 7, 1)

    def update_inverter_info(self, event):
        selected_inverter = self.inverter.get()
        if self.db_instance:
            query = "SELECT warranty, phases, price FROM inverters WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_inverter,))
            row = cur.fetchone() if cur else None
            if row:
                self.inverter_producer_warranty.configure(text=row["warranty"])
                self.inverter_phases.configure(text=row["phases"])
                self.selected_inverter_price = row["price"]
            else:
                self.inverter_producer_warranty.configure(text="Brak danych")
                self.inverter_phases.configure(text="Brak danych")
                self.selected_inverter_price = 0
        else:
            self.inverter_producer_warranty.configure(text="Brak danych")
            self.inverter_phases.configure(text="Brak danych")
            self.selected_inverter_price = 0

    def update_warehouse_info(self, event):
        selected_warehouse = self.warehouse.get()
        if self.db_instance:
            query = "SELECT warranty, price FROM warehouses WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_warehouse,))
            row = cur.fetchone() if cur else None
            if row:
                self.warehouse_producer_warranty.configure(text=row["warranty"])
                self.selected_warehouse_price = row["price"]
            else:
                self.warehouse_producer_warranty.configure(text="Brak danych")
                self.selected_warehouse_price = 0
        else:
            self.warehouse_producer_warranty.configure(text="Brak danych")
            self.selected_warehouse_price = 0

    def get_inverters_data(self):
        inverter_value = self.inverter.get()
        if inverter_value == "Wybierz z listy":
            inverter_value = "Brak"
        count_inverters = safe_int(self.number_of_inverters.get())

        warehouse_value = self.warehouse.get()
        if warehouse_value == "Wybierz z listy":
            warehouse_value = "Brak"
        count_warehouses = safe_int(self.number_of_warehouses.get())

        data = {
            "inverter_name": inverter_value,
            "inverter_price": safe_float(getattr(self, "selected_inverter_price", 0)),
            "inverter_count": count_inverters,
            "inverter_warranty": self.inverter_producer_warranty.cget("text"),
            "inverter_phases": self.inverter_phases.cget("text"),
            "warehouse_name": warehouse_value,
            "warehouse_price": safe_float(getattr(self, "selected_warehouse_price", 0)),
            "warehouse_count": count_warehouses,
            "warehouse_warranty": self.warehouse_producer_warranty.cget("text")
        }
        return data





