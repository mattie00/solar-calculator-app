import datetime
import json
import customtkinter as ctk
from app.calculator.functions.calculation_summary import perform_calculations_summary
from utils.helpers import create_section_label, create_label, \
    create_active_label, safe_float, go_to_menu


class SummaryFrame(ctk.CTkFrame):
    def __init__(self, master, calculator_screen=None, **kwargs):
        super().__init__(master, **kwargs)
        self.last_brutto = None
        self.last_net = None
        self.calculator_screen = calculator_screen

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Podsumowanie", 0, 0)

        create_label(self, "Cena instalacji netto", 1, 0)
        self.net_price_label = create_active_label(self, 1, 1, text="Uzupełnij dane")

        create_label(self, "Cena instalacji brutto", 2, 0)
        self.gross_price_label = create_active_label(self, 2, 1, text="Uzupełnij dane")

        create_label(self, "Powiadomienia", 4, 0)
        self.notifications_label = create_active_label(self, 4, 1, text="Brak")

        self.calculate_button = ctk.CTkButton(self, text="Oblicz", command=self.perform_calculations)
        self.calculate_button.grid(row=6, column=0, columnspan=2, sticky="ew", pady=5, padx=10)

        self.save_button = ctk.CTkButton(self, text="Zapisz kalkulacje", command=self.save_calculations, state="disabled")
        self.save_button.grid(row=7, column=0, columnspan=2, sticky="ew", pady=5, padx=10)

        self.back_button = ctk.CTkButton(self, text="Powrót do menu", command=self.calculator_screen.go_back_to_menu)
        self.back_button.grid(row=8, column=0, columnspan=2, sticky="ew", pady=5, padx=10)

    def perform_calculations(self):
        modules_data = self.calculator_screen.pv_modules_frame.get_modules_data()
        inverters_data = self.calculator_screen.inverters_frame.get_inverters_data()
        optimizers_data = self.calculator_screen.optimizers_frame.get_optimizers_data()
        structure_data = self.calculator_screen.structure_frame.get_structure_data()
        routes_data = self.calculator_screen.router_frame.get_routes_data()
        security_data = self.calculator_screen.security_frame.get_security_data()
        promotions_data = self.calculator_screen.promotion_frame.get_promotions_data()
        investor_data = self.calculator_screen.investor_frame.get_investor_data()

        result, message = perform_calculations_summary(
            modules_data, inverters_data, optimizers_data, structure_data,
            routes_data, security_data, promotions_data, investor_data
        )
        if result is None:
            self.notifications_label.configure(text=message, text_color="red")
            self.save_button.configure(state="disabled")
            return

        total_net, total_brutto = result
        self.net_price_label.configure(text=f"Cena instalacji netto: {total_net:.2f} PLN")
        self.gross_price_label.configure(text=f"Cena instalacji brutto: {total_brutto:.2f} PLN")
        self.notifications_label.configure(text=message, text_color="green")
        self.save_button.configure(state="normal")
        self.last_net = total_net
        self.last_brutto = total_brutto

    def get_summary_data(self):
        modules_data = self.calculator_screen.pv_modules_frame.get_modules_data()
        inverters_data = self.calculator_screen.inverters_frame.get_inverters_data()
        optimizers_data = self.calculator_screen.optimizers_frame.get_optimizers_data()
        structure_data = self.calculator_screen.structure_frame.get_structure_data()
        routes_data = self.calculator_screen.router_frame.get_routes_data()
        security_data = self.calculator_screen.security_frame.get_security_data()
        promotions_data = self.calculator_screen.promotion_frame.get_promotions_data()
        investor_data = self.calculator_screen.investor_frame.get_investor_data()

        calculation_data = {
            "investor_data": investor_data,
            "modules_data": modules_data,
            "inverters_data": inverters_data,
            "optimizers_data": optimizers_data,
            "structure_data": structure_data,
            "routes_data": routes_data,
            "security_data": security_data,
            "promotions_data": promotions_data,
            "total_net": f"{getattr(self, 'last_net', 0):.2f}",
            "total_brutto": f"{getattr(self, 'last_brutto', 0):.2f}"
        }
        return calculation_data

    def save_calculations(self):
        calculation_data = self.get_summary_data()
        if safe_float(calculation_data.get("total_brutto")) == 0:
            self.notifications_label.configure(text="Brak danych do zapisu (wykonaj obliczenia)", text_color="red")
            return

        investor_name = self.calculator_screen.investor_frame.investor_name.get().strip().replace(" ", "_")
        current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        record_name = f"{investor_name}_{current_date}.json"
        calculation_data["record_name"] = record_name
        calculation_data["created_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        calculation_json = json.dumps(calculation_data, ensure_ascii=False)
        record = {
            "record_name": record_name,
            "data": calculation_json,
            "created_at": calculation_data["created_at"]
        }
        result_id = self.calculator_screen.db_instance.insert_record("calculations", record)
        if result_id:
            self.notifications_label.configure(text="Kalkulacje zapisane pomyślnie", text_color="green")
        else:
            self.notifications_label.configure(text="Błąd zapisu kalkulacji", text_color="red")
