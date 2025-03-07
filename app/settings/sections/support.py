from app.settings.settings_frame_base import BaseSettingsFrame

class SupportSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "type": "Typ konstrukcji wsporczej:",
                "price": "Cena:"
            },
            "display": ["type", "price"],
            "numeric": ["price"]
        }
        super().__init__(master, table_name="support", columns_config=columns_config, db_instance=db_instance, **kwargs)





