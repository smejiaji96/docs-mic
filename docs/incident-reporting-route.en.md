# Spec · Incident Reporting Route

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m16 (inventario MIC) |
| Tipo | Formulario de Microsoft Forms con flujo de Power Automate, base en SharePoint y dashboard de Execution Team |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Formulario donde FS, DM y RM reportan cada ruta que **no se ejecutó según lo planeado**, con su motivo, la secuencia de tiendas visitadas y una justificación. No es una solicitud de aprobación: es un aviso, y cada respuesta se notifica por correo en el momento. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Respuestas | 832, del 2026-08-03 al 2026-10-20 (≈ 74 por semana) | Dueño |
| Quién reporta | 62 personas: FS 74 % · DM 25 % · RM 1 % | Dueño |
| Tipos de cambio | Day Change 51 % · Order Change 40 % · Split 5 % · Order+Day 4 % | Dueño |
| Motivos | Ausencia temporal 84 % · Contingencia de tienda 16 % · Festivo 0,7 % | Dueño |
| Rutas combinadas | 27 % de las respuestas (varios IDs separados con «-») | Dueño |
| Formulario | 17 secciones y 194 preguntas, con una sección por DM (14) | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Alto ⚠️ C-06 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🔴 **No se puede agregar otro DM:** Microsoft Forms permite 200 preguntas, el formulario tiene 194 y cada sección de DM ocupa 13. [Dueño]
2. 🟠 **El correo del flujo llega incompleto** en algunos casos (rutas *split* sin fechas, paradas faltantes o repetidas) y el email del FS se escribe a mano. [Dueño]
3. 🟠 **Los dos reportes no cuadran:** el dashboard cuenta 736 registros y el análisis de cumplimiento 707; el ID 429 no está en ninguna base. [Dueño]
4. 🟠 **La suplente todavía no tiene accesos** a los 6 componentes (formulario, flujo, agente, carpeta, dashboard y buzón). [Dueño]
5. ⚠️ **El formulario no es público ni pide aprobación**, al contrario de lo que decía el análisis inicial (C-01 y C-02). [Dueño]

**Funciona bien:** la consolidación y la carga son fieles. El consolidado coincide al 100 % con el export y la base coincide campo por campo. [Dueño]

**Contradicciones:** 6 detectadas; 4 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (IRR-A01, IRR-A02, IRR-A03, IRR-A04, IRR-A13, IRR-A17) y la pregunta Q-17. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Dejar registrado, y avisar de inmediato, cada vez que una ruta de supervisión no se ejecuta como estaba planeada, para que Execution Team y la jerarquía sepan qué cambió, por qué y qué tiendas se visitaron, y para medir el cumplimiento de rutas.

- **Problema que resuelve:** sin este registro no se sabe cuándo ni por qué una ruta cambió de día, de orden o se partió en dos días. [Dueño]
- **Qué logra:** una respuesta por evento (`ID`), con tipo de cambio, motivo, fechas, hasta 7 paradas por DM y una justificación, más un correo automático. [Dueño]
- **Éxito:** todo evento reportado llega a la base, el correo sale completo y los dos reportes de cumplimiento muestran la misma cifra (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: el formulario (17 secciones), el flujo de Power Automate «Incident Reporting Process» y su correo, la carga semanal a `Incident Reporting Process Database.xlsx` (`Table1`), la copia `Cleandata` y el agente o script de consolidación.

**No incluye** ❓: el dashboard de Execution Team, el archivo de análisis de cumplimiento de PERFORMANCE, el Route Master y el Store Master, que son dependencias.

**Futuro** [Dueño]: que el mismo flujo agregue cada respuesta a la base (IRR-A06), rediseñar la captura de tiendas (IRR-A07) y validar los IDs contra el Route Master (IRR-A10).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| FS, DM y RM (62 personas) | Reportan cada ruta que no se ejecutó según el plan | 832 respuestas | Dueño |
| Responsable del formulario (el dueño) | Recibe las respuestas, hace la carga semanal y mantiene el formulario y el flujo | Carga semanal | Dueño |
| Execution Team | Ve el dashboard que lee la base | Se refresca a diario | Dueño |
| PERFORMANCE | Usa `Cleandata` para el análisis de cumplimiento de rutas | — | Dueño |
| RM, DM, FS y quien reportó | Reciben el correo «New Route Event» | Cada respuesta | Dueño |
| Buzón `route.request` | Recibe cada aviso | Cada respuesta | Dueño |

**Acceso**

- Se llena con la cuenta corporativa. [Dueño] ⚠️ C-01
- Formulario no anónimo: el dueño ve el nombre y el correo de quien responde. [Inicial]
- La base está en SharePoint › Analizer Routes › EXCEPCIONES DE RUTA, y el dashboard en la carpeta de Teams de Execution Team. [Dueño]
- ❓ Falta la lista de personas con acceso a la base y a las carpetas, y quién la aprueba (Q-18). [Inicial]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño · Inicial]

