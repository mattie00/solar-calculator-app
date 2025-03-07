def get_friendly_names():
    friendly = {
        "investor": "Typ Inwestora",
        "investor_name": "Imię i Nazwisko / Nazwa firmy",
        "investor_nip": "NIP",
        "investor_email": "Email",
        "investor_phone": "Numer telefonu",
        "investor_representative": "Osoba reprezentująca",
        "investor_street": "Ulica i nr",
        "investor_city": "Miasto",
        "investor_postal_code": "Kod pocztowy",
        "vat": "Stawka VAT",
        "module_name": "Nazwa modułu",
        "module_count": "Ilość modułów",
        "module_product_warranty": "Gwarancja produktu",
        "module_performance_warranty": "Gwarancja liniowa",
        "module_total_power": "Łączna moc modułów",
        "installation_direction": "Kierunek instalacji",
        "roof_angle": "Kąt nachylenia dachu",
        "inverter_name": "Nazwa inwertera",
        "inverter_count": "Ilość inwerterów",
        "inverter_warranty": "Gwarancja inwertera",
        "inverter_phases": "Fazy inwertera",
        "warehouse_name": "Nazwa magazynu",
        "warehouse_count": "Ilość magazynów",
        "warehouse_warranty": "Gwarancja magazynu",
        "optimizer_name": "Nazwa optymalizatora",
        "optimizer_count": "Ilość optymalizatorów",
        "construction_type": "Typ konstrukcji wsporczej",
        "rafter_type": "Rodzaj krokwi",
        "trench_length": "Długość przekopu",
        "trench_cable_type": "Typ przewodu w przekopie",
        "dc_cable_type": "Typ przewodu DC",
        "dc_route_length": "Długość trasy DC",
        "ac_cable_type": "Typ przewodu AC",
        "ac_route_length": "Długość trasy AC",
        "installation_point": "Punkt instalacji",
        "security_type": "Typ zabezpieczenia",
        "building_volume": "Objętość budynku",
        "promotion_name": "Nazwa promocji",
        "total_net": "Cena netto",
        "total_brutto": "Cena brutto",
    }
    return friendly

def flatten_calculation_data(calc_data):
    flat = {}
    for key, value in calc_data.items():
        if isinstance(value, dict):
            flat.update(value)
        else:
            flat[key] = value
    return flat

def format_calculation_data(calc_data):
    friendly = get_friendly_names()
    flat = flatten_calculation_data(calc_data)
    lines = []
    for key, friendly_name in friendly.items():
        if key in flat:
            lines.append(f"{friendly_name}: {flat[key]}")
    return "\n".join(lines)
