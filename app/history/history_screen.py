import customtkinter as ctk
import json

from tkinter.filedialog import asksaveasfilename
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from utils.helpers import settings_label, go_to_menu
from app.history.friendly_names import format_calculation_data


class HistoryScreen(ctk.CTkFrame):
    def __init__(self, parent, db_instance=None):
        super().__init__(parent.main_frame, fg_color="transparent")
        self.parent = parent
        self.db_instance = db_instance
        self.current_record_id = None

        self.menu_frame = ctk.CTkFrame(self, width=250)
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        settings_label(self.menu_frame, "Historia kalkulacji")

        self.history_list = ctk.CTkScrollableFrame(self.menu_frame, width=400)
        self.history_list.pack(fill="both", expand=True, padx=5, pady=5)

        self.refresh_btn = ctk.CTkButton(self.menu_frame, text="Odśwież", command=self.load_history)
        self.refresh_btn.pack(pady=5, fill="x")

        settings_label(self.content_frame, "Podgląd kalkulacji")

        self.preview_text = ctk.CTkTextbox(self.content_frame, width=500, height=400)
        self.preview_text.pack(padx=10, pady=10, fill="both", expand=True)

        self.pdf_btn = ctk.CTkButton(self.content_frame, text="Zapisz jako PDF", command=self.save_as_pdf)
        self.pdf_btn.pack(side="left", padx=10, pady=5)

        self.delete_btn = ctk.CTkButton(self.content_frame, text="Usuń", command=self.delete_record)
        self.delete_btn.pack(side="left", padx=10, pady=5)

        self.back_btn = ctk.CTkButton(self, text="Powrót do menu", command=lambda: go_to_menu(self))
        self.back_btn.pack(side="right", fill="x", padx=10, pady=10)

        self.load_history()

    def load_history(self):
        for widget in self.history_list.winfo_children():
            widget.destroy()
        query = "SELECT id, record_name, created_at FROM calculations ORDER BY created_at DESC"
        cur = self.db_instance.execute_query(query)
        rows = cur.fetchall() if cur else []
        for row in rows:
            text = f"{row['record_name']} ({row['created_at']})"
            btn = ctk.CTkButton(
                self.history_list,
                text=text,
                anchor="w",
                command=lambda rid=row["id"]: self.load_record(rid)
            )
            btn.pack(fill="x", pady=2, padx=5)

    def load_record(self, record_id):
        self.current_record_id = record_id
        query = "SELECT data FROM calculations WHERE id = ?"
        cur = self.db_instance.execute_query(query, (record_id,))
        row = cur.fetchone() if cur else None
        self.preview_text.delete("1.0", ctk.END)
        if row:
            try:
                data = json.loads(row["data"])
                formatted = format_calculation_data(data)
            except Exception:
                formatted = row["data"]
            self.preview_text.insert(ctk.END, formatted)

    def delete_record(self):
        if not self.current_record_id:
            return
        query = "DELETE FROM calculations WHERE id = ?"
        self.db_instance.execute_query(query, (self.current_record_id,))
        self.current_record_id = None
        self.load_history()
        self.preview_text.delete("1.0", ctk.END)

    def save_as_pdf(self):
        if not self.current_record_id:
            return
        filename = asksaveasfilename(defaultextension=".pdf", initialfile="Kalkulacja.pdf", filetypes=[("PDF files", "*.pdf")])
        if not filename:
            return
        query = "SELECT data FROM calculations WHERE id = ?"
        cur = self.db_instance.execute_query(query, (self.current_record_id,))
        row = cur.fetchone() if cur else None
        if row:
            try:
                data = json.loads(row["data"])
                formatted = format_calculation_data(data)
            except Exception:
                formatted = row["data"]
        else:
            formatted = "Brak danych"
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        for line in formatted.splitlines():
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 12))
        try:
            doc.build(story)
            # Możesz dodać komunikat o sukcesie, np.:
            # self.notifications_label.configure(text="PDF zapisany pomyślnie", text_color="green")
        except Exception as e:
            # self.notifications_label.configure(text=f"Błąd zapisu PDF: {e}", text_color="red")
            pass