- Es el propietario del formulario y recibe las respuestas.
- Hace la carga semanal, mantiene el flujo y actualiza el formulario y el correo cuando cambia un DM, un RM o una tienda.
- Aprobó su análisis el 2026-10-20 (v1.4).

## Administrador técnico

**Jeronimo Sanchez**, administra el formulario y el flujo. [Inicial]

- El flujo, sus conexiones (Forms y Outlook), el agente de consolidación y la carga dependen de sus cuentas. [Dueño]
- ❓ Quiénes reciben el buzón `route.request` (Q-13).

## Suplente

**Jennifer Guarin.** [Dueño] Todavía no tiene los accesos para operar la herramienta.

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Formulario | Ser copropietaria | ⬜ Pendiente (IRR-A01) |
| Flujo de Power Automate y sus conexiones | Copropiedad y conexiones propias | ⬜ Pendiente (IRR-A01) |
| Agente de consolidación o script | Poder correrlo | ⬜ Pendiente (IRR-A01) |
| Carpeta de SharePoint | Editar la base | ⬜ Pendiente (IRR-A01) |
| Carpeta de Teams del dashboard | Acceso a la carpeta | ⬜ Pendiente (IRR-A01) |
| Buzón `route.request` | Recibir los avisos | ⬜ Pendiente (IRR-A01) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| Respuestas del formulario | Lo que FS, DM y RM escriben; nombre, email y fechas de envío los pone Forms | Quienes reportan | Dueño |
| Export de Forms (200 columnas) | Se descarga cada semana | Dueño | Dueño |
| Consolidado semanal (29 columnas) | El agente de Claude o `consolidate_incident_report.py` reduce 200 columnas a 29 | Dueño | Dueño |
| `Incident Reporting Process Database.xlsx` (`Table1`) | Base del dashboard; se pegan las filas nuevas | Dueño | Dueño |
| `Cleandata.xlsx` | Copia con IDs corregidos y la columna `Count?`; insumo del análisis de cumplimiento | Dueño y PERFORMANCE | Dueño |
| Catálogos dentro del formulario | RMs, DMs y tiendas por DM | Dueño | Dueño |
| Route Master | De él salen los IDs de ruta, pero se escriben a mano | Equipo del Route Master | Dueño |

**Cómo fluyen los datos** [Dueño]

1. **Captura:** FS o DM llenan el formulario.
2. **Aviso:** el flujo envía el correo «New Route Event» al buzón `route.request`, con copia al RM, DM, FS y a quien reportó.
3. **Carga semanal (manual):** export de Forms → recorte a los IDs nuevos → consolidación a 29 columnas → pegado en `Table1`.
4. **Consumo:** el dashboard de Execution Team lee la base y `Cleandata` alimenta el análisis de cumplimiento.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | Microsoft Forms · Power Automate (conexiones de Forms y Outlook) · buzón `route.request` · SharePoint · carpeta de Teams de Execution Team · agente de Claude o script |
| Archivos | Base `Table1` · `Cleandata` · Route Master |
| Personas | El dueño o su suplente |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| Dashboard de Execution Team | Lee `Table1` y se refresca a diario | Execution Team |
| Análisis de cumplimiento de rutas | Usa `Cleandata` | PERFORMANCE |
| Jerarquía de campo | Recibe el correo de cada evento | RM, DM y FS |

