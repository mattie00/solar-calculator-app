import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent.main_frame)

        self.parent = parent

        title_label = ctk.CTkLabel(self, text="Menu Główne", font=("Arial", 28, "bold"))
        title_label.pack(pady=40)

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(expand=True)

        buttons = [
            ("Rozpocznij nową kalkulację", lambda: self.parent.show_screen(self.parent.calculator_screen)),
            ("Kalkulator Cen Prądu", lambda: self.parent.show_screen(self.parent.calculator2_screen)),
            ("Zobacz Historię Kalkulacji", lambda: self.parent.show_screen(self.parent.history_screen)),
            ("Ustawienia", lambda: self.parent.show_screen(self.parent.settings_screen)),
            ("Zamknij", self.parent.quit)
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(button_frame, text=text, command=command, width=200)
            btn.pack(pady=10)
