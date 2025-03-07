import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_combobox, \
    safe_float


class PromotionsFrame(ctk.CTkFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db_instance = db_instance

        self.selected_promotion_amount = 0

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Promocja", 0, 0)

        if self.db_instance:
            promotions_list = self.db_instance.fetch_combobox_values("promotions", "name")
        else:
            promotions_list = ["Brak danych"]

        promotions_list.insert(0, "Brak")

        create_label(self, "Wybierz promocje", 1, 0)
        self.promotion = create_combobox(self, 1, 1, values=promotions_list, command=self.update_promotions_info)


    def update_promotions_info(self, selected_value):
        if self.db_instance:
            query = "SELECT amount FROM promotions WHERE name = ?"
            cur = self.db_instance.execute_query(query, (selected_value,))
            row = cur.fetchone() if cur else None
            if row:
                self.selected_promotion_amount = row["amount"]
            else:
                self.selected_promotion_amount = 0
        else:
            self.selected_promotion_amount = 0

    def get_promotions_data(self):
        data = {
            "promotion_name": self.promotion.get(),
            "promotion_amount": safe_float(getattr(self, "selected_promotion_amount", 0))
        }
        return data