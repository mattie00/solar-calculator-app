import customtkinter as ctk
from utils.helpers import create_label, create_entry, settings_label

class BaseSettingsFrame(ctk.CTkFrame):
    def __init__(self, master, table_name, columns_config, db_instance=None, **kwargs):
        super().__init__(master, **kwargs)
        self.db_instance = db_instance
        self.table_name = table_name
        self.columns_config = columns_config
        self.selected_id = None
        self.new_entries = {}

        self.grid_columnconfigure(0, weight=1)
        settings_label(self, f"Zarządzanie danymi {table_name}")

        self.list_frame = ctk.CTkScrollableFrame(self, height=250)
        self.list_frame.pack(padx=10, pady=10, fill="both", expand=False)

        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.pack(pady=10)

        self.refresh_btn = ctk.CTkButton(self.btn_frame, text="Odśwież", command=self.load_data)
        self.refresh_btn.pack(side="left", padx=10)
        self.delete_btn = ctk.CTkButton(self.btn_frame, text="Usuń zaznaczone", command=self.delete_selected)
        self.delete_btn.pack(side="left", padx=10)

        settings_label(self, "Wprowadzanie nowych danych")

        form_container = ctk.CTkFrame(self)
        form_container.pack(pady=10, padx=10)

        form_frame = ctk.CTkFrame(form_container)
        form_frame.pack()

        row = 0

        for key, label_text in self.columns_config["form"].items():
            create_label(form_frame, label_text, row, 0)
            entry = create_entry(form_frame, row, 1, width=300)
            self.new_entries[key] = entry
            row += 1

        self.add_btn = ctk.CTkButton(form_frame, text="Dodaj", command=self.add_new)
        self.add_btn.grid(row=row, column=0, columnspan=2, pady=10)
        self.load_data()

    def load_data(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        query = f"SELECT id, {', '.join(self.columns_config['display'])} FROM {self.table_name}"
        cur = self.db_instance.execute_query(query)
        rows = cur.fetchall() if cur else []
        for row in rows:
            display_text = " | ".join([f"{col}: {row[col]}" for col in self.columns_config["display"]])
            text = f"{row['id']} - {display_text}"
            btn_color = "darkgreen" if self.selected_id == row["id"] else None
            btn = ctk.CTkButton(
                self.list_frame,
                text=text,
                anchor="w",
                command=lambda rid=row["id"]: self.select_record(rid),
                fg_color=btn_color
            )
            btn.pack(fill="x", pady=2, padx=5)

    def select_record(self, record_id):
        self.selected_id = record_id
        self.load_data()

    def add_new(self):
        data = {}
        for key, entry in self.new_entries.items():
            value = entry.get().strip()
            if key in self.columns_config.get("numeric", []):
                try:
                    value = float(value)
                except ValueError:
                    value = 0
            data[key] = value
        if not data.get("name"):
            return
        self.db_instance.insert_record(self.table_name, data)
        for entry in self.new_entries.values():
            entry.delete(0, "end")
        self.load_data()

    def delete_selected(self):
        if not self.selected_id:
            return
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.db_instance.execute_query(query, (self.selected_id,))
        self.selected_id = None
        self.load_data()
