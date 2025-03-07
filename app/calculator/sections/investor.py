import customtkinter as ctk

from utils.helpers import create_label, create_section_label, create_combobox, \
    create_entry

INVESTOR = ["Osoba prywatna", "Firma"]

class InvestorFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        create_section_label(self, "Dane inwestora", 0, 0)

        create_label(self, "Inwestor", 1, 0)
        self.investor = create_combobox(self, 1, 1, values=INVESTOR)
        self.investor.set("Osoba prywatna")

        create_label(self, "Imię i nazwisko / Nazwa firmy", 2, 0)
        self.investor_name = create_entry(self, 2, 1)

        create_label(self, "NIP (Opcjonalne)", 3, 0)
        self.investor_nip = create_entry(self, 3, 1)

        create_label(self, "Email", 4, 0)
        self.investor_email = create_entry(self, 4, 1)

        create_label(self, "Numer telefonu", 5, 0)
        self.investor_phone = create_entry(self, 5, 1)

        create_label(self, "Osoba reprezentująca", 6, 0)
        self.investor_representative = create_entry(self, 6, 1)

        create_label(self, "Ulica i nr", 7, 0)
        self.investor_street = create_entry(self, 7, 1)

        create_label(self, "Miasto", 8, 0)
        self.investor_city = create_entry(self, 8, 1)

        create_label(self, "Kod pocztowy", 9, 0)
        self.investor_postal_code = create_entry(self, 9, 1)

    def get_investor_data(self):
        investor_type = self.investor.get()

        if investor_type == "Osoba prywatna":
            vat = 8
        elif investor_type == "Firma":
            vat = 23
        else:
            vat = 0

        data = {
            "investor": investor_type,
            "investor_name": self.investor_name.get(),
            "investor_nip": self.investor_nip.get(),
            "investor_email": self.investor_email.get(),
            "investor_phone": self.investor_phone.get(),
            "investor_representative": self.investor_representative.get(),
            "investor_street": self.investor_street.get(),
            "investor_city": self.investor_city.get(),
            "investor_postal_code": self.investor_postal_code.get(),
            "vat": vat
        }
        return data