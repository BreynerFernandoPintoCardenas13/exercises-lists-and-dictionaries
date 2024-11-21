import json

# Función para leer el archivo JSON
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Función para escribir en el archivo JSON
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para añadir una nueva factura
def add_invoice(invoice_number, cost, invoices):
    invoices[invoice_number] = cost
    return invoices

# Función para pagar una factura
def pay_invoice(invoice_number, invoices):
    if invoice_number in invoices:
        del invoices[invoice_number]
        return invoices
    else:
        print(f"Factura {invoice_number} no encontrada.")
        return invoices

# Función para calcular los totales de cobrado y pendiente
def calculate_totals(invoices):
    total_pending = sum(invoices.values())
    total_paid = 0  # Al principio no se han pagado facturas
    print(f"\nCantidad pendiente de cobro: {total_pending}")
    print(f"Cantidad cobrada: {total_paid}")
    return total_pending, total_paid
