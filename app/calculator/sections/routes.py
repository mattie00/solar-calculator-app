import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_bold_label, \
    create_entry, create_combobox, safe_int, safe_float

TRENCH_CABLE_TYPE = ["AC", "DC"]

class RoutesFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db_instance = db_instance

        self.selected_dc_cable_price = 0
        self.selected_ac_cable_price = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Trasy kablowe i długości przewodów", 0, 0)

        create_bold_label(self, "Trasa gruntowa", 1, 0)

        create_label(self, "Długość przekopu [mb]", 2, 0)
        self.trench_length = create_entry(self, 2, 1)

        create_label(self, "Typ przewodu w przekopie", 3, 0)
        self.trench_cable_type = create_combobox(self, 3, 1, values=TRENCH_CABLE_TYPE)

        create_bold_label(self, "Długości przewodów", 4, 0)

        create_label(self, "Typ przewodu DC", 5, 0)

        if self.db_instance:
            dc_cable_list = self.db_instance.fetch_combobox_values("cable_dc","name")
        else:
            dc_cable_list = ["Brak"]

        dc_cable_list.insert(0, "Brak")

        self.dc_cable_type = create_combobox(self, 5, 1, values=dc_cable_list, command=self.update_dc_cable_info)

        create_label(self, "Długość trasy DC [m]", 6, 0)
        self.dc_route_length = create_entry(self, 6, 1)

        create_label(self, "Typ przewodu AC", 7, 0)

        if self.db_instance:
            ac_cable_list = self.db_instance.fetch_combobox_values("cable_ac", "name")
        else:
            ac_cable_list = ["Brak"]
        ac_cable_list.insert(0, "Brak")

        self.ac_cable_type = create_combobox(self, 7, 1, values=ac_cable_list, command=self.update_ac_cable_info)

        create_label(self, "Długość trasy AC [m]", 8, 0)
        self.ac_route_length = create_entry(self, 8, 1)

    def update_dc_cable_info(self, selected_value):
        if self.db_instance:
            query = "SELECT price FROM cable_dc WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_dc_cable_price = row["price"]
            else:
                self.selected_dc_cable_price = 0
        else:
            self.selected_dc_cable_price = 0

    def update_ac_cable_info(self, selected_value):
        if self.db_instance:
            query = "SELECT price FROM cable_ac WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_ac_cable_price = row["price"]
            else:
                self.selected_ac_cable_price = 0
        else:
            self.selected_ac_cable_price = 0

    def get_routes_data(self):
        trench_length = safe_int(self.trench_length.get())
        dc_route_length = safe_int(self.dc_route_length.get())
        ac_route_length = safe_int(self.ac_route_length.get())

        dc_cable = self.dc_cable_type.get()
        if not dc_cable or dc_cable == "Wybierz z listy":
            dc_cable = "Brak"

        ac_cable = self.ac_cable_type.get()
        if not ac_cable or ac_cable == "Wybierz z listy":
            ac_cable = "Brak"

        data = {
            "trench_length": trench_length,
            "trench_cable_type": self.trench_cable_type.get(),
            "dc_cable_type": dc_cable,
            "dc_route_length": dc_route_length,
            "dc_cable_price": safe_float(getattr(self, "selected_dc_cable_price", 0)),
            "ac_cable_type": ac_cable,
            "ac_route_length": ac_route_length,
            "ac_cable_price": safe_float(getattr(self, "selected_ac_cable_price", 0))
        }
        return data
