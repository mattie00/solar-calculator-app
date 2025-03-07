import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_combobox, \
    safe_float


class StructureFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db_instance = db_instance

        self.selected_support_price = 0
        self.selected_rafter_price = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Konstrukcja wsporcza", 0, 0)

        create_label(self, "Typ konstrukcji", 1, 0)

        if self.db_instance:
            construction_list = self.db_instance.fetch_combobox_values("support", "type")
        else:
            construction_list = ["Brak danych"]

        construction_list.insert(0, "Brak")

        self.type_of_construction = create_combobox(self, 1, 1, values=construction_list, command=self.update_support_info)

        create_label(self, "Rodzaj krokwi", 2, 0)

        if self.db_instance:
            rafter_list = self.db_instance.fetch_combobox_values("rafter", "type")
        else:
            rafter_list = ["Brak danych"]

        rafter_list.insert(0, "Brak")

        self.type_of_rafter = create_combobox(self, 2, 1, values=rafter_list, command=self.update_rafter_info)

    def update_support_info(self, selected_value):
        if self.db_instance:
            query = "SELECT price FROM support WHERE type = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_support_price = row["price"]
            else:
                self.selected_support_price = 0
        else:
            self.selected_support_price = 0

    def update_rafter_info(self, selected_value):
        if self.db_instance:
            query = "SELECT price FROM rafter WHERE type = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_rafter_price = row["price"]
            else:
                self.selected_rafter_price = 0
        else:
            self.selected_rafter_price = 0

    def get_structure_data(self):
        data = {
            "construction_type": self.type_of_construction.get(),
            "construction_price": safe_float(getattr(self, "selected_support_price", 0)),
            "rafter_type": self.type_of_rafter.get(),
            "rafter_price": safe_float(getattr(self, "selected_rafter_price", 0))
        }
        return data