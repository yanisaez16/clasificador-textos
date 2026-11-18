# Architecture Decision Records

Cada decisión que cueste revertir o que alguien pueda preguntar "¿por qué así?" se registra aquí.
Los ADR no se editan una vez aceptados: si cambia la decisión, se crea uno nuevo que la reemplaza.

| # | Título | Estado | Versión |
|---|---|---|---|
| [0001](0001-registrar-decisiones-con-adr.md) | Registrar decisiones con ADR | Aceptado | v0.1 |
| [0002](0002-clasificacion-por-palabras-clave.md) | Clasificación por palabras clave | Aceptado | v0.1 |
| [0003](0003-solo-libreria-estandar.md) | Solo librería estándar en el núcleo | Aceptado | v0.1 |

## Plantilla

Copiar como `NNNN-titulo-corto.md`:

```markdown
# NNNN. Título

- Estado: Propuesto | Aceptado | Reemplazado por NNNN
- Fecha: AAAA-MM-DD
- Versión: v0.X

## Contexto
Qué problema hay y qué restricciones aplican.

## Decisión
Qué se eligió.

## Alternativas consideradas
Qué otras opciones había y por qué no.

## Consecuencias
Qué se gana, qué se pierde y qué habrá que revisar más adelante.
```
