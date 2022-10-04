#descuento del 15%

montototal = float(input("Monto total ->  "))

descuento = 0.15 * montototal
pagar = montototal - descuento

print(f"El usuario debe cancelar S/{pagar:.2f} ")
