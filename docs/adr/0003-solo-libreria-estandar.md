# 0003. Solo librería estándar en el núcleo

- Estado: Aceptado
- Fecha: 2026-11-17
- Versión: v0.1

## Contexto
El volumen de datos es mínimo y el objetivo de la v0.1 es entender el flujo de punta a punta
y trabajar con agentes, no una herramienta concreta.

## Decisión
El clasificador usa solo la librería estándar (`csv`, `re`, `unicodedata`). La única dependencia
es `pytest` (y `pytest-cov`) para tests.

## Alternativas consideradas
- pandas: cómodo, pero agrega una dependencia pesada para 20 filas.

## Consecuencias
- Instalación inmediata y CI rápida.
- Cuando el volumen o el tema lo justifiquen, se agregan herramientas nuevas con su propio ADR,
  sin cambiar el núcleo.
