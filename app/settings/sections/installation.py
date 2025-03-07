from app.settings.settings_frame_base import BaseSettingsFrame


class InstallationSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "location": "Lokalizacja:"
            },
            "display": ["location"],
            "numeric": []
        }
        super().__init__(master, table_name="installation", columns_config=columns_config, db_instance=db_instance, **kwargs)