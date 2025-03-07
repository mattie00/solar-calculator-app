from app.settings.settings_frame_base import BaseSettingsFrame

class ModuleSettingsFrame(BaseSettingsFrame):
    def __init__(self, master, db_instance=None, **kwargs):
        columns_config = {
            "form": {
                "name": "Nazwa modułu:",
                "product_warranty": "Gwarancja produktu:",
                "performance_warranty": "Gwarancja liniowa:",
                "power": "Moc (W):",
                "price": "Cena:"
            },
            "display": ["name", "product_warranty", "performance_warranty", "power", "price"],
            "numeric": ["power", "price"]
        }
        super().__init__(master, table_name="modules", columns_config=columns_config, db_instance=db_instance, **kwargs)