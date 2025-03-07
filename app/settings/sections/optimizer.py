from app.settings.settings_frame_base import BaseSettingsFrame


class OptimizerSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "name": "Nazwa optymalizatora:",
                "price": "Cena:"
            },
            "display": ["name", "price"],
            "numeric": ["price"]
        }
        super().__init__(master, table_name="optimizers", columns_config=columns_config, db_instance=db_instance, **kwargs)
