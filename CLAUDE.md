# clasificador-textos

Script de Python que lee tickets de soporte desde un CSV, los clasifica por palabras clave y guarda el resultado en otro CSV.
Proyecto de aprendizaje: mantenerlo simple. Los datos son sintéticos. No usa ninguna API paga.

## Versiones
Es la semilla de una plataforma de datos de tickets que crece por versiones (tabla en `README.md`).
Cada versión agrega una capa sobre **los mismos tickets**; no se arrancan proyectos aparte.
El detalle de las versiones futuras está en `CLAUDE.local.md` (no se sube al repo): no escribirlo
en archivos versionados.

## Documentación al cerrar trabajo
- Decisión nueva (herramienta, estructura, trade-off) → proponer un ADR en `docs/adr/` con la plantilla de `docs/adr/README.md` y agregarlo al índice y al README
- Al cerrar una versión → actualizar `CHANGELOG.md`, la tabla de versiones del README y el diagrama de arquitectura si cambió
- `docs/learning-log.md`: la sección "Qué aprendí" la escribe la persona, no el agente

## Categorías
`facturacion`, `tecnico`, `cuenta`, `otro`. Cada ticket recibe exactamente una.

## Reglas para casos ambiguos
- Si la duda es sobre el dinero (si se cobró, cuánto, a quién), va a `facturacion`, aunque haya un error técnico (#18, #20)
- Si el pago está confirmado y lo que falla es el producto, va a `tecnico` (#15)
- Cancelar o cambiar el plan es `facturacion`; cancelar o eliminar la cuenta es `cuenta` (#7)
- Las consultas comerciales sin un problema (precios, descuentos, sugerencias) van a `otro` (#10)

## Estructura
- `main.py` — lee el CSV, clasifica cada fila y escribe el resultado
- `reglas.py` — diccionario de palabras clave por categoría (editar aquí, no en main.py)
- `data/input.csv` — columnas: `id`, `texto`
- `data/output.csv` — columnas: `id`, `texto`, `categoria`
- `docs/adr/` — decisiones de arquitectura; `docs/learning-log.md` — aprendizajes semanales
- `.github/workflows/ci.yml` — tests + cobertura en cada push a `main`

## Comandos
- Ejecutar: `python main.py`
- Tests: `python -m pytest -q` (el ejecutable `pytest` no está en el PATH)
- Cobertura: `python -m pytest -q --cov`

## Reglas
- Solo librería estándar de Python (`csv`, no pandas) salvo `pytest` para tests
- La comparación de palabras ignora mayúsculas y tildes
- Si un ticket no coincide con ninguna regla, va a `otro`
- Código simple: funciones cortas, sin clases si no hacen falta
- Antes de terminar una tarea, `python -m pytest -q` debe pasar
