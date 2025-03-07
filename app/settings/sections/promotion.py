from app.settings.settings_frame_base import BaseSettingsFrame


class PromotionSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "name": "Nazwa promocji:",
                "amount": "Kwota:"
            },
            "display": ["name", "amount"],
            "numeric": ["amount"]
        }
        super().__init__(master, table_name="promotions", columns_config=columns_config, db_instance=db_instance, **kwargs)
