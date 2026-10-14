# SDD · Costo de servir

## Resumen
Se entra solo por el Portal (solo quienes tienen acceso al Portal); se actualiza por programación (última: 7 de octubre). Tareas por hacer: 2.

## 1. Principios del proyecto

**Punto de partida**
- Vulnerabilidad (Bajo): Se entra solo por el Portal; solo pueden entrar quienes tienen acceso al Portal (según la responsable)
- Estabilidad (Bajo): Actualización programada; última: 7 de octubre de 2026 (según el reporte activo en el Portal)
- Escalabilidad (Bajo): Modelo de 12 MB (según el enlace público anterior)

| # | Principio | Estado | Cómo está esta herramienta |
|---|---|---|---|
| 1 | Entrar con la cuenta de la empresa | Cumplido | Se entra solo por el Portal; solo pueden entrar quienes tienen acceso al Portal. |
| 2 | Datos en un lugar de la empresa | No aplica | Los datos viven en sus fuentes; este dashboard solo los muestra. |
| 3 | Información al día | Parcial | Se actualiza solo (última: 7 de octubre); falta activar el aviso de fallas. |
| 4 | Responsables — Dueño | Cumplido | Dueño: su creador, ya registrado. |
| 4 | Responsables — Suplente | Por hacer | Suplente: falta anotarlo en la ficha. |
| 5 | Documentar y cambiar con orden | Parcial | Tiene su ficha de documentación; queda 1 pendiente por cerrar. |

## 2. Qué se necesita

### Necesidades de las personas

- **US-001** (Cumplido): Que solo entre quien tiene cuenta de la empresa — Ya se entra solo por el Portal.
- **US-002A** (Cumplido): Que se actualice solo y se vea cuándo — Se actualiza solo y muestra su fecha.
- **US-002B** (Por confirmar): Que se confirme si falla y se avise — Falta confirmar si falla y activar el aviso al dueño y al suplente.
- **US-003A** (Cumplido): Que tenga su dueño registrado — Su dueño es su creador, ya registrado.
- **US-003B** (Por hacer): Que tenga un suplente registrado — Falta anotar el suplente en la ficha.

### Lo que debe cumplir

| ID | Requisito | Estado |
|---|---|---|
| FR-001 | El sistema DEBE exigir entrar con una cuenta de la empresa (correo Falcon Farms) para ver cualquier reporte con datos del personal o de la operación; no se crean grupos por rol. | Cumplido |
| FR-002 | El sistema DEBE unificar en un solo sitio los enlaces de las herramientas y retirar los enlaces públicos directos; ningún dashboard queda público por diseño. | Cumplido |
| FR-005 | El sistema DEBERÍA eliminar las páginas duplicadas u ocultas que no tengan un propósito documentado. Eliminar o documentar 1 página oculta. | Por hacer |
| FR-006 | El sistema DEBE actualizar cada reporte por programación definida. | Cumplido |
| FR-007 | El sistema DEBE mostrar en cada reporte la fecha y hora de su última actualización. | Cumplido |
| FR-008 | El sistema DEBE avisar al dueño y a su suplente cuando una actualización falle. Falta confirmar si falla y activar el aviso. | Por confirmar |
| FR-010 | Cada herramienta DEBE tener un suplente registrado, que sea una persona. | Por hacer |
| FR-011 | El sistema DEBE mantener la documentación de las 7 áreas por herramienta. | Parcial |

### Cómo sabremos que funcionó

| ID | Criterio | Cómo medirlo aquí | Estado |
|---|---|---|---|
| SC-001 | El 100 % de los reportes con información sensible exigen inicio de sesión; ninguno se abre solo con un enlace, salvo excepciones aprobadas. | Abrir «Costo de servir» en una ventana privada: debe pedir cuenta. | Cumplido |
| SC-002 | El 100 % de los reportes se actualiza por programación y muestra la fecha y hora de su última actualización. | Su última actualización coincide con la programación y se ve la fecha y hora. | Cumplido |
| SC-005 | Una actualización fallida se detecta por su dueño en menos de 1 día hábil. | Una falla de prueba avisa al dueño y al suplente. | Por confirmar |
| SC-003 | El 100 % de las 17 herramientas tiene un suplente registrado en 30 días (el dueño, su creador, ya está registrado). | Su ficha muestra el suplente. | Por hacer |
| SC-006 | Las líneas pendientes de la documentación bajan de 32 a menos de 10. | Los pendientes de su ficha bajan a cero o casi (hoy 1). | Parcial |

