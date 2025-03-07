import customtkinter as ctk

from app.settings.sections.cable_ac import CableACSettingsFrame
from app.settings.sections.cable_dc import CableDCSettingsFrame
from app.settings.sections.installation_direction import InstallationDirectionSettingsFrame
from app.settings.sections.installation import InstallationSettingsFrame
from app.settings.sections.inverter import InverterSettingsFrame
from app.settings.sections.module import ModuleSettingsFrame
from app.settings.sections.optimizer import OptimizerSettingsFrame
from app.settings.sections.promotion import PromotionSettingsFrame
from app.settings.sections.rafter import RafterSettingsFrame
from app.settings.sections.security import SecuritySettingsFrame
from app.settings.sections.support import SupportSettingsFrame
from app.settings.sections.warehouse import WarehouseSettingsFrame
from utils.helpers import go_to_menu
from utils.data_importer import import_data_from_single_file


class SettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, db_instance=None):
        super().__init__(parent.main_frame, fg_color="transparent")
        self.parent = parent
        self.db_instance = db_instance

        self.menu_frame = ctk.CTkFrame(self, width=250)
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Moduły", command=lambda: self.show_frame(ModuleSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Inwertery", command=lambda: self.show_frame(InverterSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Magazyny", command=lambda: self.show_frame(WarehouseSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Zabezpieczenia", command=lambda: self.show_frame(SecuritySettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Konstrukcje wsporcze", command=lambda: self.show_frame(SupportSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Kierunki instalacji", command=lambda: self.show_frame(InstallationDirectionSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Miejsca wpięcia", command=lambda: self.show_frame(InstallationSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Typy AC", command=lambda: self.show_frame(CableACSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Typy DC", command=lambda: self.show_frame(CableDCSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Optymalizatory", command=lambda: self.show_frame(OptimizerSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Typy pokrycia dachu", command=lambda: self.show_frame(RafterSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Promocje", command=lambda: self.show_frame(PromotionSettingsFrame))
        self.modules_btn.pack(pady=5, fill="x")

        self.import_btn = ctk.CTkButton(self.menu_frame, text="Zaimportuj podstawowe dane", command=self.import_default_data)
        self.import_btn.pack(pady=(50, 5), fill="x")

        self.modules_btn = ctk.CTkButton(self.menu_frame, text="Powrót to menu",command=lambda: go_to_menu(self))
        self.modules_btn.pack(pady=(10,5), fill="x")

        self.current_frame = None
        self.show_frame(ModuleSettingsFrame)

    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.content_frame,db_instance=self.db_instance)
        self.current_frame.pack(fill="both", expand=True)

    def import_default_data(self):
        mapping = {
            "modules": "modules",
            "inverters": "inverters",
            "warehouse": "warehouses",
            "security": "security",
            "support": "support",
            "installation_direction": "installation_direction",
            "installation": "installation",
            "cable_ac": "cable_ac",
            "cable_dc": "cable_dc",
            "optimizers": "optimizers",
            "rafter": "rafter",
            "promotions": "promotions"
        }

        import_data_from_single_file(self.db_instance, "data.json", mapping)


