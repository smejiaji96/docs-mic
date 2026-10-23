# Spec · DSD FS Route Master

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m21 (inventario MIC) |
| Tipo | Base de datos: libro de Excel (rutero de los supervisores de campo) alimentado desde un planner web y Power Query |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Rutero de los **supervisores de campo (FS)**. Cada fila es un paso del día de un FS: salir de su tienda base, visitar tiendas en un orden, almorzar (`BREAK`) y volver. Guarda millas y manejo, gastos de viaje y el **costo por tienda**; la jerarquía, las coordenadas y la dirección salen de una copia del Store Master. Sirve para ver la mejor manera en que cada FS visita sus tiendas y para organizar el costo de cada uno (hoja `Costs`: presupuesto mensual por FS; hoja oculta `C2SFS`: costo promedio por visita, que el DSD Route Master lee como `C2S FS/MILES`). [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 4.232 filas (2.503 visitas a tiendas + 1.158 filas de tienda base + 571 `BREAK`) × 35 columnas | Dueño |
| Rutas | 579 (`FSTN001`…), 4,3 tiendas por ruta en promedio, 71 con gastos de viaje | Dueño |
| Cobertura | 104 FS de los 105 con tiendas activas · 2.503 tiendas: Walmart 1.773 · Sprouts 475 · Michaels 163 · Costco 88 | Dueño |
| Jerarquía | 4 RMs · 14 DMs · 104 FS | Dueño |
| Libro | 11 hojas (9 ocultas) · 14 consultas de Power Query (3 en uso real) · 2 vínculos externos ⚠️ C-01 | Dueño |
| Actividad | 357 versiones en 75 días: 356 del dueño y 1 de la suplente ⚠️ C-04 | Dueño |
| Fuente | 104 archivos `Routes` y 105 `Stores` en 107 carpetas de FS | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Medio ⚠️ C-06 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🟠 **El costo por tienda se calcula en 104 archivos distintos** y llega pegado como valor: el 0,725 por milla está escrito en cada fórmula y no hay hoja de parámetros. [Dueño]
2. 🟠 **Copiar y pegar sin control:** coinciden 578 de las 579 rutas con `Router Test` y nadie avisa cuando el libro se queda atrás. [Dueño]
3. 🟠 **La copia del Store Master está atrás** (32 tiendas con otro FS, 34 con otro `Active`) y se lee por letra de columna (13 columnas). [Dueño]
4. 🟠 **92 tiendas activas sin ruta,** 4 filas con tienda inactiva o inexistente y 5 rutas con tiendas de dos FS. [Dueño]
5. 🟠 **Todo depende de una persona** (356 de 357 versiones) y el procedimiento no está escrito. [Dueño]
6. ⚠️ **El inventario lista a Last Visit y Visit FS como lectores;** el dueño solo menciona al DSD Route Master (C-03). [Inicial]

**Funciona bien:** **Estructura de las rutas:** las 579 empiezan y terminan en la tienda base; `stop` es secuencial en las 579; ninguna tienda se repite ni está en dos rutas. **Datos de cada paso:** duración y frecuencia coinciden al 100 % con `Router Test`. **Tienda base:** 92 de 93 coinciden con `Field-Supervisors_home_stores.xlsx`. **Costos:** `C2SFS` tiene los 104 FS con valor. [Dueño]

**Contradicciones:** 7 detectadas; 5 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (FSR-A01, FSR-A02, FSR-A03, FSR-A04, FSR-A05, FSR-A06, FSR-A07, FSR-A08, FSR-A09, FSR-A31) y las preguntas Q-19 y Q-20. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Ver la mejor manera en que cada FS visita sus tiendas y **organizar el costo de cada uno**: presupuesto mensual por FS y costo promedio por visita, que alimenta el costo del DSD Route Master.

- **Problema que resuelve:** FS, DM y RM necesitan coordinar sus viajes y rutas, y el costo de cada FS debe salir de un solo lugar. [Dueño]
- **Qué logra:** un rutero con todos los pasos del día de cada FS, millas, manejo, gastos de viaje y costo por tienda. [Dueño]
- **Éxito:** el costo sale de parámetros únicos, el libro coincide con `Router Test` y cada tienda activa tiene su ruta (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: el FS Route Master y el proceso que lo alimenta (carpeta `Tiendas x FS` y `Router Test`).

**No incluye** [Dueño]: el Store Master y el Route Master de mercaderistas (ya tienen su análisis); el planner web, `DM Costs`, `Travel Monthly Budget` y `Convertidor plan`, que se listan como dependencias.

**Futuro** [Dueño]: cargar sin copiar y pegar (FSR-A22), evaluar una base de datos (FSR-A23), validaciones y protección (FSR-A24) y documentar el planner (FSR-A25).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| FS, DM y RM | Consultan el rutero para coordinar sus viajes y rutas; todos tienen permiso de lectura y saben dónde está | 104 FS · 14 DM · 4 RM | Dueño |
| Responsable (el dueño) | Alimenta todo el libro | 356 de 357 versiones | Dueño |
| Suplente | Aprueba los parámetros del costo | — | Dueño |
| DSD Route Master | Lee `C2SFS` como `C2S FS/MILES` | — | Dueño |
| Presupuesto de viaje por FS (hoja `Costs`) | Presupuesto mensual por FS, tomado de `DM Costs.xlsx` | — | Dueño |

**Acceso**

- Está en SharePoint › DSD Business Analysis › DSD Data Master, con permisos propios; las fuentes están en otro sitio (Sales Administration › Field Routes › Tiendas x FS). [Dueño]
- Exige cuenta de la empresa y permiso. [Dueño · Inicial]
- La cuenta del planner la paga Falcon y la usan la suplente, el dueño y otras personas: el acceso no es el riesgo. [Dueño]
- ❓ Falta la lista de personas con acceso al libro y a la carpeta, y quién aprueba los accesos nuevos (Q-20). [Inicial]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño · Inicial]

- Alimenta todo el libro: diseña las rutas en el planner, las guarda en la carpeta del FS y las pega en el rutero.
- Completa en cada `Routes` el `#Stores`, los gastos de viaje, `Visits x Month` y las fórmulas de costo, y asigna el `ROUTE ID GLOBAL`.
- Aprobó su análisis el 2026-10-21 (v1.5).

## Administrador técnico

**Jeronimo Sanchez**, administra el libro. [Inicial]

- Administra el libro en SharePoint, su Power Query y los archivos de la carpeta `Tiendas x FS`. [Dueño]
- ❓ Quién aprueba los accesos nuevos (Q-20).

## Suplente

**Jennifer Guarin.** Aprueba los parámetros del costo y ya tiene acceso al planner; faltan sus accesos a la carpeta y a `DM Costs` y el procedimiento escrito. [Dueño]

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Planner web | Diseñar y descargar rutas | ✅ Tiene acceso |
| Parámetros del costo | Aprobarlos | ✅ Los aprueba |
| Carpeta `Tiendas x FS` | Editar los archivos de cada FS | ⬜ Pendiente (FSR-A01) |
| `DM Costs.xlsx` | Leerlo para el presupuesto | ⬜ Pendiente (FSR-A01) |
| Procedimiento de alta, baja y cambio | Seguirlo sin ayuda | ⬜ Pendiente (FSR-A02) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| `Stores` y `Routes` por FS | Tiendas y rutas diseñadas en el planner; una carpeta por DM y, dentro, una por FS | Dueño | Dueño |
| `Router Test.xlsx` | Consulta de Power Query que une la hoja `Combined` de todos los `Routes` | Dueño | Dueño |
| `Field-Supervisors_home_stores.xlsx` | Tienda base de cada FS | Dueño | Dueño |
| Copia del Store Master (`StoreMaster DSD`) | Jerarquía, coordenadas y dirección; 13 búsquedas por letra de columna | Dueño | Dueño |
| `DM Costs.xlsx` | Presupuesto mensual por FS (`Costs`) | Dueño | Dueño |
| Cotizaciones de viaje | Gastos de viaje de las rutas | La persona que cotiza los viajes | Dueño |

**Cómo se alimenta** [Dueño]

1. Las rutas se diseñan en el planner web: se sube el `Stores`, se diseñan las rutas y se descarga el `Routes`, que se guarda en la carpeta del FS.
2. `Router Test` toma la hoja `Combined` de todos los `Routes` y la une en una tabla.
3. De las 35 columnas del rutero, 14 se copian y pegan desde `Router Test`, 6 se escriben a mano, 13 son búsquedas al Store Master y `#FS` y `Start Time` son fórmulas.
4. **Baja de un FS:** se borran sus archivos y sus filas. **Alta:** se crean sus archivos y rutas, se corre la consulta y se pegan solo las filas del FS nuevo, al final.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | Planner web · SharePoint · Excel con Power Query |
| Archivos | Carpeta `Tiendas x FS` · `Router Test` · `Field-Supervisors_home_stores` · Store Master · `DM Costs` |
| Personas | El dueño y su suplente |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| DSD Route Master | Lee la hoja oculta `C2SFS` como `C2S FS/MILES` | Dueño del DSD Route Master |
| Plan de visitas (Unify) | Su generador lee el costo diario del FS (consulta `CostFS`) | Dueño y suplente |
| FS, DM y RM | Consultan sus rutas y su presupuesto de viaje | — |
| Last Visit y Visit FS ❓ | El inventario los lista como lectores; el dueño no los menciona (Q-19) | PERFORMANCE |

## Procesos operativos

[Dueño] Se actualiza con cada cambio de rutas y con cada alta o baja de FS: 357 versiones en 75 días, casi todas del dueño. ⚠️ C-04

1. **Antes:** confirmar que el FS existe en el Store Master con RM, DM y tiendas; actualizar la copia `StoreMaster DSD`.
2. **Planner:** subir el `Stores` del FS; **escribir `Home Store` y `Home Store (end)` exactamente así** (hoy hay 11 variantes); diseñar y descargar el archivo `MyRouteOnline_…xlsx`.
2b. **Completar y guardar:** renombrarlo `Routes - Apellido, Nombre - (m-d-aaaa).xlsx`, ponerlo en la carpeta del FS y agregar `#Stores`, gastos de viaje (cotizados con la persona que cotiza los viajes), `Visits x Month`, las fórmulas de `Totals` y las 7 columnas de `Combined`.
3. **Consolidar:** actualizar `Router Test` y comparar filas y rutas con el libro.
4. **Pegar:** reemplazar (cambio de ruta) o agregar al final (FS nuevo); **no ordenar la tabla**; construir `ROUTE ID GLOBAL`.
5. **Baja:** borrar archivos y filas; actualizar `Costs`, `DM Costs` y los archivos dependientes.
6. **Revisar:** sin `#N/A` en `STATE`, `Active`, RM, DM o FS; el FS nuevo aparece en `C2SFS` (el Route Master lo lee).
7. **Registrar:** `Last Date Up` y una nota del cambio.
8. **Avisar:** a los dueños de los archivos dependientes.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- Una ruta empieza y termina en la tienda base, y cada tienda está en una sola ruta.
- `Start Time` es la hora de finalización de cada paso; el encabezado dice «inicio» pero es intencional.
- `Milleage` significa «desde la parada anterior» aquí, y «hasta la siguiente» en el Route Master de mercaderistas.
- Los costos se repiten en cada fila de la ruta: sumar la columna cuenta cada gasto varias veces.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Ruta (`ROUTE ID GLOBAL`)** | Un día de trabajo de un FS: sale de la tienda base, visita de 1 a 10 tiendas y regresa. `FS` + estado predominante entre las tiendas + consecutivo del estado (`FSTN001`). Lo creó un generador en la carga masiva (578 de 579 rutas cumplen la regla). Hoy lo asigna el dueño: ruta nueva = estado predominante + último ID del estado + 1; rediseñada = conserva el ID salvo que cambie el estado predominante; eliminada = su número no se reutiliza |
| **Home Store** | Tienda base del FS, donde empieza y termina el día (2 filas por ruta, duración 0) |
| **FFM** | Tienda base especial de 13 rutas de Florida ⚠️ por confirmar |
| **BREAK** | Descanso de 30 minutos que inserta el planner (571 de 579 rutas) |
| **Duration** | 60 minutos por tienda (todas), 30 por `BREAK`, 0 en la tienda base |
| **Frequency x Month** | Veces al mes que se recorre la ruta: 2 (475 rutas), 1 (83), 4 (19), 0,5 (2) |
| **Milleage / Driving Time** | Millas y minutos **desde la parada anterior** (la fila de regreso trae el viaje de vuelta) |
| **Start Time** | **Hora de finalización** de cada paso (7:00 + minutos acumulados); el encabezado dice "inicio" |
| **Cost x Route / Month / Store** | Millas × 0,725 · × visitas al mes (+ viaje) · ÷ n.º de tiendas. Se calcula en cada `Routes` y se pega |
| **Promedio Daily Visit Cost (`C2SFS`)** | Promedio por FS de `COST x Store ÷ 4,3 ÷ 3,75` (Costco `÷ 7`); es el `C2S FS/MILES` del Route Master. Es una consulta que promedia el costo por visita de las rutas de cada FS; los parámetros los aprueba Jennifer Guarin ⚠️ unidad por confirmar |
| **Budget x Month (`Costs`)** | Presupuesto mensual por FS, tomado de `DM Costs.xlsx` |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | Cada ruta MUST empezar y terminar en la tienda base, con `stop` secuencial | Must Have | ✅ 579 de 579 rutas | Dueño |
| FR-02 | Cada tienda activa con FS MUST estar en una sola ruta | Must Have | ❌ 92 sin ruta; 5 rutas con tiendas de 2 FS (FSR-A07, FSR-A21) | Dueño |
| FR-03 | El costo por tienda MUST calcularse con parámetros únicos y documentados | Must Have | ❌ 0,725 escrito en 104 archivos (FSR-A10) | Dueño |
| FR-04 | El libro MUST coincidir con `Router Test` en conteo de filas y rutas | Must Have | ⚠️ 578 de 579; `FSME001` con una fila de más (FSR-A08) | Dueño |
| FR-05 | La copia del Store Master MUST estar al día y leerse por nombre de columna | Must Have | ❌ 32 FS y 34 `Active` distintos; 13 columnas por letra (FSR-A04, FSR-A05) | Dueño |
| FR-06 | Las columnas heredadas MUST completarse o retirarse (`#FS`, `CLUSTER FS`) | Should Have | ❌ `#N/A` en 1.437 filas; vacía en 4.232 (FSR-A06) | Dueño |
| FR-07 | `C2SFS` MUST tener valor para todos los FS | Must Have | ✅ 104 de 104 | Dueño |
| FR-08 | El alta, la baja y el cambio de FS MUST seguir un procedimiento escrito y probado | Must Have | ❌ (FSR-A02) | Dueño |
| FR-09 | Se MUST avisar a los dueños de los archivos dependientes antes de renombrar o mover columnas | Must Have | ❌ Sin regla (FSR-A14) | Dueño |
| FR-10 | Todo cambio MUST ser trazable | Should Have | ❌ Solo versiones de SharePoint (FSR-A16) | Dueño |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Rutas que coinciden con `Router Test` | 578 de 579 | 579 de 579 | Dueño |
| SC-02 | Tiendas activas con ruta, o con motivo documentado | 92 sin ruta | 0 | Dueño |
| SC-03 | Lugares donde viven las constantes del costo | 104 archivos + consulta + `Convertidor plan` | 1 hoja `Parametros` | Dueño |
| SC-04 | Filas con `#N/A` en `#FS` | 1.437 | 0 (columna completada o retirada) | Dueño |
| SC-05 | Hojas ocultas sin lector revisadas y retiradas por etapas | 0 de 3 sin lector · 0 de 3 de la isla | Todas revisadas | Dueño |
| SC-06 | Componentes que opera la suplente | 2 de 5 | 5 de 5 | Dueño · Inicial |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Costos, presupuesto y datos de viaje por FS; exige cuenta y permiso; conexiones a nómina heredadas; falta la lista de permisos | Inicial · Dueño |
| Estabilidad | Alto | El costo se calcula en 104 archivos, el libro se actualiza copiando y pegando sin control, la copia del Store Master está atrás y todo depende de una persona ⚠️ C-06 | Inicial · Dueño |
| Escalabilidad | Medio | 4.232 filas × 35 columnas, 14 consultas (3 en uso) y 60.332 fórmulas heredadas en `old router`; el proceso por FS es manual ⚠️ C-06 | Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🟠 Alta | **El costo por tienda se calcula en 104 archivos distintos y llega pegado como valor.** Cada `Routes` multiplica las millas por **0,725** (escrito en la fórmula), por las visitas al mes y lo divide entre las tiendas. No hay hoja de parámetros: 4,3 semanas, 3,75 y 7 días (Costco) viven en la consulta `CostFS`; 4,34524 en `Convertidor plan`; el Route Master usa 0,76 por milla. Cambiar una constante exige editar 104 archivos. | Dueño |
| R2 | 🟠 Alta | **Copiar y pegar sin ningún control.** Hoy coinciden **578 de las 579 rutas** con `Router Test`; la ruta `FSME001` tiene una fila de más y hay 17 filas con millas y 20 con costo distintos. Nadie avisa cuando el libro se queda atrás. | Dueño |
| R3 | 🟠 Alta | **Columnas heredadas del Route Master que ya no funcionan.** `#FS` vale `#N/A` en **1.437 filas** y `CLUSTER FS` está vacía en las 4.232. Ninguna consulta usa `#FS`. | Dueño |
| R4 | 🟠 Alta | **La copia del Store Master está atrás** (32 tiendas con otro FS, con marcadores `New_FS_…`; 34 con otro `Active`; 3 activas faltan) y se lee **por letra de columna** (13 columnas). | Dueño |
| R5 | 🟠 Alta | **92 tiendas activas sin ruta** (Walmart 40 · Sprouts 39 · Michaels 10 · Costco 3): 30 son de una FS nueva (carpeta con `Stores`, sin `Routes`); 2 no tienen FS. | Dueño |
| R6 | 🟠 Alta | **4 filas con tienda inactiva o inexistente** (RM, DM y FS en 0) y **5 rutas con tiendas de dos FS** (`FSPA009`, `FSTX039`, `FSTX042`, `FSTX061`, `FSCA051`). | Dueño |
| R7 | 🟡 Media | **`Start Time` es la hora de finalización de la visita** (intencional; 3.036 de 3.077 filas comparables), pero el encabezado dice "inicio" y FS, DM y RM lo leen para coordinar sus rutas. Renombrarlo exige cambiar también la consulta `CostFS`. | Dueño |
| R8 | 🟠 Alta | **`Router Test` es un archivo de pruebas que opera como producción:** su consulta lee todo el sitio de SharePoint, tiene 18 columnas escritas a mano y no limpia `Home Store` (11 variantes de la etiqueta). Hay 3 FS con `Routes` fechados en 2025. | Dueño |
| R9 | 🟠 Alta | **Hojas y consultas heredadas.** 9 de 11 hojas ocultas; solo 3 de 14 consultas alimentan algo en uso. Cuatro leen una tabla `RouteMaster` que ya no existe aquí, y `old router` pesa 60.332 fórmulas. El libro se construyó **duplicando el Route Master**, por eso están. Las que no se usan para nada se podrían borrar, pero el dueño quiere **revisarlas con detalle antes** (sin editar el archivo): de las 9 ocultas, **3 no tienen ningún lector** (`old router`, `MC`, `ST-RATE`), **3 forman una isla** sin lectores externos (`C2S`, `FS Cost`, `Dm Cost`) y **3 se usan** (`StoreMaster DSD`, `C2SFS`, `FS-CLUSTER`). Detalle y orden de borrado en el Anexo B del documento completo. | Dueño |
| R10 | 🟡 Media | **El vínculo a la copia local (`DSD Route Master copy Sep16.xlsx`) solo lo usa la hoja oculta `old router`.** El costo no depende de él: se pueden convertir esas 285 fórmulas en valores o dejarlo documentado, sin borrar la hoja. Esto cierra el pendiente del análisis del Route Master. | Dueño |
| R11 | 🟡 Media | **Dos significados de `Milleage`** (aquí *desde* la parada anterior; en el Route Master de mercaderistas, *hasta* la siguiente) y **costos repetidos en cada fila** de la ruta: sumar la columna cuenta cada gasto varias veces. | Dueño |
| R12 | 🟠 Alta | **Todo depende de una persona:** 356 de 357 versiones; el flujo no está escrito. La cuenta del planner la paga Falcon y la usan Jennifer Guarin, Jeronimo Sanchez y otras personas, así que el acceso no es el riesgo. | Dueño |
| R13 | 🟡 Media | **El libro conserva conexiones a nómina** (`Salary`, `Table2`) y hojas de costo por salario (`FS Cost`, `Dm Cost`) que son restos del Route Master. Aquí el costo del FS no usa salarios. | Dueño |
| R14 | 🟠 Alta | Contiene costos, presupuesto y datos de viaje por supervisor, y la lista de permisos no está revisada (Q-20) | Inicial |
| R15 | 🟡 Media | Si Last Visit y Visit FS leen este libro, un cambio de columnas los rompería sin aviso (Q-19) | Inicial |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Actualizar la copia del Store Master, corregir rutas y filas con error, y completar o retirar `#FS` y `CLUSTER FS` | Datos al día y sin errores | FSR-A05, FSR-A06, FSR-A07, FSR-A08 | Dueño |
| Corto plazo | Hoja `Parametros` con el costo calculado en el libro; convención de nombres y fechas; `Router Test` como archivo de producción; diccionario y registro de cambios | Un solo lugar para las constantes y trazabilidad | FSR-A10, FSR-A11, FSR-A12, FSR-A15, FSR-A16 | Dueño |
| Mediano plazo | Borrar por etapas las piezas heredadas, con copia previa, y quitar las conexiones a nómina | Libro más liviano y claro | FSR-A09, FSR-A20 | Dueño |
| Largo plazo | Cargar sin copiar y pegar, evaluar una base de datos y agregar validaciones y protección | Menos trabajo manual y datos validados | FSR-A22, FSR-A23, FSR-A24 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| FSR-A01 | Verificar accesos de Jennifer Guarin a los archivos | P0 | Dueño y suplente | Dueño | T-001 |
| FSR-A02 | Escribir y probar el procedimiento de alta, baja y cambio | P0 | Dueño | Dueño | T-003 |
| FSR-A03 | Quitar la dependencia de la copia local | P0 | Dueño | Dueño | T-005 |
| FSR-A04 | Búsquedas por nombre de columna | P0 | Dueño | Dueño | T-004 |
| FSR-A05 | Actualizar `StoreMaster DSD` | P0 | Dueño | Dueño | T-006 |
| FSR-A06 | `#FS` y `CLUSTER FS` | P0 | Dueño | Dueño | T-007 |
| FSR-A07 | 4 filas y 5 rutas con 2 FS | P0 | Dueño | Dueño | T-008 |
| FSR-A08 | Control de conteo contra `Router Test` y corregir `FSME001` | P0 | Dueño | Dueño | T-009 |
| FSR-A09 | Borrar las piezas heredadas por etapas (Anexo B), con copia previa | P0 | Dueño | Dueño | T-010 |
| FSR-A10 | Hoja `Parametros` y costo calculado en el libro | P1 | Dueño | Dueño | T-011 |
| FSR-A11 | Convención de nombres y fechas; `Home Store` | P1 | Dueño | Dueño | T-012 |
| FSR-A12 | `Router Test` como archivo de producción | P1 | Dueño | Dueño | T-013 |
| FSR-A13 | Regla del `ROUTE ID GLOBAL` | P1 | Dueño | Dueño | T-014 |
| FSR-A14 | Encabezado de `Start Time` (junto con `CostFS`) | P1 | Dueño | Dueño | T-015 |
| FSR-A15 | Diccionario | P1 | Dueño | Dueño | T-016 |
| FSR-A16 | Registro de cambios | P1 | Dueño | Dueño | T-017 |
| FSR-A17 | Convención de carpetas | P1 | Dueño | Dueño | T-018 |
| FSR-A18 | Cadena de costos de viaje | P1 | Dueño | Dueño | T-019 |
| FSR-A19 | Aviso sobre `Milleage` | P1 | Dueño | Dueño | T-020 |
| FSR-A20 | Quitar conexiones a nómina | P1 | Dueño | Dueño | T-021 |
| FSR-A21 | Rutas de una FS nueva y 62 tiendas | P1 | Dueño | Dueño | T-022 |
| FSR-A22 | Cargar sin copiar y pegar | P2 | Dueño | Dueño | T-023 |
| FSR-A23 | Evaluar base de datos | P2 | Dueño | Dueño | T-024 |
| FSR-A24 | Validaciones y protección | P2 | Dueño | Dueño | T-025 |
| FSR-A25 | Documentar el planner | P2 | Dueño | Dueño | T-026 |
| FSR-A26 | Audiencia de `Costs` (Q-17) | P2 | Dueño | Dueño | T-027 |
| FSR-A27 | Confirmar si Last Visit y Visit FS leen este libro y, si no, corregir el inventario | P1 | Dueño y PERFORMANCE | Inicial | C-03 |
| FSR-A28 | Revisar la lista de personas con acceso al libro y a la carpeta, y quién aprueba los accesos nuevos | P1 | Dueño e IT | Inicial | Q-20 |
| FSR-A29 | Hacer la revisión técnica con IT: costos y presupuesto por FS y conexiones a nómina | P1 | IT | Inicial | — |
| FSR-A30 | Guardar esta spec, las consultas de Power Query y las fórmulas del costo en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| FSR-A31 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-06 | `FFM` | Dueño (se resuelve con su tarea) | Dueño |
| Q-06b | fuente de la tienda base | Dueño (se resuelve con su tarea) | Dueño |
| Q-07 | `#FS`, `FS-CLUSTER` y `CLUSTER FS` | Dueño (se resuelve con su tarea) | Dueño |
| Q-08 | archivos `Total Costs`, `Travel Monthly Budget` y `Convertidor plan` | Dueño (se resuelve con su tarea) | Dueño |
| Q-09 | `Routes` de 2025 | Dueño (se resuelve con su tarea) | Dueño |
| Q-10 | `Visits x Month` 0,5 y 4 | Dueño (se resuelve con su tarea) | Dueño |
| Q-11 | tiendas sin ruta | Dueño (se resuelve con su tarea) | Dueño |
| Q-12 | conexiones a nómina | Dueño (se resuelve con su tarea) | Dueño |
| Q-13 | nombre de `Router Test` | Dueño (se resuelve con su tarea) | Dueño |
| Q-16 | constantes de costo distintas entre libros y unidad de `Promedio Daily Visit Cost` | Dueño (se resuelve con su tarea) | Dueño |
| Q-17 | audiencia del presupuesto por FS (`Costs`) | Dueño (se resuelve con su tarea) | Dueño |
| Q-18 | frecuencia y registro de las cotizaciones de viaje de la persona que cotiza los viajes | Dueño (se resuelve con su tarea) | Dueño |
| Q-19 | ¿Last Visit y Visit FS leen este libro, o solo el DSD Route Master? | Dueño y PERFORMANCE | Inicial |
| Q-20 | ¿Quiénes tienen acceso al libro y a la carpeta, y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Hojas visibles y ocultas | Inicial: 4 visibles y 7 ocultas. Dueño: 11 hojas, 9 ocultas | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-02 | Tamaño | Inicial: ≈ 4.177 filas × 35 columnas. Dueño: 4.232 filas × 35 (versión 358.0) | Lo del dueño; el archivo cambió | ✅ Resuelta a favor del dueño |
| C-03 | Quién lo lee | Inicial (inventario): Last Visit y Visit FS. Dueño: el DSD Route Master (`C2S FS/MILES`); FS, DM y RM lo consultan | Lo del dueño; confirmar con PERFORMANCE (Q-19) | ❓ Por confirmar |
| C-04 | Frecuencia | Inicial: según la necesidad. Dueño: 357 versiones en 75 días | Cada cambio de rutas o de FS; casi diaria | ✅ Resuelta a favor del dueño |
| C-05 | Relación con Isolved y AFS | Inicial: sus campos sugieren relación con esos sistemas. Dueño: las conexiones a nómina son restos del Route Master; el costo del FS no usa salarios | Lo del dueño; retirar las conexiones (FSR-A20) | ✅ Resuelta a favor del dueño |
| C-06 | Nivel de riesgo | Inicial: estabilidad «Medio» y escalabilidad «Bajo». Dueño: costo en 104 archivos, copiar y pegar sin control, copia del Store Master atrás, 9 hojas ocultas y una sola persona | Estabilidad «Alto» y escalabilidad «Medio» | ❓ Por confirmar |
| C-07 | Cómo se alimenta | Inicial: por confirmar si es manual. Dueño: 14 columnas pegadas desde `Router Test`, 6 a mano y 13 búsquedas al Store Master | Lo del dueño | ✅ Resuelta a favor del dueño |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, inventario de consultas y fórmulas, calidad de datos, y la revisión de hojas y consultas heredadas con su orden de borrado) todavía no están integrados.
- La distribución de filas por DM y FS está en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/dsd-fs-route-master/spec.md`. [Inicial]
- Incluir el código de las consultas de Power Query de `Router Test` y las fórmulas del costo, sin datos de FS ni de tiendas. [Dueño · Inicial]
- Mantener en el mismo repositorio la hoja de parámetros del costo (0,725, semanas y días) y su historial de cambios. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Modelar rutas y pasos como tablas (ruta, paso, FS, tienda), con clave `ROUTE ID GLOBAL` más `stop`, y calcular el costo en SQL desde una tabla de parámetros (FSR-A10). [Dueño · Inicial]
2. Cargar los `Routes` con un proceso programado en lugar de copiar y pegar (FSR-A22). [Dueño]
3. Leer la jerarquía del Store Master por nombre de columna o desde la réplica SQL, no desde una copia (FSR-A04, FSR-A05). [Dueño · Inicial]
4. Exponer `C2SFS` como una vista con el nombre `C2S FS/MILES` para el DSD Route Master. [Dueño]
5. Retirar primero las piezas heredadas (FSR-A09) y migrar solo lo que se usa. [Dueño]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 3 | Dueño y suplente definidos; la suplente aprueba el costo y le faltan accesos |
| Operación documentada | 2 | Lista de verificación propuesta; el flujo no estaba escrito |
| Control de acceso | 3 | Cuenta y permiso; lectura para FS, DM y RM |
| Contrato de datos | 1 | Sin diccionario; encabezados engañosos; lectura por letra de columna |
| Calidad y validación | 2 | 578 de 579 rutas coinciden; `#N/A` en 1.437 filas |
| Automatización e integración | 2 | Consulta de Power Query, pero las columnas se pegan a mano |
| Trazabilidad de cambios | 1 | Solo versiones de SharePoint |
| Entornos y pruebas | 1 | `Router Test`, un archivo de pruebas, opera como producción |

**Nivel global: 2,0 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.