## Procesos operativos

[Dueño] Se llena cada vez que ocurre un evento (≈ 74 por semana) y la base se actualiza **una vez por semana**, a mano. ⚠️ C-04

1. Descargar el export de Forms.
2. **Recortarlo** a los IDs mayores que el último de `Table1` (hoy es 737, así que el próximo lote empieza en **738**). Comprobar que no falte ningún ID.
3. Pasarlo al agente de Claude (o correr `consolidate_incident_report.py`) y revisar sus advertencias.
4. Pegar las filas al final de `Table1`.
5. Si aplica, agregar las mismas filas a `Cleandata` para PERFORMANCE.
6. Al día siguiente, verificar que el dashboard muestre el lote (se refresca a diario).
7. Revisar en Power Automate si hubo ejecuciones fallidas del flujo.

**Cuando cambia un DM, un RM o una tienda:** actualizar el formulario (listas y sección) **y** el correo del flujo. Hoy no hay cupo para crear la sección de un DM nuevo.

**Cuando cambia un DM, un RM o una tienda** [Dueño]: actualizar el formulario (listas y sección) **y** el correo del flujo. Hoy no hay cupo para crear la sección de un DM nuevo.

## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- Es un aviso, no una solicitud de aprobación: cada respuesta se notifica en el momento.
- El primer ID de cada lote debe ser el último de la base más 1, sin saltos.
- Una respuesta es un evento y puede abarcar varias rutas combinadas.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Evento** | Una respuesta del formulario (`ID`). Puede abarcar varias rutas combinadas |
| **Fecha del evento** | Order Change → `Date of Route Execution` · Day y Order+Day → `New Execution Date` · Split → `First Route Execution Date` |
| **Motivo** | **A** ausencia temporal · **C** contingencia de la tienda · **H** festivo |
| **Global Route ID / Route ID** | Códigos del Route Master: `G` o `R` + estado + 3 dígitos (ej. `GFL001`, `RFL002`). Las rutas combinadas se separan con "-" |
| **Parada (Stop 1–8)** | El nuevo orden en que se ejecutaron las tiendas ese día, con formato número + cadena (ej. `101Sprouts`) |
| **Jerarquía** | RM → DM → FS. Cada DM tiene un solo RM |
| **`Count?`** | Criterio del archivo de PERFORMANCE: `No` = no se tiene en cuenta en **ese** análisis. No aplica al dashboard |
| **Registro de prueba** | Respuesta del administrador para probar el formulario o el flujo (IDs 1, 15 y 16) |
| **Lote semanal** | IDs nuevos que se cargan cada semana. El primer ID debe ser el último de la base + 1 |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | El formulario MUST registrar cada ruta no ejecutada según el plan, con tipo de cambio, motivo, tiendas y justificación | Must Have | ✅ 832 respuestas | Dueño |
| FR-02 | El correo del flujo MUST salir completo: fechas de las rutas *split*, todas las paradas y todos los DM | Must Have | ⚠️ Incompleto en varios casos (IRR-A03) | Dueño |
| FR-03 | El formulario SHOULD permitir agregar un DM sin rediseñarse | Should Have | ❌ 194 de 200 preguntas (IRR-A07) | Dueño |
| FR-04 | Los campos clave MUST validarse: email del FS y IDs de ruta contra el Route Master | Must Have | ❌ Texto libre; 7–9 % de los IDs fuera de formato (IRR-A10) | Dueño |
| FR-05 | La base del dashboard MUST contener todas las respuestas, sin pruebas, y coincidir con el reporte de cumplimiento | Must Have | ❌ 736 frente a 707; falta el ID 429 (IRR-A02, IRR-A05) | Dueño |
| FR-06 | La carga a la base SHOULD ser automática, o tener un control de lo cargado | Should Have | ⚠️ Semanal y manual (IRR-A06) | Dueño |
| FR-07 | La suplente MUST poder operar los 6 componentes | Must Have | ❌ 0 de 6 (IRR-A01) | Dueño |
| FR-08 | La descripción del formulario MUST decir lo que hace: un aviso, sin validación previa | Should Have | ⚠️ Promete una validación que no existe (IRR-A08) ⚠️ C-02 | Dueño · Inicial |
| FR-09 | El formulario MUST pedir cuenta de la empresa a quien responde | Must Have | ❓ El dueño dice que sí; el análisis inicial decía que era público ⚠️ C-01 | Dueño · Inicial |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Respuestas del formulario cargadas en la base | 737 de 832 (falta el lote 738–832 y el ID 429) | 832 de 832 | Dueño |
| SC-02 | Registros del dashboard frente al análisis de cumplimiento | 736 frente a 707 | La misma cifra | Dueño |
| SC-03 | Correos con todos los datos (fechas *split*, paradas) | 40 *split* sin fechas | 0 | Dueño |
| SC-04 | IDs de ruta fuera de formato | 7 % a 9 % | 0 (validados contra el Route Master) | Dueño |
| SC-05 | Componentes que opera la suplente | 0 de 6 | 6 de 6 | Dueño · Inicial |
| SC-06 | Margen de preguntas del formulario | 6 (194 de 200) | Espacio para al menos un DM nuevo (13 preguntas) | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Recopila nombres, emails y justificaciones; el email del FS es texto libre; el flujo y el agente dependen de cuentas personales | Inicial · Dueño |
| Estabilidad | Alto | Todo depende de una persona, la suplente no tiene accesos, un reporte real se perdió y los dos reportes no cuadran ⚠️ C-06 | Inicial · Dueño |
| Escalabilidad | Alto | 194 de 200 preguntas: no cabe otro DM; la carga semanal es manual ⚠️ C-06 | Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🔴 Crítica | **No se puede agregar otro DM.** Microsoft Forms permite 200 preguntas, el formulario tiene 194 y cada sección de DM ocupa 13. Hay que rediseñar cómo se capturan las tiendas. | Dueño |
| R2 | 🟠 Alta | **El correo del flujo llega incompleto en algunos casos:** Las rutas *split* (40 casos) llegan sin fechas. Falta la parada 8 (sección de un DM). En la parada 3 falta la tienda de un DM y la de otro DM sale repetida. El email del FS se escribe a mano y va en copia: si está mal escrito (11 casos), el envío probablemente falla. | Dueño |
| R3 | 🟠 Alta | **Los dos reportes no cuadran.** El dashboard cuenta 736 registros, sin las ≈ 160 correcciones de IDs y con 3 pruebas del administrador (IDs 1, 15 y 16). El archivo de PERFORMANCE usa `Cleandata` y cuenta 707. | Dueño |
| R4 | 🟠 Alta | **Se perdió un reporte real:** el **ID 429** (Route Day Change, GTX055, 2026-09-16) no está en ninguna de las dos bases. | Dueño |
| R5 | 🟠 Alta | **La suplente todavía no tiene accesos.** El formulario, el flujo (y sus conexiones), el agente y la carga dependen de las cuentas de Jeronimo Sanchez. | Dueño |
| R6 | 🟠 Alta | **Hay campos clave en texto libre:** el email del FS y los IDs de ruta. Entre el 7 % y el 9 % de los IDs no siguen el formato, aunque todos salen del Route Master. | Dueño |
| R7 | 🟡 Media | **Otros detalles:** Tope de 7 paradas por DM: 61 reportes llegaron al tope. La descripción del formulario habla de una "validación previa" que no existe. La justificación es un campo de una sola línea. | Dueño |
| R8 | 🟠 Alta | Los nombres y justificaciones que recopila el formulario no tienen una regla de retención ni de quién puede descargarlos (Q-17) | Inicial |
| R9 | 🟠 Alta | Si el dueño cambia de rol o sale, se pierde el control del formulario y del flujo | Inicial · Dueño |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Cargar el lote pendiente, recuperar el ID 429 y completar el correo del flujo | Los reportes cuadran y el aviso sale completo | IRR-A02, IRR-A03, IRR-A04 | Dueño |
| Corto plazo | Alinear las correcciones de IDs con PERFORMANCE y ajustar el formulario (email del FS, justificación larga, ayuda y descripción) | Una sola cifra y menos errores de captura | IRR-A05, IRR-A08 | Dueño |
| Mediano plazo | Que el mismo flujo agregue cada respuesta a la base y rediseñar la captura de tiendas | Sin export, recorte ni pegado manual; sin tope de 7 paradas | IRR-A06, IRR-A07 | Dueño |
| Largo plazo | Validar los IDs contra el Route Master, reglas de calidad y columnas derivadas; mover la base a SQL | Datos validados al entrar | IRR-A10, IRR-A11, IRR-A12 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| IRR-A01 | Dar a Jennifer Guarin acceso a los 6 componentes (formulario, flujo, agente, carpeta, dashboard, buzón) | P0 | Dueño y suplente | Dueño | T-001 |
| IRR-A02 | Cargar el lote 738–832 y recuperar el ID 429 | P0 | Dueño | Dueño | T-005 |
| IRR-A03 | Completar el correo (fechas *split*, parada 8, parada 3 de dos DM) | P0 | Dueño | Dueño | T-006 |
| IRR-A04 | Proteger la copia al FS de emails inválidos y activar las alertas de falla | P0 | Dueño | Dueño | T-007 |
| IRR-A05 | Con PERFORMANCE: llevar las correcciones de IDs a la base del dashboard, quitar las pruebas y documentar `Count?` | P1 | Dueño y PERFORMANCE | Dueño | T-008 |
| IRR-A06 | Que el mismo flujo agregue cada respuesta a `Table1` (elimina el export, el recorte, el agente y el pegado manual) | P1 | Dueño | Dueño | T-030 |
| IRR-A07 | Rediseñar la captura de tiendas para liberar preguntas y quitar el tope de 7 paradas | P1 | Dueño | Dueño | T-020 |
| IRR-A08 | Ajustes al formulario: email del FS, justificación larga, sección de un DM, ayuda en el cargo, motivo "vacante" y nueva descripción | P1 | Dueño | Dueño | T-010 a T-015 |
| IRR-A09 | Mover exports y consolidados a SharePoint | P2 | Dueño | Dueño | T-002 |
| IRR-A10 | Validar los IDs contra el Route Master | P2 | Dueño | Dueño | T-031 |
| IRR-A11 | Reglas de calidad | P2 | Dueño | Dueño | T-032 |
| IRR-A12 | Columnas derivadas para el dashboard | P2 | Dueño | Dueño | T-034 |
| IRR-A13 | Confirmar en la configuración de Forms que solo responden cuentas de la empresa, y que el formulario no es público | P0 | Dueño | Inicial | C-01 |
| IRR-A14 | Definir cuánto tiempo se conservan las respuestas y quién puede descargarlas | P1 | Dueño y PM | Inicial | Q-17 |
| IRR-A15 | Hacer la revisión técnica con IT: datos de personas y flujo atado a cuentas personales | P1 | IT | Inicial | — |
| IRR-A16 | Guardar esta spec, el paquete del flujo y el script de consolidación en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| IRR-A17 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |

