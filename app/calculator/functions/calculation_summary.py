from app.calculator.functions.calculations import calculate_total_cost, calculate_net_cost
from utils.helpers import safe_int, safe_float


def perform_calculations_summary(modules_data, inverters_data, optimizers_data, structure_data, routes_data, security_data, promotions_data, investor_data):
    if modules_data.get("module_name") != "Brak" and safe_int(modules_data.get("module_count")) == 0:
        return None, "Wprowadź poprawną liczbę modułów"
    if inverters_data.get("inverter_name") != "Brak" and safe_int(inverters_data.get("inverter_count")) == 0:
        return None, "Wprowadź poprawną liczbę inwerterów"
    if optimizers_data.get("optimizer_name") != "Brak" and safe_int(optimizers_data.get("optimizer_count")) == 0:
        return None, "Wprowadź poprawną liczbę optymalizatorów"
    if inverters_data.get("warehouse_name") != "Brak" and safe_int(inverters_data.get("warehouse_count")) == 0:
        return None, "Wprowadź poprawną liczbę magazynów"

    ac_cable = routes_data.get("ac_cable_type")
    if ac_cable not in ["Brak", "Wybierz z listy", "Wybierz typ przewodu AC"]:
        ac_length = safe_int(routes_data.get("ac_route_length"))
        if ac_length < 1:
            return None, "Wprowadź poprawną długość trasy AC"

    dc_cable = routes_data.get("dc_cable_type")
    if dc_cable not in ["Brak", "Wybierz z listy", "Wybierz typ przewodu DC"]:
        dc_length = safe_int(routes_data.get("dc_route_length"))
        if dc_length < 1:
            return None, "Wprowadź poprawną długość trasy DC"

    total_brutto = calculate_total_cost(modules_data, inverters_data, optimizers_data, structure_data, routes_data, security_data, promotions_data)

    if safe_float(total_brutto) == 0:
        return None, "Wprowadź dane do kalkulatora"

    vat = investor_data.get("vat", 0)
    total_net = calculate_net_cost(total_brutto, vat)

    return (total_net, total_brutto), "Obliczenia zakończone pomyślnie"

