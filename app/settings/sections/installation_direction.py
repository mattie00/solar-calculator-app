from app.settings.settings_frame_base import BaseSettingsFrame


class InstallationDirectionSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "direction": "Kierunek instalacji:",
                "price": "Cena:"
            },
            "display": ["direction", "price"],
            "numeric": ["price"]
        }
        super().__init__(master, table_name="installation_direction", columns_config=columns_config, db_instance=db_instance, **kwargs)