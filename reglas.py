"""Palabras clave por categoría.

Cada palabra se busca al inicio de una palabra del texto, así que sirve
como raíz: "cobr" encuentra "cobro", "cobrar" y "cobraron".
Mayúsculas y tildes no importan.

Si un ticket coincide con varias categorías, gana la que tenga más
coincidencias; en caso de empate, la que aparece primero aquí.
"""

REGLAS = {
    "facturacion": [
        "factura",
        "cobr",
        "cargo",
        "pagar",
        "pago",
        "tarjeta",
        "reembolso",
        "devuelvan",
        "transferencia",
        "monto",
        "plan",
        "suscripci",
    ],
    "tecnico": [
        "error",
        "falla",
        "no funciona",
        "no hace nada",
        "se cierra",
        "lento",
        "tarda",
        "botón",
        "exportar",
        "notificaci",
        "configur",
        "funcion",
        "sigo viendo",
        "después de pagar",
    ],
    "cuenta": [
        "cuenta",
        "contraseña",
        "iniciar sesión",
        "recuperación",
        "correo",
        "bloquead",
        "acceso",
        "verificación",
        "cancelar",
        "eliminar",
    ],
}
