import customtkinter as ctk

from utils.helpers import go_to_menu


class Calculator2Screen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent.main_frame, fg_color="transparent")
        self.parent = parent

        title = ctk.CTkLabel(self, text="Kalkulator Rocznych Kosztów", font=("Arial", 20, "bold"), text_color="#2fa572")
        title.pack(pady=(15, 10))

        output_frame = ctk.CTkFrame(self, fg_color="transparent")
        output_frame.pack(fill="x", pady=10)

        self.frame = ctk.CTkFrame(output_frame)
        self.frame.pack(pady=10)

        ctk.CTkLabel(self.frame, text="Rok", font=('Arial', 16, 'bold'), text_color="#2fa572")\
            .grid(row=0, column=0, padx=55, pady=(15, 0), sticky="ew")
        ctk.CTkLabel(self.frame, text="Koszt roczny", font=('Arial', 16, 'bold'), text_color="#2fa572")\
            .grid(row=0, column=1, padx=55, pady=(15, 0), sticky="ew")
        ctk.CTkLabel(self.frame, text="Suma kosztów", font=('Arial', 16, 'bold'), text_color="#2fa572")\
            .grid(row=0, column=2, padx=55, pady=(15, 0), sticky="ew")
        ctk.CTkLabel(self.frame, text="Miesięczny koszt", font=('Arial', 16, 'bold'), text_color="#2fa572")\
            .grid(row=0, column=3, padx=55, pady=(15, 0), sticky="ew")

        self.years = []
        start_year = 2025
        end_year = 2035
        for i, year in enumerate(range(start_year, end_year + 1), start=1):
            pady_value = (0, 15) if year == end_year else 5
            ctk.CTkLabel(self.frame, text=str(year)).grid(row=i, column=0, padx=10, pady=pady_value, sticky="ew")
            yearly_cost_label = ctk.CTkLabel(self.frame, text="")
            yearly_cost_label.grid(row=i, column=1, padx=10, pady=pady_value, sticky="ew")
            sum_cost_label = ctk.CTkLabel(self.frame, text="")
            sum_cost_label.grid(row=i, column=2, padx=10, pady=pady_value, sticky="ew")
            monthly_cost_label = ctk.CTkLabel(self.frame, text="")
            monthly_cost_label.grid(row=i, column=3, padx=10, pady=pady_value, sticky="ew")
            self.years.append({
                'year': year,
                'cost_label': yearly_cost_label,
                'sum_cost_label': sum_cost_label,
                'monthly_cost_label': monthly_cost_label
            })

        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.pack(fill="x", pady=10)

        center_frame1 = ctk.CTkFrame(input_frame, fg_color="transparent")
        center_frame1.pack(pady=10)

        left_frame = ctk.CTkFrame(center_frame1, fg_color="transparent")
        left_frame.pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(left_frame, text="Koszt na rok 2025", font=("Arial", 14, "bold"), text_color="#2fa572")\
            .pack(side="top", padx=5, pady=(0, 5))
        self.input2 = ctk.CTkEntry(left_frame, placeholder_text="Wprowadź dane", width=250)
        self.input2.pack(side="top", padx=5, pady=(0, 15))

        right_mid = ctk.CTkFrame(center_frame1, fg_color="transparent")
        right_mid.pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(right_mid, text="Koszt na rok 2026 (opcjonalny)", font=("Arial", 14, "bold"), text_color="#2fa572")\
            .pack(side="top", padx=5, pady=(0, 5))
        self.input4 = ctk.CTkEntry(right_mid, placeholder_text="Wprowadź dane", width=250)
        self.input4.pack(side="top", padx=5, pady=(0, 15))

        right_frame = ctk.CTkFrame(center_frame1, fg_color="transparent")
        right_frame.pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(right_frame, text="Wprowadź % wzrostu", font=("Arial", 14, "bold"), text_color="#2fa572")\
            .pack(side="top", padx=5, pady=(0, 5))
        self.input6 = ctk.CTkEntry(right_frame, placeholder_text="Wprowadź dane", width=250)
        self.input6.pack(side="top", padx=5, pady=(0, 15))
        self.input6.insert(0, "7")

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", pady=10)
        center_frame2 = ctk.CTkFrame(button_frame, fg_color="transparent")
        center_frame2.pack(pady=10)
        calc_button = ctk.CTkButton(center_frame2, text="Oblicz", command=self.calc)
        calc_button.pack(side="left", padx=5)
        back_button = ctk.CTkButton(center_frame2, text="Powrót do menu", command=lambda: go_to_menu(self))
        back_button.pack(side="left", padx=5)

    def calc(self):
        try:
            percent = float(self.input6.get()) / 100

            cost_2025_str = self.input2.get()
            if not cost_2025_str:
                print("Proszę wprowadzić koszt dla roku 2025.")
                return
            cost_2025 = round(float(cost_2025_str))

            cost_2026_str = self.input4.get()
            if cost_2026_str:
                cost_2026 = round(float(cost_2026_str))
            else:
                cost_2026 = round(cost_2025 * (1 + percent))

            self.years[0]['cost_label'].configure(text=f"{cost_2025} zł")
            self.years[0]['sum_cost_label'].configure(text=f"{cost_2025} zł")
            self.years[0]['monthly_cost_label'].configure(text=f"{round(cost_2025 / 12)} zł")

            self.years[1]['cost_label'].configure(text=f"{cost_2026} zł")
            sum_cost_2026 = round(cost_2025 + cost_2026)
            self.years[1]['sum_cost_label'].configure(text=f"{sum_cost_2026} zł")
            self.years[1]['monthly_cost_label'].configure(text=f"{round(cost_2026 / 12)} zł")

            previous_cost = cost_2026
            cumulative_sum = sum_cost_2026

            for i in range(2, len(self.years)):
                current_cost = round(previous_cost * (1 + percent))
                cumulative_sum += current_cost

                self.years[i]['cost_label'].configure(text=f"{current_cost} zł")
                self.years[i]['sum_cost_label'].configure(text=f"{cumulative_sum} zł")
                self.years[i]['monthly_cost_label'].configure(text=f"{round(current_cost / 12)} zł")

                previous_cost = current_cost

        except ValueError:
            print("Proszę wprowadzić poprawne dane liczbowe.")
