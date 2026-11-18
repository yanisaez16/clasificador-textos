---
name: comparar-clasificacion
description: Clasifica los tickets de data/input.csv con criterio propio y los compara con el resultado del script de palabras clave. Usar cuando pidan comparar, revisar o mejorar la clasificación.
---

# Clasificar con criterio y comparar con el script

## Pasos

1. Lee `data/input.csv` y las categorías definidas en `CLAUDE.md`.
2. Clasifica cada ticket tú mismo, entendiendo la intención del cliente (no por palabras sueltas).
   Si un ticket es ambiguo, elige la categoría según qué equipo tendría que resolverlo.
3. Escribe `data/output_ia.csv` con columnas: `id`, `categoria`, `motivo` (máximo 10 palabras).
4. Si `data/output.csv` no existe, ejecuta `python main.py` para generarlo.
5. Compara ambos archivos y muestra:
   - Porcentaje de coincidencia
   - Tabla solo con los tickets donde difieren: `id`, texto resumido, script, Claude, motivo
6. Para cada diferencia, sugiere qué palabra clave agregar, quitar o mover en `reglas.py` para que el script acierte.

## Reglas
- NO modifiques `reglas.py` ni `main.py`: solo sugiere. Pregunta antes de aplicar cambios.
- Si aplicas cambios aprobados, corre `python -m pytest -q` y vuelve a comparar.
