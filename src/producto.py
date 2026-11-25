"""E02 · La regla vive en el objeto: una property protege las existencias."""


class MovimientoInvalido(Exception):
    """Rechazo de negocio: el movimiento dejaría el inventario en un estado no permitido."""


class Producto:
    alerta_stock = 3  # atributo de CLASE: el mismo para todos los productos

    def __init__(self, sku, nombre, existencias):
        self.sku = sku            # atributos de INSTANCIA: propios de cada producto
        self.nombre = nombre
        self.existencias = existencias  # pasa por el setter: la regla se aplica desde el inicio

    @property
    def existencias(self):
        return self._existencias

    @existencias.setter
    def existencias(self, valor):
        if valor < 0:  # REGLA: nunca quedar con stock negativo
            raise MovimientoInvalido(f"Existencias inválidas: {valor}")
        self._existencias = valor

    def registrar_salida(self, cantidad):
        if cantidad <= 0:
            raise ValueError(f"Cantidad inválida: {cantidad}. Debe ser positiva")
        if cantidad > self.existencias:
            raise MovimientoInvalido(f"Stock insuficiente: hay {self.existencias}, se piden {cantidad}")
        self.existencias -= cantidad
        return self.existencias

    def necesita_pedido(self):
        return self.existencias <= self.alerta_stock

    def __repr__(self):  # para quien programa: sin ambigüedad
        return f"Producto(sku={self.sku!r}, existencias={self.existencias})"

    def __str__(self):   # para quien usa el sistema: legible
        return f"{self.nombre}: {self.existencias} unidades"
