import csv
import re
import unicodedata

from reglas import REGLAS

ENTRADA = "data/input.csv"
SALIDA = "data/output.csv"
CATEGORIA_POR_DEFECTO = "otro"


def normalizar(texto):
    """Pasa a minúsculas y quita las tildes (la ñ queda como n)."""
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def contar_coincidencias(texto, palabras):
    """Cuenta cuántas palabras clave aparecen al inicio de una palabra del texto."""
    return sum(
        1 for palabra in palabras
        if re.search(r"\b" + re.escape(normalizar(palabra)), texto)
    )


def clasificar(texto, reglas=REGLAS):
    """Devuelve la categoría con más coincidencias, u 'otro' si no hay ninguna."""
    texto = normalizar(texto)
    mejor, mejor_cuenta = CATEGORIA_POR_DEFECTO, 0
    for categoria, palabras in reglas.items():
        cuenta = contar_coincidencias(texto, palabras)
        if cuenta > mejor_cuenta:
            mejor, mejor_cuenta = categoria, cuenta
    return mejor


def leer_tickets(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def escribir_resultado(ruta, tickets):
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=["id", "texto", "categoria"])
        escritor.writeheader()
        escritor.writerows(tickets)


def procesar(entrada, salida):
    tickets = leer_tickets(entrada)
    resultado = [
        {"id": t["id"], "texto": t["texto"], "categoria": clasificar(t["texto"])}
        for t in tickets
    ]
    escribir_resultado(salida, resultado)
    return resultado


def main():
    resultado = procesar(ENTRADA, SALIDA)
    print(f"{len(resultado)} tickets clasificados -> {SALIDA}")


if __name__ == "__main__":
    main()
