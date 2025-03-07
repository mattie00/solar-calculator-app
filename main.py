import customtkinter as ctk

from app.additional_calculator.calculator2_screen import Calculator2Screen
from app.calculator.calculator_screen import CalculatorScreen
from app.history.history_screen import HistoryScreen
from app.main_menu import MainMenu
from app.settings.settings_screen import SettingsScreen
from setup_databases import setup_calculator_db


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        calc_db = setup_calculator_db()

        self.title("Solar Calculator")
        self.geometry("1680x980")
        self.eval('tk::PlaceWindow . center')

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.menu_screen = MainMenu(self)
        self.calculator_screen = CalculatorScreen(self, db_instance=calc_db)
        self.calculator2_screen = Calculator2Screen(self)
        self.settings_screen = SettingsScreen(self, db_instance=calc_db)
        self.history_screen = HistoryScreen(self, db_instance=calc_db)

        self.show_screen(self.menu_screen)

    def show_screen(self, screen):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()
        screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = App()
    app.mainloop()
