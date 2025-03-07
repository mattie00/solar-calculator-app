import customtkinter as ctk

def create_label(parent, text, row, column):
    label = ctk.CTkLabel(parent, text=text, font=("Arial", 12, "normal"))
    label.grid(row=row, column=column, pady=5, sticky="w", padx=(10, 0))
    return label

def create_bold_label(parent, text, row, column):
    label = ctk.CTkLabel(parent, text=text, font=("Arial", 14, "bold"))
    label.grid(row=row, column=column, pady=5, sticky="w", padx=(10, 0))
    return label

def create_section_label(parent, text, row, column):
    label = ctk.CTkLabel(parent, text=text, font=("Arial", 16, "bold"), text_color="#2fa572")
    label.grid(row=row, column=column, pady=5, sticky="w", padx=(10, 0), columnspan=2)
    return label

def settings_label(parent, text, **kwargs):
    label = ctk.CTkLabel(parent, text=text, font=("Arial", 16, "bold"), text_color="#2fa572", **kwargs)
    label.pack(pady=10)
    return label

def create_combobox(parent, row, column, **kwargs):
    kwargs.setdefault("state", "readonly")
    placeholder = kwargs.pop("placeholder_text", "Wybierz z listy")
    combobox = ctk.CTkComboBox(parent, **kwargs)
    combobox.set(placeholder)
    combobox.grid(row=row, column=column, sticky="ew", padx=10, pady=5)
    return combobox

def create_entry(parent, row, column, **kwargs):
    kwargs.setdefault("placeholder_text", "Wprowadź dane")
    entry = ctk.CTkEntry(parent, **kwargs)
    entry.grid(row=row, column=column, sticky="ew", padx=10, pady=5)
    return entry

def create_active_label(parent, row, column, **kwargs):
    label = ctk.CTkLabel(parent, **kwargs)
    label.grid(row=row, column=column, sticky="ew",padx=10, pady=5)
    return label

def go_to_menu(self):
    self.parent.show_screen(self.parent.menu_screen)

def safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

def safe_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default