**Canceladas por el dueño:** T-040 Flujo de aprobación: cancelado (es un aviso, no una solicitud).


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-05b | ¿En qué se diferencian el Global Route ID y el Route ID, y dónde está el Route Master? | Dueño del Route Master | Dueño |
| Q-06b | ¿Por qué falta el ID 429? | Jeronimo Sanchez | Dueño |
| Q-07 | ¿La vacante necesita un motivo propio? | Operaciones y RMs | Dueño |
| Q-08 | ¿Cuál es el plazo para reportar? | Operaciones y RMs | Dueño |
| Q-09 | ¿En qué zona horaria están las marcas de tiempo? | Jeronimo Sanchez | Dueño |
| Q-10 | Dos DM no tienen reportes. ¿Faltan reportes o sus rutas no tienen excepciones? Según el Store Master, los dos están activos | RMs | Dueño |
| Q-13 | ¿Quiénes reciben el buzón `route.request`? | Administración de correo | Dueño |
| Q-15 | En una ruta *split*, ¿las paradas cubren los dos días? | Jeronimo Sanchez y FS | Dueño |
| Q-16 | ¿Quién mantiene `Cleandata`? | Jeronimo Sanchez y PERFORMANCE | Dueño |
| Q-17 | ¿Cuánto tiempo se conservan las respuestas y quién puede descargarlas? | Dueño y PM | Inicial |
| Q-18 | ¿Quiénes tienen acceso a la base y a las carpetas, y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |
| Q-19 | ¿El formulario exige iniciar sesión con la cuenta de la empresa, o puede responderlo quien tenga el enlace? | Dueño | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Acceso al formulario | Inicial: el enlace es público y quien responde no inicia sesión. Dueño: se llena con la cuenta corporativa | Cuenta corporativa; confirmar en Forms que solo responden cuentas de la empresa (Q-19) | ❓ Por confirmar |
| C-02 | Aviso o aprobación | Inicial: toda excepción exige justificación y validación previa. Dueño: es un aviso, y la «validación previa» no existe | Es un aviso; corregir la descripción del formulario (IRR-A08) | ✅ Resuelta a favor del dueño |
| C-03 | Dónde se guardan las respuestas | Inicial: por confirmar. Dueño: Forms → correo de Power Automate → `Table1` en SharePoint, con carga semanal manual | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-04 | Frecuencia | Inicial: bajo demanda. Dueño: ≈ 74 respuestas por semana y carga semanal a la base | Se llena a demanda y la base se actualiza cada semana | ✅ Resuelta a favor del dueño |
| C-05 | Quién recibe las respuestas | Inicial: el administrador. Dueño: el buzón `route.request` y la jerarquía, por correo | Lo del dueño; falta saber quiénes reciben el buzón (Q-13) | ✅ Resuelta a favor del dueño |
| C-06 | Nivel de riesgo | Inicial: estabilidad y vulnerabilidad «Medio». Dueño: tope de 200 preguntas, correo incompleto, reportes que no cuadran y suplente sin accesos | Estabilidad «Alto», escalabilidad «Alto» y vulnerabilidad «Medio» | ❓ Por confirmar |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de datos, mapa de las 200 columnas, revisión del flujo pregunta por pregunta, registro de aclaraciones y estadísticas) todavía no están integrados.
- La distribución de reportes por RM y DM está en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/incident-reporting-route/spec.md`. [Inicial]
- Incluir en el mismo repositorio el paquete exportado del flujo «Incident Reporting Process» y el script `consolidate_incident_report.py`, sin respuestas ni datos de personas. [Dueño · Inicial]
- Describir la estructura del formulario (secciones, preguntas y lógica de ramificación) en un archivo, para poder rehacerlo y para controlar el tope de 200 preguntas. [Inicial]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Modelar una tabla de eventos (clave primaria `ID`) y una tabla de paradas (una fila por parada, de 1 a 8), en lugar de 200 columnas. [Dueño · Inicial]
2. Hacer que el mismo flujo de Power Automate escriba cada respuesta en SQL: elimina el export, el recorte, el agente y el pegado (IRR-A06). [Dueño]
3. Validar el ID de ruta contra el Route Master al cargar (IRR-A10). [Dueño]
4. Dejar `Cleandata` como una vista con las correcciones de IDs y la columna `Count?`, para que el dashboard y el análisis de cumplimiento lean la misma fuente. [Dueño · Inicial]
5. Conservar el nombre de la hoja y los encabezados que hoy lee el dashboard, mediante una vista de compatibilidad. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; la descripción del formulario es incorrecta |
| Responsables | 2 | Dueño definido; la suplente no tiene ningún acceso |
| Operación documentada | 3 | Lista de verificación semanal escrita |
| Control de acceso | 2 | Cuenta corporativa por confirmar; flujo y agente atados a cuentas personales |
| Contrato de datos | 2 | Campos clave en texto libre; 200 columnas a 29 por un agente |
| Calidad y validación | 2 | 7 % a 9 % de IDs fuera de formato; emails con error |
| Automatización e integración | 2 | El flujo envía el correo; la carga a la base es manual |
| Trazabilidad de cambios | 2 | Un reporte real perdido; las dos bases no cuadran |
| Entornos y pruebas | 2 | Las pruebas del administrador quedaron en la base |

**Nivel global: 2,2 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.
