from etiquetas import etiqueta, slug
from producto import Producto


def test_slug_quita_tildes_y_espacios():
    assert slug("  Café de Santa Elena ") == "cafe-de-santa-elena"


def test_etiqueta_une_sku_y_nombre():
    panela = Producto("panela-1kg", "Panela de Barbosa 1 kg", 8)
    assert etiqueta(panela) == "panela-1kg-panela-de-barbosa-1-kg"
