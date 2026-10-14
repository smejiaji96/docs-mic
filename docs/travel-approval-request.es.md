# SDD · Travel Approval Request

## Resumen
Cualquiera con el enlace puede responder; se llena cuando ocurre el evento. Tareas por hacer: 1.

## 1. Principios del proyecto

**Punto de partida**
- Vulnerabilidad (Medio): Enlace público: cualquiera que lo tenga puede abrirlo y responder; recopila nombre y número de empleado
- Estabilidad (Medio): Lo recibe y lo actualiza el administrador; destino de las respuestas por confirmar

| # | Principio | Estado | Cómo está esta herramienta |
|---|---|---|---|
| 1 | Entrar con la cuenta de la empresa | Por hacer | Cualquiera con el enlace puede responder, sin cuenta. |
| 2 | Datos en un lugar de la empresa | Por hacer | Falta definir dónde se guardan las respuestas y por cuánto tiempo. |
| 3 | Información al día | No aplica | Se llena cuando ocurre el evento; no se actualiza por programación. |
| 4 | Responsables — Dueño | Cumplido | Dueño: su creador, ya registrado. |
| 4 | Responsables — Suplente | Por hacer | Suplente: falta anotarlo en la ficha. |
| 5 | Documentar y cambiar con orden | Parcial | Tiene su ficha de documentación; quedan 4 pendientes por cerrar. |

## 2. Qué se necesita

### Necesidades de las personas

- **US-003A** (Cumplido): Que tenga su dueño registrado — Su dueño es su administrador, ya registrado.
- **US-003B** (Por hacer): Que tenga un suplente registrado — Falta anotar el suplente en la ficha.
- **US-005** (Por hacer): Que solo responda gente de la empresa y se sepa dónde van las respuestas — Falta limitar quién responde y definir el destino de las respuestas.

### Lo que debe cumplir

| ID | Requisito | Estado |
|---|---|---|
| FR-010 | Cada herramienta DEBE tener un suplente registrado, que sea una persona. | Por hacer |
| FR-011 | El sistema DEBE mantener la documentación de las 7 áreas por herramienta. | Parcial |
| FR-015 | El sistema DEBE limitar quién puede responder cada formulario a personas con una cuenta de la empresa. | Por hacer |
| FR-016 | El sistema DEBE definir el destino y el tiempo de guardado de las respuestas de cada formulario. | Por hacer |

### Cómo sabremos que funcionó

| ID | Criterio | Cómo medirlo aquí | Estado |
|---|---|---|---|
| SC-003 | El 100 % de las 17 herramientas tiene un suplente registrado en 30 días (el dueño, su creador, ya está registrado). | Su ficha muestra el suplente. | Por hacer |
| SC-006 | Las líneas pendientes de la documentación bajan de 32 a menos de 10. | Los pendientes de su ficha bajan a cero o casi (hoy 4). | Parcial |

## 3. Preguntas y respuestas

### Ya respondidas

| Pregunta | Respuesta |
|---|---|
| ¿Qué enlaces piden inicio de sesión hoy? | Ningún dashboard (salvo Costo de servir, por el Portal) ni formulario: cualquiera que tenga el enlace puede abrirlos. Las bases de datos en Excel, en SharePoint, exigen una cuenta de la empresa y permiso. |
| ¿Quién recibe las respuestas de cada formulario? | Su administrador, que también lo actualiza. |
| ¿Deben iniciar sesión las personas que responden los formularios? | Hoy no; quienes los llenan deberían tener correo de la empresa, por verificar. |

### Por responder

- Verificar que quienes lo llenan tengan correo de la empresa (Falcon Farms); deberían tenerlo.
- Dónde se guardan las respuestas (Excel, SharePoint o Power Automate); las recibe el administrador.
- Dueño del formulario y licencia.
- Retención de las respuestas y quién puede descargarlas.

## 4. Plan: cómo se hace

### Decisiones sobre herramientas

| Tema | Qué se elige | Por qué |
|---|---|---|
| Formularios | Formularios a nombre de un grupo, solo para personas de la empresa, con las respuestas guardadas en un lugar de la empresa | El formulario no depende de una persona y las respuestas tienen destino y tiempo de guardado definidos. |

### Fases que le tocan

- Fase 5: Formularios controlados
- Fase 3: Dueño y suplente por herramienta
- Fase final: Cierre

### Riesgos y cómo evitarlos

| Riesgo | Cómo evitarlo |
|---|---|
| Quienes responden los formularios deberán iniciar sesión por primera vez | Avisar antes, probar con pocas personas y mantener el mismo enlace. |

## 5. Tareas

- [ ] T-006: Limitar «Travel Approval Request» a cuentas de la empresa y definir dónde se guardan sus respuestas (Por hacer · Primero)
  - Se entrega cuando: Una cuenta externa no puede responder y el formulario tiene destino de respuestas.

## 6. Plan de acción

| # | Qué se hace | Quién | Cuándo |
|---|---|---|---|
| 1 | Cargar las tareas de «Travel Approval Request» (T-006) en la lista de trabajo | Responsable del inventario | Primer día |
| 2 | Hacer primero las más importantes: T-006 | Dueño de la herramienta (su creador), con su suplente | Primera semana |
| 3 | Probar el resultado: intentar responder desde una cuenta que no sea de la empresa | Dueño de la herramienta | Primera semana |
| 4 | Anotar el suplente en la ficha y cerrar los 4 pendientes de documentación | Dueño de la herramienta | Primeras dos semanas |
| 5 | Cada semana, marcar el avance en la lista de trabajo | Responsable del inventario | Cada semana |
