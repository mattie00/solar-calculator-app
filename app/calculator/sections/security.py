import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_entry, \
    create_combobox, safe_float, safe_int


class SecurityFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db_instance = db_instance

        self.selected_security_price = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Zabezpieczenia", 0, 0)

        create_label(self, "Miejsce wpięcia instalacji", 1, 0)

        if self.db_instance:
            installation_point_list = self.db_instance.fetch_combobox_values("installation", "location")
        else:
            installation_point_list = ["Brak danych"]

        installation_point_list.insert(0, "Brak")

        self.installation_point = create_combobox(self, 1, 1, values=installation_point_list)

        create_label(self, "Rodzaj zabezpieczenia", 2, 0)

        if self.db_instance:
            security_list = self.db_instance.fetch_combobox_values("security", "name")
        else:
            security_list = ["Brak danych"]

        security_list.insert(0, "Brak")

        self.security_type = create_combobox(self, 2, 1, values=security_list, command = self.update_security_info)

        create_label(self, "Kubatura budynku (m3)", 3, 0)
        self.building_volume = create_entry(self, 3, 1)

    def update_security_info(self, selected_value):
        if self.db_instance:
            query = "SELECT price FROM security WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_security_price = row["price"]
            else:
                self.selected_security_price = 0
        else:
            self.selected_security_price = 0

    def get_security_data(self):
        building_volume = safe_int(self.building_volume.get())
        data = {
            "installation_point": self.installation_point.get(),
            "security_type": self.security_type.get(),
            "building_volume": building_volume,
            "security_price": safe_float(getattr(self, "selected_security_price", 0))
        }
        return data
