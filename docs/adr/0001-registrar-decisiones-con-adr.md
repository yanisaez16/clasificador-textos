# 0001. Registrar decisiones con ADR

- Estado: Aceptado
- Fecha: 2026-11-17
- Versión: v0.1

## Contexto
El proyecto va a crecer en varias versiones con tecnologías distintas. Sin registro, el motivo
de cada elección se pierde y es difícil explicarlo o retomarlo con un agente de IA que no tiene
la historia.

## Decisión
Cada decisión relevante se documenta como un ADR corto en `docs/adr/` y se enlaza desde el README.

## Alternativas consideradas
- Solo mensajes de commit: no se encuentran fácil y no muestran alternativas descartadas.
- Una wiki aparte: queda desincronizada del código.

## Consecuencias
- Hay que escribir un ADR al tomar decisiones nuevas (incluido en `CLAUDE.md` para que el agente lo proponga).
- El historial de decisiones viaja con el repo y sirve para explicar cada elección más adelante.
