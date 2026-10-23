# Spec · Plan de visitas (Unify)

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m22 (inventario MIC) |
| Tipo | Base de datos: carpeta de libros de Excel mensuales (Labor Unif) y generador `plan1.xlsx` con Power Query |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Plan mensual de ejecución de rutas: una fila por tienda activa y por día del mes, con ruta, orden de parada, horas de servicio, costo de servir, millas, tiempo de manejo, ventana horaria y RM → DM → FS. Como el Route Master y el Store Master solo guardan el estado de hoy, **cada Labor Unif es el único registro de cómo estaba el plan ese mes**. También se conoce como Plan Unify o «Labor Unif». [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Octubre | 77.188 filas · 2.411 tiendas · 31 días · 1.285 rutas · 60.024 h planeadas · 44.720 filas con visita (58 %) ⚠️ C-07 | Dueño |
| Clientes | Walmart 55.668 · Sprouts 15.724 · Costco 5.796 filas | Dueño |
| Costo | 53 tarifas por hora (17,51 a 56,50); `$ /dia` = horas × tarifa en el 100 % de octubre | Dueño |
| Libro mensual | 1 hoja (`Labor Report`), 25 columnas, 7,9 MB | Dueño |
| Generador | `plan1.xlsx`: 19,9 MB · 4 hojas (3 ocultas) · 12 consultas · 91 versiones | Dueño |
| Carpeta UNIFY | 8 archivos · 735 versiones guardadas · permisos propios | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Medio ⚠️ C-05 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🟠 **Septiembre tiene el Labor Day con la etiqueta de día cambiada:** 4.739 filas con el día de la semana intercambiado, un error que corrige el dueño; las 172 filas repetidas del 8 son intencionales. [Dueño]
2. 🟠 **Los ajustes parciales se pegan al final y pueden duplicar el plan:** en septiembre, 586 filas pegadas y 39 tienda–día con las filas viejas todavía con horas. [Dueño]
3. 🟠 **Las columnas cambian de un mes a otro** y *Last Visit* lee estos archivos. [Dueño] ⚠️ C-01
4. 🟠 **El plan regenerado hoy no es el plan pegado,** por eso el Unif es el único registro de cada mes. [Dueño]
5. 🟠 **Todo depende de dos personas** y de un procedimiento no escrito; además el alcance del query no es el que se quiere. [Dueño]

**Funciona bien:** una fila por tienda y fecha (Octubre sin repetidas ni etiquetas de día mal puestas), toda fila con horas tiene ruta y costo, `$ /dia` correcto en Octubre, jerarquía de 4 RM / 14 DM / 105 FS, y el generador lee las fuentes **por nombre de columna**. [Dueño]

**Contradicciones:** 7 detectadas; 5 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (UNI-A01, UNI-A02, UNI-A03, UNI-A04, UNI-A05, UNI-A06, UNI-A07, UNI-A21, UNI-A25) y las preguntas Q-05 y Q-13. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Dar a PERFORMANCE un plan mensual de rutas con horas y costo, para comparar lo real contra lo planeado en el dashboard *Last Visit*, y conservar cómo estaba el plan cada mes.

- **Problema que resuelve:** el Route Master y el Store Master solo guardan el estado de hoy; sin los Labor Unif no hay registro del plan de cada mes. [Dueño]
- **Qué logra:** una fila por tienda y día con ruta, orden, horas, costo de servir, millas, manejo y ventana horaria. [Dueño]
- **Éxito:** un plan mensual con estructura fija, sin duplicados ni etiquetas cruzadas, que PERFORMANCE lee sin sorpresas (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: los libros mensuales (hoja `Labor Report`), el generador `plan1.xlsx`, el proceso mensual de generar, pegar y ajustar, y el contrato con PERFORMANCE.

**No incluye** [Dueño]: el Route Master, el Store Master y el FS Route Master (dependencias). No se revisó el Histórico hasta marzo ni el dashboard *Last Visit*.

**Futuro** [Dueño]: una foto mensual de los maestros (UNI-A18), generación automática (UNI-A19) y consolidar el Histórico (UNI-A20).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Responsables (el dueño y su suplente) | Generan y ajustan el plan; se respaldan entre sí | Cada mes | Dueño |
| PERFORMANCE | Usa los archivos para el dashboard *Last Visit* (real contra plan) | 7 meses | Dueño |
| Otras personas que guardan versiones | Según el dueño, solo visualizan o filtran; falta bloquearles la edición | 4 personas | Dueño |
| Visit FS y Costco Report ❓ | El inventario los lista como lectores; el dueño no los menciona (Q-13) | — | Inicial |

**Acceso**

- La carpeta UNIFY está en SharePoint › Sales Administration – Horas labor, con permisos propios; el generador está en otro sitio (Costo de Servir – Desviaciones › Herramienta Plan). [Dueño]
- Exige cuenta de la empresa y permiso. [Inicial]
- Para generar el plan, Excel necesita credenciales de SharePoint. [Dueño]
- ❓ Falta la lista de personas con acceso a la carpeta y su permiso, y bloquear la edición a quienes solo consultan (Q-14). [Inicial · Dueño]

## Dueño funcional

**Jeronimo Sanchez**, junto con su suplente: ambos generan y ajustan el plan y se respaldan entre sí. [Dueño] ⚠️ C-03

- Cada mes cambia las fechas, actualiza el generador, crea el libro del mes y pega el plan.
- Completa la tarifa por hora y hace los ajustes del mes.
- Corrige el error del `Weekday` de septiembre.
- Aprobó su análisis el 2026-10-21 (v1.2).

## Administrador técnico

**Jeronimo Sanchez**, administra la carpeta y el generador. [Inicial]

- Administra los libros en SharePoint y el código de Power Query de `plan1.xlsx`. [Dueño]
- ❓ Quién aprueba los accesos nuevos a la carpeta (Q-14).

## Suplente

**Jennifer Guarin.** Se respalda con el dueño: ambos generan y ajustan el plan. Falta verificar los accesos de ambos a los 3 libros de origen, a `plan1.xlsx` y a las tarifas. [Dueño]

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Route Master, Store Master y FS Route Master | Poder leerlos desde el generador | ⬜ Por verificar (UNI-A01) |
| `plan1.xlsx` | Actualizarlo y copiar la hoja del plan | ⬜ Por verificar (UNI-A01) |
| Archivo de tarifas del mes | Leerlo para completar la tarifa | ⬜ Por verificar (UNI-A01) |
| Carpeta UNIFY | Crear y editar el libro del mes | ⬜ Por verificar (UNI-A01) |
| Procedimiento mensual y de ajustes | Seguirlo sin ayuda | ⬜ Pendiente (UNI-A03) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| DSD Route Master (`RouteMaster`) | Ruta, orden, duración, millas y manejo de cada tienda | Equipo del Route Master | Dueño |
| DSD Store Master (`StoreMaster`) | Tiendas activas y jerarquía (declara el tipo de unas 60 columnas por nombre) | Dueño | Dueño |
| DSD FS Route Master (`CostFS`) | Costo diario del FS (`C2S FS`) | Dueño | Dueño |
| `Rate para labor <mes>` | Tarifa por hora; la crean otra persona del equipo o la suplente, y se aplica con un cruce por distrito o estado | Dueño y suplente | Dueño |
| Ajustes a mano | Cierres de tiendas, rutas partidas y feriados durante el mes | Dueño y suplente | Dueño |

**Cómo se produce** [Dueño]

1. En `plan1.xlsx` se cambian `Start Date` y `End Date` (están dentro del código de Power Query).
2. Al actualizar, el generador lee en vivo los tres libros de origen y cruza cada tienda activa con cada fecha y con la ruta que le toca ese día de la semana.
3. Se copia la hoja `Plan STime (Unify)` y se pega en el libro nuevo del mes, en la carpeta UNIFY.
4. Se completan a mano la tarifa por hora y el costo diario, que el generador deja vacíos a propósito.
5. Durante el mes los cambios se hacen a mano en el libro del mes; si son muchos, se regenera en `plan1` y se pegan solo las filas editadas desde el día del cambio.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | Excel con Power Query y credenciales de SharePoint · SharePoint (carpeta UNIFY y Herramienta Plan) |
| Archivos | Los 3 libros de origen · el archivo de tarifas del mes · `plan1.xlsx` |
| Personas | El dueño y su suplente |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| PERFORMANCE | Lee los archivos para *Last Visit*; depende del nombre de la hoja, de los encabezados y de algunas columnas | PERFORMANCE |
| Visit FS y Costco Report ❓ | El inventario los lista como lectores (Q-13) | PERFORMANCE |

## Procesos operativos

[Dueño] Ciclo **mensual**: un libro por mes y ajustes durante el mes. Un mes se sigue editando semanas después de terminar (abril tiene versiones hasta el 14 de agosto). ⚠️ C-02

1. **Inicio de mes:** cambiar `Start Date` y `End Date`, actualizar `plan1.xlsx`, crear el libro del mes desde la plantilla y pegar la hoja `Plan STime (Unify)` (sin cambiar encabezados ni columnas).
2. **Tarifa:** completar `Pay Rate/ Hour` con el archivo del mes y verificar que `$ /dia` sea fórmula en todas las filas.
3. **Validar:** tiendas activas con fila, sin filas repetidas, `Weekday` = día de la fecha, `C2S FS` presente, sin filtros ni filas vacías.
4. **Ajustes:** registrar fecha, filas, motivo y autor; tienda cerrada de una sola manera; al regenerar, **anular las filas viejas antes de pegar las nuevas**.
5. **Feriados:** mover el plan cambiando la fecha, nunca la etiqueta del día; revisar que no queden filas dobles.
6. **Avisar:** a PERFORMANCE antes de cambiar columnas, hoja o encabezados, y de cada ajuste importante.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- El Unif del mes es el único registro del plan de ese mes: no se regenera un mes ya pegado.
- La visita del lunes movida y la del martes se registran las dos (las filas dobles del 8 son intencionales).
- Michaels, Walgreens y CVS quedan fuera a propósito: no tienen ruta de ejecución.
- Los feriados mueven el plan cambiando la fecha, nunca la etiqueta del día.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Fila del plan** | `Store` + `fecha` + `ROUTE` + `ORDER`. Un día sin visita = 0 horas y sin ruta (42 % de las filas). Costco puede tener 2 a 4 paradas el mismo día |
| **Horas Regulares /dia** | Horas de la visita = `Duration` del Route Master ÷ 60 |
| **Pay Rate / Hour y $ /dia** | Tarifa por hora (se completa a mano) y costo del día = horas × tarifa |
| **C2S / C2S FS** | Costo de servir de la parada (Route Master) y costo diario promedio del FS (FS Route Master) |
| **Window time** | `7am-12pm` si la parada empieza antes de las 12:00, `12pm-7pm` si no |
| **Tienda activa (para el plan)** | `Active` distinto de `N` y cliente Costco, ElSuper, Fiesta, Sprouts o Walmart (incluye `P`) ⚠️ |
| **Ajuste a mano / regeneración parcial** | Cambio directo en el libro del mes; o regenerar en `plan1` y pegar solo las filas editadas desde el día del cambio |
| **Histórico** | `Labor Unif Historico hasta Marzo 2026` (63 MB); desde Abril, un archivo por mes |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | El plan MUST tener una fila por tienda activa y por fecha, sin repetidas ni etiquetas de día mal puestas | Must Have | ⚠️ ✅ en octubre; septiembre con 4.739 filas de etiqueta cruzada (UNI-A05) | Dueño |
| FR-02 | Toda fila con horas MUST tener ruta y costo | Must Have | ✅ En octubre | Dueño |
| FR-03 | El alcance MUST ser Walmart, Sprouts y Costco con `Active = Y` | Must Have | ❌ El query usa `Active <> "N"` y 5 clientes (UNI-A14) | Dueño |
| FR-04 | La tarifa por hora MUST salir de un paso documentado | Must Have | ❌ Sin procedimiento (UNI-A08) | Dueño |
| FR-05 | La hoja, el orden y los encabezados MUST mantenerse entre meses | Must Have | ❌ Las columnas cambian de un mes a otro (UNI-A07) ⚠️ C-01 | Dueño · Inicial |
| FR-06 | Los ajustes MUST registrarse y las filas viejas anularse antes de pegar las nuevas | Must Have | ❌ 586 filas pegadas al final en septiembre (UNI-A09) | Dueño |
| FR-07 | La tienda cerrada MUST registrarse de una sola manera | Must Have | ❌ 543 tienda–día borrados y 3 tiendas con 0 horas (UNI-A05) | Dueño |
| FR-08 | El generador MUST tolerar que el Store Master cambie los nombres de columnas | Should Have | ❌ Declara el tipo de unas 60 por nombre (UNI-A12) | Dueño |
| FR-09 | PERFORMANCE MUST ser avisado antes de cambiar la hoja, el orden o los encabezados | Must Have | ❌ Sin contrato (UNI-A15) | Dueño |
| FR-10 | Los libros mensuales MUST abrirse sin filtros ni filas vacías | Should Have | ❌ Filtros en 5 de 7; ≈ 140.000 filas vacías (UNI-A06, UNI-A10) | Dueño |
| FR-11 | La suplente MUST poder generar y ajustar el plan | Must Have | ⚠️ Accesos por verificar (UNI-A01) | Dueño · Inicial |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Filas con la etiqueta del día cruzada en septiembre | 4.739 | 0 | Dueño |
| SC-02 | Archivos con filtros activos | 5 de 7 | 0 | Dueño |
| SC-03 | Filas de octubre con el costo diario del FS vacío | 1.674 | 0 | Dueño |
| SC-04 | Meses con la misma estructura de columnas | No (cambian entre meses) | Todos, con plantilla | Dueño |
| SC-05 | Personas que editan los libros | Varias guardan versiones | Solo el dueño y su suplente | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Tarifas por hora y costo por tienda y día; permisos propios; otras personas guardan versiones y falta bloquear la edición | Inicial · Dueño |
| Estabilidad | Alto | Todo depende de dos personas y de un procedimiento no escrito; el plan regenerado no coincide con el pegado; los ajustes se pegan sin registro ⚠️ C-05 | Inicial · Dueño |
| Escalabilidad | Medio | ≈ 77.000 filas por mes en un libro por mes; el histórico crece y hay ≈ 140.000 filas vacías con formato | Inicial · Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🟠 Alta | **Septiembre tiene el Labor Day con la etiqueta de día cambiada.** El plan del lunes 7 se movió al martes 8: **4.739 filas con el día de la semana intercambiado** (el 7 dice `Tuesday`, el 8 dice `Monday`) es un **error que corrige el dueño**. Las **172 tienda–ruta–parada repetidas el 8** (171 Costco, 1 Walmart; 459,8 h) son **intencionales**: la visita del lunes movida más la del martes. | Dueño |
| R2 | 🟠 Alta | **Los ajustes parciales se pegan al final y pueden duplicar el plan.** Septiembre: **586 filas pegadas al final** (52 tiendas, del 5 al 30); en **39 tienda–día** las filas viejas siguen con horas (43,3 h). No hay registro de los cambios. | Dueño |
| R3 | 🟠 Alta | **Las columnas cambian de un mes a otro.** Millas y tiempo de manejo existen desde Junio; `C2S FS` falta en Abril y Agosto y en el 99 % de Septiembre; la ventana horaria existe desde Agosto. *Last Visit* lee estos archivos. | Dueño |
| R4 | 🟠 Alta | **El plan regenerado hoy no es el plan pegado.** `plan1` (21-oct) trae 1.754 filas que el Unif de Octubre no tiene y viceversa 1.196, y el costo de servir es distinto en el 7,3 % de las filas que coinciden. Por eso no se regenera el mes, y por eso el Unif es el único registro del plan. No se puede separar ajuste manual de cambio de maestros. | Dueño |
| R5 | 🟠 Alta | **La tarifa por hora se llena en un paso aparte sin procedimiento.** Sale de `Rate para labor <mes>` (la crean otra persona del equipo o Jennifer Guarin; el de Octubre es del 2026-10-02) y se aplica con un cruce por distrito o estado. La descripción inicial no lo incluía. | Dueño |
| R6 | 🟠 Alta | **Las tiendas cerradas se registran de dos maneras.** En Octubre **32 tiendas tienen menos de 31 días** (543 tienda–día borrados) y 3 tiendas dejaron 29 filas con ruta y **0 horas**. Una tienda sin fila no es lo mismo que una con 0 horas. | Dueño |
| R7 | 🟠 Alta | **El generador se rompe si el Store Master renombra una columna** (declara el tipo de ~60 por nombre; agregar no rompe). | Dueño |
| R8 | 🟠 Alta | **El alcance del query no es el que se quiere.** Hoy usa `Active <> "N"` y clientes Costco, ElSuper, Fiesta, Sprouts, Walmart. **Decidido:** solo Walmart, Sprouts y Costco con `Active = Y`; Michaels, Walgreens y CVS quedan fuera a propósito (no tienen ruta de ejecución). Falta cambiar el query. | Dueño |
| R9 | 🟠 Alta | **Costo diario del FS vacío en 1.674 filas de Octubre** (957 con horas). | Dueño |
| R10 | 🟡 Media | **Nombres cruzados en `plan1.xlsx`:** la hoja visible `Plan STime (Unify)` la alimenta la consulta `Plan STime (test)`, y hay 3 hojas ocultas más. | Dueño |
| R11 | 🟡 Media | **Filtros dejados activos** en 5 de 7 archivos (Octubre muestra 31 de 77.188 filas) y **~140.000 filas vacías con formato** en Abril–Agosto. | Dueño |
| R12 | 🟡 Media | **`$ /dia` ≠ horas × tarifa** en Abril (2.085 filas), Mayo (3.377), Julio (2.446) y Junio (15); en Agosto, Septiembre y Octubre, 0. | Dueño |
| R13 | 🟠 Alta | **Todo depende de dos personas y de un procedimiento no escrito.** Además guardan versiones PERFORMANCE, otra persona y otra persona; según el dueño solo visualizan o filtran, y falta bloquearles la edición. | Dueño |
| R14 | 🟠 Alta | La carpeta concentra el historial laboral de todos los meses y su lista de permisos no está revisada (Q-14) | Inicial |
| R15 | 🟡 Media | Si Visit FS y Costco Report leen estos archivos, un cambio de columnas los rompe sin aviso (Q-13) | Inicial |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Corregir septiembre, cambiar el query al alcance definido, quitar los filtros y escribir el procedimiento mensual | Plan correcto y repetible | UNI-A03, UNI-A05, UNI-A06, UNI-A14 | Dueño |
| Corto plazo | Plantilla con estructura fija, tarifa documentada, registro de ajustes y contrato con PERFORMANCE | Menos sorpresas para *Last Visit* | UNI-A07, UNI-A08, UNI-A09, UNI-A15 | Dueño |
| Mediano plazo | Ordenar `plan1.xlsx`, hacer tolerante la consulta del Store Master y limpiar abril a agosto | Generador más estable | UNI-A10, UNI-A11, UNI-A12 | Dueño |
| Largo plazo | Foto mensual de los maestros, generación automática y Histórico consolidado; mover el plan a SQL | Plan reproducible y sin archivos mensuales | UNI-A18, UNI-A19, UNI-A20 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| UNI-A01 | Accesos y lista de editores | P0 | Dueño | Dueño | T-001 |
| UNI-A02 | Publicar documento y diccionario | P0 | Dueño | Dueño | T-002 |
| UNI-A03 | Procedimiento mensual y de ajustes | P0 | Dueño | Dueño | T-003 |
| UNI-A04 | Hoja `Control` | P0 | Dueño | Dueño | T-004 |
| UNI-A05 | Corregir Septiembre y revisar cierres | P0 | Dueño | Dueño | T-005 |
| UNI-A06 | Quitar filtros | P0 | Dueño | Dueño | T-006 |
| UNI-A07 | Plantilla con estructura fija | P0 | Dueño | Dueño | T-007 |
| UNI-A08 | Tarifa por hora documentada/automatizada | P1 | Dueño | Dueño | T-008 |
| UNI-A09 | Registro de ajustes y regla de anular antes de pegar | P1 | Dueño | Dueño | T-009 |
| UNI-A10 | Limpiar Abril–Agosto | P1 | Dueño | Dueño | T-010 |
| UNI-A11 | Ordenar `plan1.xlsx` | P1 | Dueño | Dueño | T-011 |
| UNI-A12 | Consulta del Store Master tolerante y fechas en una celda | P1 | Dueño | Dueño | T-012 |
| UNI-A13 | Diccionario | P1 | Dueño | Dueño | T-013 |
| UNI-A14 | Alcance escrito | P1 | Dueño | Dueño | T-014 |
| UNI-A15 | Contrato con *Last Visit* | P1 | Dueño | Dueño | T-015 |
| UNI-A16 | Revisar editores | P1 | Dueño | Dueño | T-016 |
| UNI-A17 | Cierre de mes | P1 | Dueño | Dueño | T-017 |
| UNI-A18 | Foto mensual de los maestros | P2 | Dueño | Dueño | T-018 |
| UNI-A19 | Generación automática | P2 | Dueño | Dueño | T-019 |
| UNI-A20 | Consolidar el Histórico | P2 | Dueño | Dueño | T-020 |
| UNI-A21 | Cambiar el query del generador a Walmart, Sprouts y Costco con `Active = Y` | P0 | Dueño | Dueño | T-014 |
| UNI-A22 | Confirmar con PERFORMANCE si Visit FS y Costco Report leen estos archivos y corregir el inventario | P1 | Dueño y PERFORMANCE | Inicial | C-04 |
| UNI-A23 | Hacer la revisión técnica con IT: tarifas por hora y costo por tienda y día | P1 | IT | Inicial | — |
| UNI-A24 | Guardar esta spec, las consultas de `plan1.xlsx` y la plantilla del libro mensual en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| UNI-A25 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-06 | cierres de tienda (filas borradas o con 0 horas) | Dueño (se resuelve con su tarea) | Dueño |
| Q-07 | `C2S FS` faltante | Dueño (se resuelve con su tarea) | Dueño |
| Q-08 | valores de `Type` | Dueño (se resuelve con su tarea) | Dueño |
| Q-09 | filtros y filas vacías | Dueño (se resuelve con su tarea) | Dueño |
| Q-10 | hojas y consultas sin uso | Dueño (se resuelve con su tarea) | Dueño |
| Q-11 | quién edita los Unif (✅ solo visualizan o filtran) | Dueño (se resuelve con su tarea) | Dueño |
| Q-12 | cierre de mes e histórico | Dueño (se resuelve con su tarea) | Dueño |
| Q-13 | ¿Visit FS y Costco Report leen estos archivos, o solo Last Visit? | Dueño y PERFORMANCE | Inicial |
| Q-14 | ¿Quiénes tienen acceso a la carpeta UNIFY y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Estructura entre meses | Inicial: un archivo por mes con la misma estructura. Dueño: las columnas cambian (millas y manejo desde junio; `C2S FS` falta en abril, agosto y casi todo septiembre; ventana horaria desde agosto) | Lo del dueño; plantilla con estructura fija (UNI-A07) | ✅ Resuelta a favor del dueño |
| C-02 | Frecuencia | Inicial: según la necesidad. Dueño: ciclo mensual, con ajustes durante el mes y ediciones semanas después | Mensual, con ajustes | ✅ Resuelta a favor del dueño |
| C-03 | Quién la mantiene | Inicial (inventario): creada por la suplente y administrada por el dueño. Dueño: ambos la generan y se respaldan entre sí | Los dos; dueño funcional: Jeronimo Sanchez, según el Excel del equipo | ✅ Resuelta a favor del dueño |
| C-04 | Quién la lee | Inicial: Last Visit, Visit FS y Costco Report. Dueño: PERFORMANCE, para Last Visit | Lo del dueño; confirmar los otros dos (Q-13) | ❓ Por confirmar |
| C-05 | Nivel de riesgo | Inicial: estabilidad «Medio». Dueño: el plan regenerado no coincide con el pegado, los ajustes se pegan sin registro y todo depende de dos personas | Estabilidad «Alto» | ❓ Por confirmar |
| C-06 | Qué es | Inicial: carpeta con un archivo por mes. Dueño: es un plan de rutas con costo, y «Labor» sugiere horas de mano de obra | Mantener el nombre del inventario y explicarlo en la descripción | ✅ Resuelta a favor del dueño |
| C-07 | Tamaño | Inicial: ≈ 74.206 filas por mes (septiembre). Dueño: 77.188 filas (octubre) | Cada mes cambia | ✅ Resuelta a favor del dueño |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, consultas, calidad de datos por mes y backlog) todavía no están integrados.
- El Histórico hasta marzo y el dashboard *Last Visit* no se han revisado.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/plan-de-visitas-unify/spec.md`. [Inicial]
- Incluir el código de las consultas de `plan1.xlsx` y la plantilla del libro mensual, sin datos de tiendas, tarifas ni personas. [Dueño · Inicial]
- Mantener el diccionario de las 25 columnas y su historial de cambios entre meses. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Una tabla del plan con clave `Store + fecha + ROUTE + ORDER` y una columna de mes, en lugar de un libro por mes. [Dueño · Inicial]
2. Guardar una foto mensual de los maestros (UNI-A18), porque hoy el Unif es el único registro de cada mes. [Dueño]
3. Generar el plan con un proceso automático (UNI-A19) y cargar el Histórico una sola vez (UNI-A20). [Dueño]
4. Guardar la tarifa por hora en una tabla por mes y aplicarla al cargar. [Dueño · Inicial]
5. Exponer una vista con el nombre de la hoja y los encabezados que hoy lee PERFORMANCE. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 3 | Dos personas que se respaldan; accesos por verificar |
| Operación documentada | 2 | Lista de verificación propuesta; el procedimiento no estaba escrito |
| Control de acceso | 2 | Permisos propios; varias personas guardan versiones |
| Contrato de datos | 1 | Las columnas cambian entre meses; sin diccionario ni contrato con PERFORMANCE |
| Calidad y validación | 2 | Octubre correcto; septiembre con errores; filas vacías y filtros |
| Automatización e integración | 2 | Generador con Power Query, pero el pegado y los ajustes son manuales |
| Trazabilidad de cambios | 1 | Los ajustes no se registran |
| Entornos y pruebas | 2 | El generador está separado de los libros mensuales |

**Nivel global: 2,0 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.
