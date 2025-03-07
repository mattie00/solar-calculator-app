import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_entry, \
    create_combobox, safe_int, safe_float


class OptimizersFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db_instance = db_instance

        self.selected_optimizer_price = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Optymalizatory mocy (opcjonalne)", 0, 0)

        create_label(self, "Typ optymalizatorów mocy", 1, 0)

        if self.db_instance:
            optimizers_list = self.db_instance.fetch_combobox_values("optimizers", "name")
        else:
            optimizers_list = ["Brak"]

        optimizers_list.insert(0, "Brak")

        self.optimizer_type = create_combobox(self, 1, 1, values=optimizers_list, command=self.update_optimizer_info)

        create_label(self, "Ilość optymalizatorów", 2, 0)
        self.number_of_optimizers = create_entry(self, 2, 1)

    def update_optimizer_info(self, selected_value):
        if self.db_instance:
            query = "SELECT price FROM optimizers WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_optimizer_price = row["price"]
            else:
                self.selected_optimizer_price = 0
        else:
            self.selected_optimizer_price = 0

    def get_optimizers_data(self):
        optimizer_value = self.optimizer_type.get()
        if optimizer_value == "Wybierz z listy":
            optimizer_value = "Brak"
        count_optimizers = safe_int(self.number_of_optimizers.get())

        data = {
            "optimizer_name": optimizer_value,
            "optimizer_price": safe_float(self.selected_optimizer_price),
            "optimizer_count": count_optimizers,
        }
        return data