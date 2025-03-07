import json
import os

def load_json_data(filename):
    base_dir = os.path.join(os.path.dirname(__file__), "..", "database")
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def import_data_from_single_file(db_instance, filename, mapping):
    data = load_json_data(filename)
    for key, table in mapping.items():
        if db_instance.count_records(table) == 0:
            if key in data:
                records = data[key]
                for record in records:
                    db_instance.insert_record(table, record)
