# 0002. Clasificación por palabras clave

- Estado: Aceptado
- Fecha: 2026-11-17
- Versión: v0.1

## Contexto
Hay que asignar cada ticket a una de cuatro categorías. Los datos son 20 tickets sintéticos,
sin etiquetas históricas para entrenar, y el proyecto no usa APIs pagas.

## Decisión
Clasificar contando coincidencias de raíces de palabras definidas en `reglas.py`, ignorando
mayúsculas y tildes. Gana la categoría con más coincidencias; empate, la primera del diccionario;
sin coincidencias, `otro`. Los casos ambiguos se resuelven con reglas escritas en `CLAUDE.md`.

## Alternativas consideradas
- Modelo de ML (por ejemplo TF-IDF + regresión logística): no hay datos etiquetados suficientes.
- LLM vía API: tiene costo y es menos predecible.

## Consecuencias
- Resultado explicable y reproducible; 20/20 coincidencias con la clasificación de referencia.
- No escala bien a textos nuevos con vocabulario distinto: las reglas hay que mantenerlas a mano.
- La salida de este clasificador sirve como línea base para comparar otros enfoques más adelante.
