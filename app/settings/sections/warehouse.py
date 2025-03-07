from app.settings.settings_frame_base import BaseSettingsFrame


class WarehouseSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "name": "Nazwa magazynu:",
                "warranty": "Gwarancja:",
                "price": "Cena:"
            },
            "display": ["name", "warranty", "price"],
            "numeric": ["price"]
        }
        super().__init__(master, table_name="warehouses", columns_config=columns_config, db_instance=db_instance, **kwargs)