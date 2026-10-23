# SDD · FIT

## Resumen
Pide cuenta y aprobación de un Admin; se actualiza en vivo. Tareas por hacer: 7.

## 1. Principios del proyecto

**Punto de partida**
- Vulnerabilidad (Medio): Pide cuenta y aprobación de un Admin y la sesión expira sola, pero los reportes de texto libre nombran a empleados de tiendas y el Admin ve correos completos; faltan las reglas de acceso de la base de datos por confirmar
- Estabilidad (Medio): Su creador es también su administrador, sin suplente; depende de Vercel, Supabase, el correo y un asistente de IA; respaldo por confirmar
- Escalabilidad (Bajo): Unas 2.551 tiendas y 106 casos históricos: volumen bajo hoy; faltan los límites de los planes por confirmar

| # | Principio | Estado | Cómo está esta herramienta |
|---|---|---|---|
| 1 | Entrar con la cuenta de la empresa | Parcial | Pide correo y contraseña y la aprobación de un Admin; falta confirmar que el registro exige correo de la empresa. |
| 2 | Datos en un lugar de la empresa | Por confirmar | Los datos viven en Supabase y la aplicación en Vercel; falta confirmar quién es el dueño de esas cuentas y que sean de la empresa. |
| 3 | Información al día | Cumplido | Se actualiza en vivo («Live from FIT») y el Dashboard muestra los casos al instante. |
| 4 | Responsables — Dueño | Cumplido | Dueño: su creador, ya registrado. |
| 4 | Responsables — Suplente | Por hacer | Suplente: falta anotarlo en la ficha; hoy su creador también es su administrador. |
| 5 | Documentar y cambiar con orden | Parcial | Tiene su ficha de documentación; quedan 14 pendientes por cerrar. |

## 2. Qué se necesita

### Necesidades de las personas

- **US-001** (Parcial): Que solo entre quien tiene cuenta de la empresa — Pide cuenta y aprobación de un Admin; falta confirmar el correo de la empresa.
- **US-002A** (Cumplido): Que se actualice solo y se vea cuándo — Se actualiza en vivo.
- **US-002B** (Por confirmar): Que se confirme si falla y se avise — Falta confirmar si hay un aviso cuando falla la base de datos o el correo.
- **US-003A** (Cumplido): Que tenga su dueño registrado — Su dueño es su creador, ya registrado.
- **US-003B** (Por hacer): Que tenga un suplente registrado — Falta anotar el suplente en la ficha.
- **US-F1** (Por hacer): Que las personas que reportan o aparecen en los reportes tengan sus datos protegidos — Los textos libres nombran a empleados de tiendas y el Admin ve correos completos: falta definir qué se escribe, quién lo ve y cuánto se guarda.
- **US-F2** (Por hacer): Que los casos y las fotos no se pierdan si algo falla — Falta confirmar el respaldo de la base de datos y de los adjuntos, y quién es dueño de las cuentas de Supabase y Vercel.

### Lo que debe cumplir

| ID | Requisito | Estado |
|---|---|---|
| FIT-FR-1 | El registro de cuentas exige correo de la empresa. | Por confirmar |
| FIT-FR-2 | Las reglas de acceso por fila de la base de datos están activas y revisadas. | Por confirmar |
| FIT-FR-3 | Solo los roles que lo necesitan ven los correos completos de usuarios y contactos. | Por hacer |
| FIT-FR-4 | Los reportes de texto libre no incluyen nombres de empleados, y se define cuánto tiempo se guardan. | Por hacer |
| FIT-FR-5 | La base de datos y los adjuntos tienen respaldo, con una fecha de retención definida. | Por hacer |
| FIT-FR-6 | Las cuentas de Vercel y Supabase son de la empresa y hay un segundo administrador. | Por hacer |
| FR-010 | Cada herramienta DEBE tener un suplente registrado, que sea una persona. | Por hacer |
| FR-011 | El sistema DEBE mantener la documentación de las 7 áreas por herramienta. | Parcial |

### Cómo sabremos que funcionó

| ID | Criterio | Cómo medirlo aquí | Estado |
|---|---|---|---|
| FIT-SC-1 | Un correo que no es de la empresa no puede activar una cuenta. | Intentar registrarse con un correo que no es de la empresa: debe rechazarse. | Por confirmar |
| FIT-SC-2 | Después de una falla se puede recuperar la información de los casos y sus adjuntos. | Restaurar el respaldo en una prueba y abrir un caso con sus adjuntos. | Por hacer |
| FIT-SC-3 | Los reportes nuevos no incluyen nombres de empleados. | Revisar una muestra de los reportes de un mes. | Por hacer |
| SC-003 | FIT tiene un suplente registrado en 30 días. | Su ficha muestra el suplente. | Por hacer |
| SC-006 | Las líneas pendientes de la ficha de FIT bajan de 14 a menos de 5. | Los pendientes de su ficha bajan a cero o casi (hoy 14). | Parcial |

## 3. Preguntas y respuestas

### Ya respondidas

| Pregunta | Respuesta |
|---|---|
| ¿Cómo se entra a FIT? | Con correo y contraseña. Toda cuenta nueva queda pendiente hasta que un Admin la aprueba y le asigna un rol; la sesión se cierra sola tras 10 minutos sin actividad. |
| ¿Qué datos guarda? | Casos con texto libre, categoría, motivo, estado, fechas y metas; fotos y adjuntos; tiendas por cliente con su cadena de gerentes; usuarios con su rol; contactos y reglas de correo. |
| ¿Dónde está alojada y dónde guarda los datos? | La aplicación está en Vercel; las cuentas, los casos y las reglas están en Supabase, y se actualiza en vivo. |
| ¿Se pueden exportar los datos? | No se vio ningún botón de exportación; solo hay importación (tiendas en Excel o CSV y un catálogo inicial). |
| ¿Qué hace el asistente de IA? | Ayuda a clasificar los reportes; su nombre por defecto es «FITTI». |

