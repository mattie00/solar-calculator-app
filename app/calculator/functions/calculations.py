from utils.helpers import safe_int, safe_float


def calculate_inverter_cost(inverters_data):
    count = safe_int(inverters_data.get("inverter_count"))
    price = safe_float(inverters_data.get("inverter_price"))
    return count * price

def calculate_warehouse_cost(warehouse_data):
    count = safe_int(warehouse_data.get("warehouse_count"))
    price = safe_float(warehouse_data.get("warehouse_price"))
    return count * price

def calculate_module_cost(modules_data):
    count = safe_int(modules_data.get("module_count"))
    price = safe_float(modules_data.get("module_price"))
    direction_price = safe_float(modules_data.get("installation_direction_price"))
    return (count * price) + direction_price

def calculate_optimizer_cost(optimizers_data):
    count = safe_int(optimizers_data.get("optimizer_count"))
    price = safe_float(optimizers_data.get("optimizer_price"))
    return count * price

def calculate_promotion_cost(promotions_data):
    return safe_float(promotions_data.get("promotion_amount"), 0.00)

def calculate_route_cost(routes_data):
    trench_length = safe_int(routes_data.get("trench_length"))
    dc_length = safe_int(routes_data.get("dc_route_length"))
    ac_length = safe_int(routes_data.get("ac_route_length"))
    dc_price = safe_float(routes_data.get("dc_cable_price"))
    ac_price = safe_float(routes_data.get("ac_cable_price"))

    ac_cost = ac_price * ac_length

    if trench_length >= 1:
        dc_cost = (dc_price * dc_length) + (15 * trench_length) + 300
    else:
        dc_cost = dc_price * dc_length

    return ac_cost + dc_cost

def calculate_security_cost(security_data):
    return safe_float(security_data.get("security_price"))

def calculate_structure_cost(structure_data):
    construction = safe_float(structure_data.get("construction_price"))
    rafter = safe_float(structure_data.get("rafter_price"))
    return  construction + rafter

def calculate_total_cost(modules_data, inverters_data, optimizers_data, structure_data, routes_data, security_data, promotions_data):

    modules = calculate_module_cost(modules_data)
    inverters = calculate_inverter_cost(inverters_data)
    warehouse = calculate_warehouse_cost(inverters_data)
    optimizers = calculate_optimizer_cost(optimizers_data)
    route = calculate_route_cost(routes_data)
    security = calculate_security_cost(security_data)
    structure = calculate_structure_cost(structure_data)
    promotion = calculate_promotion_cost(promotions_data)

    total_brutto = modules + inverters + warehouse + optimizers + structure + route + security + promotion

    return total_brutto

def calculate_net_cost(total_brutto, vat):
    if vat:
        return total_brutto / (1 + vat / 100)
    return total_brutto