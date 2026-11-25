"""Etiqueta legible para el estante: sin tildes ni espacios."""
from unidecode import unidecode


def slug(nombre):
    texto = unidecode(nombre).lower().strip()
    return "-".join(texto.split())


def etiqueta(producto):
    return f"{producto.sku}-{slug(producto.nombre)}"
