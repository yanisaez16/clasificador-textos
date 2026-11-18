import csv

import pytest

from main import clasificar, normalizar, procesar


def test_normalizar_quita_mayusculas_y_tildes():
    assert normalizar("Facturación ÁRBOL Contraseña") == "facturacion arbol contrasena"


@pytest.mark.parametrize("texto, esperada", [
    ("Me cobraron dos veces este mes", "facturacion"),
    ("Necesito la FACTURA de octubre", "facturacion"),
    ("La app se cierra sola", "tecnico"),
    ("El botón no hace nada", "tecnico"),
    ("Olvidé mi contraseña", "cuenta"),
    ("Olvide mi CONTRASENA", "cuenta"),
    ("No puedo iniciar sesion", "cuenta"),
])
def test_clasificar_por_categoria(texto, esperada):
    assert clasificar(texto) == esperada


def test_sin_coincidencias_va_a_otro():
    assert clasificar("Hola, solo quería felicitarlos") == "otro"
    assert clasificar("") == "otro"


def test_solo_coincide_al_inicio_de_palabra():
    # "cuenta" no debe encontrarse dentro de "descuenta"
    assert clasificar("me descuentan algo", {"cuenta": ["cuenta"]}) == "otro"


def test_gana_la_categoria_con_mas_coincidencias():
    # "error" (tecnico) contra "pagar" y "cargo" (facturacion)
    assert clasificar("Intenté pagar, dio error y no sé si se hizo el cargo") == "facturacion"


def test_empate_gana_la_primera_categoria():
    reglas = {"a": ["hola"], "b": ["chau"]}
    assert clasificar("hola y chau", reglas) == "a"


def test_procesar_escribe_csv_con_categoria(tmp_path):
    entrada = tmp_path / "input.csv"
    salida = tmp_path / "output.csv"
    entrada.write_text(
        'id,texto\n1,"Me llegó un cobro raro"\n2,"Qué lindo día"\n',
        encoding="utf-8",
    )

    procesar(entrada, salida)

    with open(salida, encoding="utf-8", newline="") as f:
        filas = list(csv.DictReader(f))
    assert filas == [
        {"id": "1", "texto": "Me llegó un cobro raro", "categoria": "facturacion"},
        {"id": "2", "texto": "Qué lindo día", "categoria": "otro"},
    ]


def test_cada_ticket_del_input_recibe_una_categoria_valida(tmp_path):
    validas = {"facturacion", "tecnico", "cuenta", "otro"}
    resultado = procesar("data/input.csv", tmp_path / "output.csv")
    assert len(resultado) == 20
    assert all(t["categoria"] in validas for t in resultado)