## 3. Preguntas y respuestas

### Ya respondidas

| Pregunta | Respuesta |
|---|---|
| ¿Cómo se accede a Costo de servir? | Solo se entra por el Portal, y solo pueden entrar quienes tienen acceso a ese Portal. |
| ¿Qué enlaces piden inicio de sesión hoy? | Ningún dashboard (salvo Costo de servir, por el Portal) ni formulario: cualquiera que tenga el enlace puede abrirlos. Las bases de datos en Excel, en SharePoint, exigen una cuenta de la empresa y permiso. |
| ¿Quién es el dueño de cada reporte? | Su creador. |
| ¿Qué reportes se actualizan por programación? | Todos, excepto Performance Audit Walmart y Sprouts Execution Report, que se actualizan a mano. |
| ¿Hay algún dashboard que deba seguir siendo público de forma deliberada? | No necesariamente públicos; lo que se necesita es que las personas con correo de la empresa tengan acceso. |

### Por responder

- Verificar que quienes lo usan tengan correo de la empresa (Falcon Farms); deberían tenerlo.

## 4. Plan: cómo se hace

### Decisiones sobre herramientas

| Tema | Qué se elige | Por qué |
|---|---|---|
| Acceso desde un solo sitio | Entrar con la cuenta de la empresa (Microsoft) desde un solo sitio de entrada, por ejemplo el Portal, abierto a toda la organización | Quienes usan las herramientas deberían tener cuenta de la empresa y sus roles ya están en cada ficha; no hace falta crear grupos por rol. Costo de servir ya se usa por el Portal, y unificar evita enlaces sueltos. |
| Enlaces públicos | Retirar los enlaces públicos que existen; publicar en la web queda limitado a quienes tienen Power BI Pro | Quienes tienen acceso pueden publicar y retirar enlaces por su cuenta; los enlaces que existen siguen abiertos a cualquiera hasta que se retiren (fuentes de terceros consultadas). |
| Actualización | Actualización programada en Power BI, con aviso al dueño y a su suplente si falla | Quita la actualización a mano y avisa de las fallas. Varios reportes ya tienen una tabla «Last Refresh» que se reutiliza. |

### Fases que le tocan

- Fase 1: Acceso seguro a los dashboards
- Fase 2: Actualización confiable y visible
- Fase 3: Dueño y suplente por herramienta
- Fase final: Cierre

### Riesgos y cómo evitarlos

| Riesgo | Cómo evitarlo |
|---|---|
| Visitantes que aún no tienen o no usan una cuenta de la empresa | Verificar la lista de usuarios de cada dashboard (los roles ya están en cada ficha) antes de retirar los enlaces; quien no tenga correo de la empresa se resuelve antes. |
| Quitar el enlace público interrumpe a quien lo usa | Avisar antes, validar el acceso nuevo y retirar el enlace al final, un dashboard a la vez. |

## 5. Tareas

- [ ] T-001: «Costo de servir» ya se entra solo por el Portal, que sirve de modelo del sitio único (Cumplido · Primero)
  - Se entrega cuando: Abre solo con cuenta, desde un solo sitio.
- [ ] T-002: Limpiar «Costo de servir»: eliminar o documentar 1 página oculta (Por hacer · Después)
  - Se entrega cuando: No quedan comentarios libres ni páginas ocultas sin explicación.
- [ ] T-004: Confirmar si «Costo de servir» ha fallado y activar el aviso de fallas al dueño y al suplente (Por hacer · Después)
  - Se entrega cuando: Se sabe si ha fallado y una falla de prueba avisa a ambos.

## 6. Plan de acción

| # | Qué se hace | Quién | Cuándo |
|---|---|---|---|
| 1 | Cargar las tareas de «Costo de servir» (T-001, T-002, T-004) en la lista de trabajo | Responsable del inventario | Primer día |
| 2 | Hacer primero las más importantes: T-002, T-004 | Dueño de la herramienta (su creador), con su suplente | Primera semana |
| 3 | Probar el resultado: confirmar que solo entran quienes tienen acceso al Portal | Dueño de la herramienta | Primera semana |
| 4 | Anotar el suplente en la ficha y cerrar el pendiente de documentación | Dueño de la herramienta | Primeras dos semanas |
| 5 | Cada semana, marcar el avance en la lista de trabajo | Responsable del inventario | Cada semana |