### Por responder

- Verificar si el registro exige correo de la empresa (Falcon Farms) o acepta cualquier correo.
- Cuántas cuentas hay aprobadas por rol y quién aprueba las nuevas.
- Quién es el dueño de la cuenta de Supabase, y en qué plan y región está.
- Respaldo de la base de datos y de los adjuntos, y cuánto tiempo se conservan los casos.
- De dónde sale el Excel de tiendas y quién lo mantiene.
- Qué proveedor de IA usa el asistente, qué datos del reporte le envía y si una persona valida su clasificación.
- Dueño de las cuentas de Vercel y del repositorio del código, y plan contratado.
- Si la empresa tendrá un dominio propio; hoy es un subdominio de vercel.app.
- Cada cuánto se publican versiones nuevas y quién las publica.
- Si la base de datos tiene reglas de acceso por fila (RLS) activas y revisadas.
- Quién ve las fotos y adjuntos y dónde se guardan.
- Política de retención y borrado de los casos con datos de personas.
- Plan de recuperación si falla Supabase, Vercel o el correo.
- Volumen esperado de casos y adjuntos, y los límites de los planes de Supabase y Vercel.

## 4. Plan: cómo se hace

### Decisiones sobre herramientas

| Tema | Qué se elige | Por qué |
|---|---|---|
| FIT se analiza aparte | Con la misma estructura que las demás herramientas, pero fuera del análisis general de las 17. | Es una aplicación con su propia base de datos; el análisis general se limita a dashboards, formularios y bases en Excel. |
| Datos personales primero | Revisar primero el texto libre de los reportes y los correos que ve el Admin. | Es lo que más expone a las personas. |

### Fases que le tocan

- Fase 1: Acceso seguro a los dashboards
- Fase 2: Actualización confiable y visible
- Fase 3: Dueño y suplente por herramienta
- Fase final: Cierre

### Riesgos y cómo evitarlos

| Riesgo | Cómo evitarlo |
|---|---|
| Los reportes de texto libre nombran a empleados de tiendas y describen situaciones con ellos. | Pedir que no se escriban nombres, definir cuánto tiempo se guardan y quién los ve. |
| Una sola persona crea y administra FIT, y las cuentas de Vercel y Supabase pueden depender de ella. | Anotar el suplente y pasar las cuentas a la empresa con un segundo administrador. |
| Sin un respaldo confirmado, una falla de Supabase podría perder casos y fotos. | Confirmar el respaldo y probar una restauración. |
| El registro puede aceptar correos que no son de la empresa. | Exigir correo de la empresa y mantener la aprobación del Admin. |
| Es un prototipo que ya se usa: un cambio puede afectar el trabajo diario. | Probar los cambios antes de publicarlos y anotar quién los publica. |

## 5. Tareas

- [ ] FIT-T1: Revisar por privacidad el texto libre de los reportes de FIT, pedir que no incluyan nombres de empleados y definir cuánto tiempo se guardan (Por hacer · Primero)
  - Se entrega cuando: Hay una regla escrita sobre qué se escribe en los reportes y por cuánto tiempo se guardan.
- [ ] FIT-T2: Confirmar quién es dueño de las cuentas de Vercel y Supabase, pasarlas a la empresa y registrar un segundo administrador (Por hacer · Primero)
  - Se entrega cuando: Las cuentas son de la empresa y hay dos administradores.
- [ ] FIT-T3: Confirmar el respaldo de la base de datos y de los adjuntos, y probar una restauración (Por hacer · Primero)
  - Se entrega cuando: Hay un respaldo con fecha y una restauración de prueba exitosa.
- [ ] FIT-T4: Exigir correo de la empresa en el registro y revisar las reglas de acceso de la base de datos (Por hacer · Después)
  - Se entrega cuando: Un correo que no es de la empresa no puede activar una cuenta y las reglas de acceso están revisadas.
- [ ] FIT-T5: Limitar quién ve los correos completos de usuarios y contactos (Por hacer · Después)
  - Se entrega cuando: Solo los roles que lo necesitan ven los correos completos.
- [ ] FIT-T6: Confirmar qué proveedor usa el asistente de IA y qué datos del reporte le envía (Por hacer · Después)
  - Se entrega cuando: Está anotado el proveedor y qué datos se le envían.
- [ ] FIT-T7: Anotar el suplente de FIT en la ficha y cerrar los pendientes de documentación (Por hacer · Al final)
  - Se entrega cuando: La ficha muestra el suplente y sus pendientes bajan a cero o casi.

## 6. Plan de acción

| # | Qué se hace | Quién | Cuándo |
|---|---|---|---|
| 1 | Cargar las tareas de «FIT» (FIT-T1, FIT-T2, FIT-T3, FIT-T4, FIT-T5, FIT-T6, FIT-T7) en la lista de trabajo | Responsable del inventario | Primer día |
| 2 | Hacer primero las más importantes: FIT-T1, FIT-T2, FIT-T3 | Dueño de la herramienta (su creador), con su suplente | Primera semana |
| 3 | Probar el resultado: abrir un correo que no es de la empresa en el registro y probar una restauración del respaldo | Dueño de la herramienta | Primeras dos semanas |
| 4 | Anotar el suplente en la ficha y cerrar los 14 pendientes de documentación | Dueño de la herramienta | Primeras dos semanas |
| 5 | Cada semana, marcar el avance en la lista de trabajo | Responsable del inventario | Cada semana |
