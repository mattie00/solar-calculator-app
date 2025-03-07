from app.settings.settings_frame_base import BaseSettingsFrame


class InverterSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "name": "Nazwa inwertera:",
                "warranty": "Gwarancja:",
                "type": "Typ inwertera:",
                "phases": "Fazy inwertera:",
                "price": "Cena:"
            },
            "display": ["name", "warranty", "type", "phases", "price"],
            "numeric": ["price"]
        }
        super().__init__(master, table_name="inverters", columns_config=columns_config, db_instance=db_instance, **kwargs)