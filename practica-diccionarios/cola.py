class ColaDoble:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0,item)

    def removerFrente(self):
        return self.items.pop()

    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

d = ColaDoble()
print(d.estaVacia())
d.agregarFinal(4)
d.agregarFinal('perro')
d.agregarFrente('gato')
d.agregarFrente(True)
print(d.tamano())
print(d.estaVacia())
d.agregarFinal(8.4)
print(d.removerFinal())
print(d.removerFrente())
print (d.tamano())