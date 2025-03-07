import customtkinter as ctk

from app.calculator.sections.investor import InvestorFrame
from app.calculator.sections.modules import PVModulesFrame
from app.calculator.sections.optimizers import OptimizersFrame
from app.calculator.sections.structure import StructureFrame
from app.calculator.sections.inverters import InvertersFrame
from app.calculator.sections.routes import RoutesFrame
from app.calculator.sections.security import SecurityFrame
from app.calculator.sections.promotions import PromotionsFrame
from app.calculator.sections.summary import SummaryFrame

class CalculatorScreen(ctk.CTkScrollableFrame):
    def __init__(self, parent, db_instance=None):
        super().__init__(parent.main_frame, fg_color="transparent")
        self.parent = parent
        self.db_instance = db_instance

        self.column0_frame = ctk.CTkFrame(self)
        self.column1_frame = ctk.CTkFrame(self)
        self.column2_frame = ctk.CTkFrame(self, fg_color="transparent")

        self.column0_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.column1_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.column2_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.investor_frame = InvestorFrame(self.column0_frame, fg_color="transparent")
        self.investor_frame.pack(padx=5, pady=5, fill="x")

        self.pv_modules_frame = PVModulesFrame(self.column0_frame, db_instance=self.db_instance, fg_color="transparent")
        self.pv_modules_frame.pack(padx=5, pady=5, fill="x")

        self.optimizers_frame = OptimizersFrame(self.column0_frame, db_instance=self.db_instance, fg_color="transparent")
        self.optimizers_frame.pack(padx=5, pady=5, fill="x")

        self.structure_frame = StructureFrame(self.column0_frame, db_instance=self.db_instance, fg_color="transparent")
        self.structure_frame.pack(padx=5, pady=5, fill="x")

        self.inverters_frame = InvertersFrame(self.column1_frame, db_instance=self.db_instance, fg_color="transparent")
        self.inverters_frame.pack(padx=5, pady=5, fill="x")

        self.router_frame = RoutesFrame(self.column1_frame, db_instance=self.db_instance, fg_color="transparent")
        self.router_frame.pack(padx=5, pady=5, fill="x")

        self.security_frame = SecurityFrame(self.column1_frame, db_instance=self.db_instance, fg_color="transparent")
        self.security_frame.pack(padx=5, pady=5, fill="x")

        self.promotion_frame = PromotionsFrame(self.column1_frame, db_instance=self.db_instance, fg_color="transparent")
        self.promotion_frame.pack(padx=5, pady=5, fill="x")

        self.summary_frame = SummaryFrame(self.column2_frame, calculator_screen=self, fg_color="transparent")
        self.summary_frame.pack(padx=5, pady=5, fill="both", expand=True)

    def go_back_to_menu(self):
        self.parent.show_screen(self.parent.menu_screen)