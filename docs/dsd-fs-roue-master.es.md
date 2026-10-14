# SDD · DSD FS ROUE MASTER

## Resumen
Pide cuenta de la empresa y permiso; se actualiza según la necesidad. Tareas por hacer: 1.

## 1. Principios del proyecto

**Punto de partida**
- Vulnerabilidad (Medio): Contiene costos, presupuesto y datos de viaje por supervisor; requiere cuenta de la empresa y permiso; falta revisar la lista de permisos
- Estabilidad (Medio): Copia de la maestra de tiendas y versión anterior oculta
- Escalabilidad (Bajo): Unas 4.177 filas en 11 hojas

| # | Principio | Estado | Cómo está esta herramienta |
|---|---|---|---|
| 1 | Entrar con la cuenta de la empresa | Cumplido | Pide cuenta de la empresa y permiso. |
| 2 | Datos en un lugar de la empresa | Parcial | Está en un sitio de equipo; falta revisar los permisos y retirar la copia de la maestra de tiendas. |
| 3 | Información al día | Por hacer | Se actualiza según la necesidad; falta anotar quién la actualiza y cuándo. |
| 4 | Responsables — Dueño | Cumplido | Dueño: su creador, ya registrado. |
| 4 | Responsables — Suplente | Por hacer | Suplente: falta anotarlo en la ficha. |
| 5 | Documentar y cambiar con orden | Parcial | Tiene su ficha de documentación; quedan 3 pendientes por cerrar. |

## 2. Qué se necesita

### Necesidades de las personas

- **US-003A** (Cumplido): Que tenga su dueño registrado — Su dueño es su creador, ya registrado.
- **US-003B** (Por hacer): Que tenga un suplente registrado — Falta anotar el suplente en la ficha.
- **US-004** (Por hacer): Que los datos estén en un lugar seguro y ordenado — Falta pasarla a un servidor, anotar quién la actualiza y revisar permisos.

### Lo que debe cumplir

| ID | Requisito | Estado |
|---|---|---|
| FR-010 | Cada herramienta DEBE tener un suplente registrado, que sea una persona. | Por hacer |
| FR-011 | El sistema DEBE mantener la documentación de las 7 áreas por herramienta. | Parcial |
| FR-013 | El sistema DEBE mantener cada base de datos maestra en un lugar controlado por la empresa, nunca en una cuenta personal, con permisos revisados. Se sugiere pasarlas a un servidor, por seguridad. Se sugiere pasarla a un servidor. | Parcial |
| FR-014 | El sistema DEBERÍA mantener una sola lista maestra de tiendas y retirar las copias. | Por hacer |

### Cómo sabremos que funcionó

| ID | Criterio | Cómo medirlo aquí | Estado |
|---|---|---|---|
| SC-003 | El 100 % de las 17 herramientas tiene un suplente registrado en 30 días (el dueño, su creador, ya está registrado). | Su ficha muestra el suplente. | Por hacer |
| SC-004 | Ningún archivo maestro permanece en una cuenta personal. | El archivo está en un lugar de la empresa, no en una cuenta personal. | Parcial |
| SC-006 | Las líneas pendientes de la documentación bajan de 32 a menos de 10. | Los pendientes de su ficha bajan a cero o casi (hoy 3). | Parcial |

## 3. Preguntas y respuestas

### Ya respondidas

| Pregunta | Respuesta |
|---|---|
| ¿Qué enlaces piden inicio de sesión hoy? | Ningún dashboard (salvo Costo de servir, por el Portal) ni formulario: cualquiera que tenga el enlace puede abrirlos. Las bases de datos en Excel, en SharePoint, exigen una cuenta de la empresa y permiso. |
| ¿Con qué frecuencia se actualizan los archivos de Excel? | Según la necesidad. |
| ¿Las bases de datos de Excel podrían migrarse a un servidor? | Sí, como sugerencia por seguridad. |

### Por responder

- Lista de personas con acceso al archivo y su permiso (lectura o edición).
- Si se alimenta de otros sistemas o se captura a mano.
- Permisos y control de versiones.

## 4. Plan: cómo se hace

### Decisiones sobre herramientas

| Tema | Qué se elige | Por qué |
|---|---|---|
| Bases de datos maestras | Pasar las 4 bases de datos de Excel a un servidor (sugerido), con una sola lista maestra de tiendas | Mejora la seguridad frente a los archivos de Excel y evita cifras distintas entre reportes. |

### Fases que le tocan

- Fase 4: Bases de datos ordenadas
- Fase 3: Dueño y suplente por herramienta
- Fase final: Cierre

### Riesgos y cómo evitarlos

| Riesgo | Cómo evitarlo |
|---|---|
| Pasar las bases de Excel a un servidor interrumpe a quien las usa hoy | Pasar una base a la vez, avisar antes y conservar el archivo original hasta validar el resultado. |

## 5. Tareas

- [ ] T-005: Pasar «DSD FS ROUE MASTER» al servidor usando la maestra única (y retirando la copia), revisar permisos y anotar quién la actualiza y cuándo (Por hacer · Después)
  - Se entrega cuando: Está en el servidor, muestra su última actualización y quién tiene acceso, y no queda nada en cuentas personales.

## 6. Plan de acción

| # | Qué se hace | Quién | Cuándo |
|---|---|---|---|
| 1 | Cargar las tareas de «DSD FS ROUE MASTER» (T-005) en la lista de trabajo | Responsable del inventario | Primer día |
| 2 | Hacer primero las más importantes: T-005 | Dueño de la herramienta (su creador), con su suplente | Primera semana |
| 3 | Probar el resultado: confirmar quién tiene acceso y que no quede nada en cuentas personales | Dueño de la herramienta | Primera semana |
| 4 | Anotar el suplente en la ficha y cerrar los 3 pendientes de documentación | Dueño de la herramienta | Primeras dos semanas |
| 5 | Cada semana, marcar el avance en la lista de trabajo | Responsable del inventario | Cada semana |
