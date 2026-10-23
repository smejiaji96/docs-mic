# Spec · DSD Route Master

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m20 (inventario MIC) |
| Tipo | Base de datos: libro de Excel (catálogo de rutas de merchandising DSD y cálculo del costo de servir) con Power Query |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Catálogo de las rutas de merchandising DSD de Walmart, Sprouts y Costco, más el cálculo del **costo de servir** de cada ruta. Las rutas se crean, editan y analizan en App Routes; el Route Master las guarda y las publica. Execution Team y todos los FS, DM y RM lo consultan en modo lectura; solo el dueño y su co-responsable lo editan. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 3.664 filas (3.221 paradas + 443 `BREAK`) × 49 columnas ⚠️ C-02 | Dueño |
| Cobertura | 2.416 tiendas: Walmart 1.813 · Sprouts 512 · Costco 91. Michaels (173 tiendas) no está todavía: entrará en 2 a 4 meses | Dueño |
| Rutas | 1.305 Route ID · 1.060 Global ID · 105 Cluster FS | Dueño |
| Jerarquía | 4 RMs · 14 DMs · 105 FS | Dueño |
| Costo de servir | 1.301 rutas: 1.003 `MultiStore` + 298 `OUTLIER` | Dueño |
| Libro | 10 hojas (8 ocultas) · 12 consultas de Power Query · 5 vínculos externos ⚠️ C-01 | Dueño |
| Actividad | 500 versiones en 42 días: dueño 368 · co-responsable 132 ⚠️ C-05 | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Medio ⚠️ C-07 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🔴 **Los supuestos del costo de servir están escritos dentro de las consultas y sin documentar:** 0,76 USD por milla, visitas por semana, cargas por cliente, gastos generales y umbrales. [Dueño]
2. 🔴 **Las fórmulas buscan en el Store Master por letra de columna:** una columna nueva en medio desplazaría los datos sin dar error. [Dueño]
3. 🟠 **Un filtro guardado oculta 3.659 de 3.664 filas,** más 9 columnas y 8 hojas ocultas. [Dueño]
4. 🟠 **`FS-CLUSTER` ya no coincide con el Store Master** (`#FS` vale 0 en 345 paradas) y hay 3 columnas con `#REF!`. [Dueño]
5. 🟠 **Dependencias personales:** dos vínculos al OneDrive de la suplente y uno a una copia local. [Dueño]
6. ⚠️ **El inventario lo daba como leído por Last Visit y Visit FS;** el dueño menciona otros lectores (C-04). [Inicial]

**Funciona bien:** **Rutas y jerarquía:** ninguna ruta tiene dos FS; RM, DM y FS coinciden al 100 % con el Store Master; todas las tiendas con ruta existen en el Store Master. **IDs y datos de cada parada:** los IDs cumplen el patrón en las 3.664 filas; todas las paradas tienen días de servicio y coordenadas válidas. **Actualización y control:** la copia del Store Master está al día (solo 2 Sprouts activadas hoy difieren) y el control `CHECK` marca OK 1.298 de 1.301 rutas. **Respaldo:** ambos co-responsables pueden editar. [Dueño]

**Contradicciones:** 7 detectadas; 5 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (DRM-A01, DRM-A02, DRM-A03, DRM-A04, DRM-A05, DRM-A06, DRM-A07, DRM-A08, DRM-A09, DRM-A33) y las preguntas Q-19 y Q-20. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Tener en un solo lugar el catálogo de las rutas de merchandising DSD y el costo de servir de cada ruta, para que Execution Team y los FS, DM y RM consulten las rutas aprobadas.

- **Problema que resuelve:** las rutas se analizan en App Routes y necesitan un catálogo oficial, con su costo, que otros archivos puedan leer. [Dueño]
- **Qué logra:** una fila por parada con ruta, orden, tienda, frecuencia, minutos de visita, millas, manejo, mercaderista y tarifa, más el costo de servir por ruta. [Dueño]
- **Éxito:** los supuestos del costo están documentados, ninguna columna cambia sin aviso y todas las rutas se calculan (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: solo el Route Master (catálogo de rutas y cálculo del costo de servir).

**No incluye** [Dueño]: el Store Master (ya tiene su análisis); el DSD FS Route Master (tiene el suyo); App Routes, Route Studio, las copias y los pilotos, que son herramientas aparte.

**Futuro** [Dueño]: incluir Michaels en rutas existentes (DRM-A20, DRM-A11), protección de hoja (DRM-A27) y evaluar una base de datos (DRM-A28).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Co-responsables (el dueño y su suplente) | Analizan, aprueban y editan el libro; ambos tienen la contraseña de escritura | 368 y 132 versiones | Dueño |
| Execution Team, FS, DM y RM | Consultan las rutas en modo lectura | — | Dueño |
| Aprobadores de los supuestos del costo | Otra persona del equipo y la suplente | — | Dueño |
| Dueños de archivos que lo copian o leen | DSD FS Route Master, DSD Route Master Copy, DSD Michaels Router Pilot y el análisis de incidentes | 4 archivos | Dueño |

**Acceso**

- Está en SharePoint › DSD Business Analysis › DSD Data Master, con permisos propios. [Dueño]
- Exige cuenta de la empresa y permiso. [Inicial · Dueño]
- Todos los FS, DM y RM abren el libro y las hojas ocultas de costo no están protegidas. [Dueño]
- ❓ Falta la lista de personas con acceso, quién aprueba los accesos nuevos y a quién se deben mostrar las hojas de costo por FS y DM (Q-20, DRM-A12). [Inicial · Dueño]

## Dueño funcional

**Jeronimo Sanchez**, co-responsable. [Dueño · Inicial]

- Analiza las propuestas de cambio en App Routes y edita el Route Master.
- Avisa al FS, DM y RM cuando se aprueba un cambio.
- Aprobó su análisis el 2026-10-21 (v1.3).

## Administrador técnico

**Jeronimo Sanchez**, administra el libro. [Inicial]

- Administra el libro en SharePoint, sus 12 consultas de Power Query y sus 5 vínculos externos. [Dueño]
- ❓ Quién aprueba los accesos nuevos (Q-20).

## Suplente

**Jennifer Guarin.** Es co-responsable: cada uno respalda al otro. Ella analiza los costos y las variables, **aprueba o no** el cambio y cubre al dueño; tiene la contraseña de escritura. [Dueño] ⚠️ C-03

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Libro y contraseña de escritura | Editar el libro | ✅ Edita cuando es necesario |
| Aprobación de rutas y de supuestos del costo | Aprobar | ✅ Aprueba |
| Archivos en su OneDrive (cambio de ABC y organigrama) | Estar en una carpeta compartida | ⬜ Pendiente (DRM-A01) |
| Permisos del libro | Verificarlos | ⬜ Pendiente (DRM-A01) |
| Flujo de cambio de ruta | Seguir un procedimiento escrito | ⬜ Pendiente (DRM-A10) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| App Routes (`Route_Analysis.xlsx`) | Rutas, orden, frecuencia, millas, manejo y `BREAK` (traspaso manual, por confirmar) | PERFORMANCE | Dueño |
| DSD Store Master | Jerarquía, zona, coordenadas y dirección (consulta de Power Query y búsquedas por letra de columna) | Dueño | Dueño |
| Requis ID Book | ID de iSolved y de requisición | Otro equipo | Dueño |
| Stores Contact List | Correos y teléfonos de RM, DM y FS | Dueño | Dueño |
| Cambio de ABC en Sprouts y organigrama DSD | Archivos en el OneDrive de la suplente | Suplente | Dueño |
| DSD FS Route Master | Costo por milla del FS (`C2S FS/MILES`) | Dueño | Dueño |
| Archivo de salarios (sitio PG) | Salario por FS y DM para el costo | Otro equipo | Dueño |
| Escritos en el libro | Duración de visita, mercaderista y tarifa | Co-responsables | Dueño |

**Cómo se cambia una ruta (todo por correo)** [Dueño]

1. Un FS o DM (a veces un RM) pide el cambio a los dos co-responsables.
2. El dueño analiza la propuesta en App Routes y comparte el archivo exportado.
3. La suplente analiza costos y variables y **aprueba o no**.
4. Si aprueba, el dueño cambia el Route Master y **avisa al FS, DM y RM**.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | App Routes (con el servicio público OSRM) · SharePoint · Excel con Power Query |
| Archivos | Store Master · DSD FS Route Master · Requis ID Book · Stores Contact List · archivos del OneDrive de la suplente · archivo de salarios |
| Personas | Los dos co-responsables · los aprobadores de los supuestos del costo |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| DSD FS Route Master | Su costo por milla lo lee el Route Master (`C2S FS/MILES`) y el libro apunta a una copia local de este | Dueño |
| Plan de visitas (Unify) | Su generador lee la hoja `RouteMaster` | Dueño y suplente |
| Stores Contact List | Lee la dirección de la hoja `StoreMaster DSD`; el Route Master le lee los contactos (dependencia cruzada) | Dueño |
| DSD Route Master Copy y DSD Michaels Router Pilot | Copian el libro | Dueño |
| Análisis de incidentes | Usa los IDs de ruta | Execution Team |
| Last Visit y Visit FS ❓ | El inventario los lista como lectores; el dueño no los menciona (Q-19) | PERFORMANCE |

## Procesos operativos

[Dueño] Cada vez que se crea o cambia una ruta, o cambia un supuesto del costo: 500 versiones en 42 días. ⚠️ C-05

1. **Antes de editar:** quitar el filtro de la tabla (hoy `GNJ002`) o usar una Vista de hoja personal.
2. **Ruta nueva o cambiada:** analizarla en **App Routes** (plan A vs B, costo, millas y manejo con OSRM, `BREAK` automático) y esperar la **aprobación de Jennifer Guarin**. Luego agregar o actualizar las filas **dentro** de la tabla con los 3 IDs, `stop` secuencial, tienda, frecuencia, duración, millas, manejo, mercaderista y tarifa.
3. **Cambio de orden o de tienda:** actualizar `stop`, millas y manejo de toda la ruta. **No ordenar la tabla:** `Start Time` depende de la fila de arriba.
4. **Cambio de frecuencia o duración:** actualizar **primero el Store Master** (`Merch Days`, `Merch Visit Duration`, que es quien manda) y después el Route Master.
5. **FS nuevo o cambio de FS:** actualizar `FS-CLUSTER` (a mano) y el costo del FS.
6. **Registrar el cambio** en `Observation` y `Last Date Up`.
7. **Actualizar las consultas** y revisar que no haya `0`, `#N/A` ni `#REF!` en RM, DM, FS o `#FS`.
8. **Antes de guardar:** sin filtros ni filas ocultas. **Después:** avisar por correo al **FS, DM y RM** afectados y a los dueños de los archivos dependientes.
9. **Cambios de columnas:** avisar antes. Agregar una columna al final del Store Master o del Route Master es seguro; insertarla en medio, no.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- El Store Master manda sobre `Merch Days` y `Merch Visit Duration`: cuando una ruta cambia, primero se actualiza el Store Master.
- Despejar el salario de cada FS es intencional: así se calcula el FS Cost.
- Se usan dos modelos de costo a propósito (App Routes y Route Master); falta medir cuánto se separan.
- Agregar una columna al final del Store Master o del Route Master es seguro; insertarla en medio, no.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Parada (fila)** | Una visita planeada a una tienda dentro de una ruta. Una tienda puede tener varias filas (642 de 2.416) |
| **Route ID / Global Route ID / Cluster FS** | `R` / `G` / `C` + estado + 3 dígitos. Route ID = ruta de un FS; Cluster FS = agrupación por FS. ⚠️ Falta definir la diferencia entre Global y Route ID (Q-07) |
| **stop** | Número de la parada dentro de la ruta; la parada 1 abre a las 7:00 |
| **Frequency / Duration** | Días de visita (`MO-WE-FR-SA`) y minutos de visita (45 a 240; 60 min en 47 % de las paradas) |
| **MO … SU** | Minutos de cada día: `Duration` si el día está en `Frequency` |
| **Milleage / Driving Time** | Millas y minutos de manejo **hasta la siguiente parada**; la última parada de la ruta tiene 0. Los calcula App Routes con OSRM |
| **BREAK** | Descanso del mercaderista: App Routes lo inserta (30 min) cuando el tiempo acumulado supera 240 min (443 filas, 35 estados) |
| **RATE** | Tarifa del mercaderista: por hora (rutas de varias tiendas) o por visita (rutas de una tienda) |
| **MultiStore / OUTLIER** | `OUTLIER` = `RATE` ≥ 35 (ruta de una sola tienda pagada por visita) ⚠️ por confirmar |
| **Cargas** | **Cargas parafiscales** que se tienen en cuenta en el costo de servir. Factor por cliente: Walmart 1,13 · Sprouts 1,23 · Costco 1,14 (en App Routes, un 1,18 único) |
| **Cost to Serve** | Costo por parada = mercaderista + FS + DM + gastos generales + costo por milla del FS. `MultiStore`: `(((servicio + manejo) ÷ 60 × tarifa) + millas × 0,76) ÷ paradas` |
| **FS$ / DM$** | Salario anual × 1,18 ÷ (tiendas × visitas por semana × 52); es el FS Cost |
| **Tip** | `Active` del Store Master (Y activa, P pendiente) |
| **#FS** | Número consecutivo del FS en la hoja `FS-CLUSTER` |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | Cada parada MUST tener los 3 IDs de ruta, `stop` secuencial, tienda, frecuencia, duración, millas y manejo | Must Have | ✅ Los IDs cumplen el patrón en las 3.664 filas | Dueño |
| FR-02 | Ninguna ruta MUST tener dos FS, y RM, DM y FS MUST coincidir con el Store Master | Must Have | ✅ 100 % | Dueño |
| FR-03 | Los supuestos del costo MUST estar en una hoja visible `Parametros` con valor, fecha y aprobador | Must Have | ❌ Escritos dentro de las consultas (DRM-A03) | Dueño |
| FR-04 | Las búsquedas al Store Master MUST hacerse por referencia de tabla, no por letra de columna | Must Have | ❌ (DRM-A04) | Dueño |
| FR-05 | El libro MUST abrirse sin filtros, filas ocultas ni `#REF!` | Must Have | ❌ El filtro oculta 3.659 de 3.664 filas; 3 columnas con `#REF!` (DRM-A05, DRM-A08) | Dueño |
| FR-06 | `#FS` y `FS-CLUSTER` MUST coincidir con el Store Master | Must Have | ❌ `#FS` = 0 en 345 paradas (DRM-A07) | Dueño |
| FR-07 | `RATE` MUST tener una sola unidad, y las rutas «Third parties» MUST decidirse | Must Have | ❌ Tres unidades; 4 rutas no entran al costo (DRM-A13) | Dueño |
| FR-08 | Los vínculos MUST apuntar a carpetas compartidas, no a archivos personales | Must Have | ❌ 2 al OneDrive de la suplente y 1 a una copia local (DRM-A01, DRM-A06) | Dueño |
| FR-09 | `Frequency` y `Duration` MUST seguir al Store Master | Should Have | ⚠️ 10 y 48 tiendas distintas (DRM-A17) | Dueño |
| FR-10 | El flujo de un cambio de ruta MUST tener identificador y registro | Should Have | ❌ Solo vive en correos (DRM-A10, DRM-A19) | Dueño |
| FR-11 | Se MUST avisar antes de renombrar, borrar o mover columnas | Must Have | ❌ Sin regla (DRM-A14, DRM-A21) | Dueño |
| FR-12 | Michaels MUST poder incluirse sin que el costo quede vacío | Should Have | ⚠️ Falta su factor en `Cargas` (DRM-A11) | Dueño |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Filas visibles al abrir el libro | 5 de 3.664 | 3.664 de 3.664 | Dueño |
| SC-02 | Columnas con `#REF!` | 3 | 0 | Dueño |
| SC-03 | Paradas con `#FS = 0` | 345 | 0 | Dueño |
| SC-04 | Lugares donde viven los supuestos del costo | Dentro de las consultas | Una hoja `Parametros` | Dueño |
| SC-05 | Rutas con el control `CHECK` en OK | 1.298 de 1.301 | 1.301 de 1.301 | Dueño |
| SC-06 | Vínculos a archivos personales o copias locales | 3 | 0 | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Tarifas, costos por supervisor y contactos del personal; todos los FS, DM y RM abren el libro y las hojas de costo no están protegidas; falta la lista de permisos | Inicial · Dueño |
| Estabilidad | Alto | Supuestos del costo sin documentar, búsquedas por letra de columna, `#REF!`, dependencias personales y poco historial ⚠️ C-07 | Inicial · Dueño |
| Escalabilidad | Medio | 3.664 filas × 49 columnas, 12 consultas (4 sin uso) y una tabla dinámica oculta con 23.587 registros viejos; Michaels aún no tiene su factor | Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🔴 Crítica | **Los supuestos del costo de servir están escritos dentro de las consultas y sin documentar.** 0,76 USD por milla, 3,74 / 3,78 / 14 visitas por semana, cargas parafiscales por cliente (1,13 / 1,23 / 1,14), un 1,18 sobre el salario, un salario por defecto, gastos generales de 5 o 13 y los umbrales 35 y 55. Los aprueban otra persona del equipo y Jennifer Guarin. **Despejar el salario de cada FS es intencional** (así se calcula el FS Cost); el riesgo que queda es que todos los FS, DM y RM abren el libro y las hojas ocultas no están protegidas. | Dueño |
| R2 | 🟡 Media | **Se usan dos modelos de costo a propósito.** App Routes: 0,725 por milla, multiplicador 1,18, FS 15 y DM 3,4 por parada, cargo fijo 5. Route Master: 0,76, cargas por cliente, FS y DM por salario, gasto general 5 o 13. El dueño dice que dan resultados muy aproximados; falta medir cuánto se separan. | Dueño |
| R3 | 🟠 Alta | **Los archivos se leen en círculo.** El Route Master lee `C2S FS/MILES` de una hoja del DSD FS Route Master, y ese archivo apunta a una **copia local** (la carpeta Descargas del dueño). Se resolverá en el análisis del DSD FS Route Master. | Dueño |
| R4 | 🔴 Crítica | **Las fórmulas buscan en el Store Master por letra de columna** (`B`, `BC`, `BI`, `BW`, `BY`…). Una columna nueva en medio del Store Master desplazaría los datos **sin dar error**. **Regla: agregar columnas solo al final y avisar antes de renombrar o borrar.** | Dueño |
| R5 | 🟠 Alta | **Un filtro guardado oculta 3.659 de 3.664 filas** (`ROUTE ID GLOBAL = GNJ002`), más 9 columnas y 8 hojas ocultas. | Dueño |
| R6 | 🟠 Alta | **`FS-CLUSTER` (escrita a mano) ya no coincide con el Store Master:** 57 de 93 `# STORE` difieren y 12 FS no están. Por eso `#FS` vale 0 en **345 paradas**. | Dueño |
| R7 | 🟠 Alta | **Tres columnas rotas (`#REF!`)** de un cambio de ABC en Sprouts (julio 2026): `ABC New` (3.637 celdas), `New Time` y `Validacion` (561 cada una). | Dueño |
| R8 | 🟠 Alta | **Dependencias personales:** dos vínculos van al OneDrive de Jennifer Guarin y los contactos de RM, DM y FS se copian de `Stores Contact List` en vez de salir del Store Master. | Dueño |
| R9 | 🟠 Alta | **`RATE` mezcla tres unidades** (por hora 15,5–20, por visita 35–50 y el texto "Third parties"). Las 4 rutas "Third parties" de Costco **no entran al costo** y nada lo avisa. | Dueño |
| R10 | 🟠 Alta | **Poco historial y ningún registro de cambios:** 500 versiones (≈ 2 meses), texto libre en `Observation` (34 %) y un flujo de solicitud, aprobación y aviso que solo vive en correos, sin identificador. | Dueño |
| R11 | 🟡 Media | **Pesa de más:** tabla dinámica oculta con 23.587 registros viejos y 4 consultas sin uso. | Dueño |
| R12 | 🟠 Alta | **Michaels llega en 2 a 4 meses y la tabla `Cargas` no tiene su factor.** Sin él, el costo de esas paradas quedaría vacío o incompleto. Hay que probar las consultas con ese cliente antes de incluirlo. | Dueño |
| R13 | 🟡 Media | **`Frequency` y `Duration` no siguen al Store Master, que es quien manda** sobre `Merch Days` y `Merch Visit Duration` (10 y 48 tiendas distintas). Cuando una ruta cambia, primero se actualiza el Store Master. | Dueño |
| R14 | 🟠 Alta | Contiene tarifas, costos y contactos del personal, y la lista de permisos no está revisada (Q-20) | Inicial |
| R15 | 🟡 Media | Si Last Visit y Visit FS leen este libro, un cambio de columnas los rompe sin aviso (Q-19) | Inicial |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Hoja visible `Parametros`, referencias de tabla, reparar `#REF!`, completar `FS-CLUSTER`, quitar el filtro y los vínculos personales y corregir los datos | Costo documentado y libro sin errores | DRM-A03, DRM-A04, DRM-A05, DRM-A06, DRM-A07, DRM-A08, DRM-A09 | Dueño |
| Corto plazo | Documentar el flujo de un cambio de ruta, preparar Michaels, regla de cambio de columnas, `RATE` en tipo y valor, alinear `Frequency` y `Duration`, diccionario y registro de cambios | Menos sorpresas y trazabilidad | DRM-A10, DRM-A11, DRM-A14, DRM-A13, DRM-A17, DRM-A18, DRM-A19 | Dueño |
| Mediano plazo | Incluir Michaels en rutas existentes, avisos a los dueños dependientes y catálogo de IDs | Cobertura completa y sin roturas | DRM-A20, DRM-A21, DRM-A16 | Dueño |
| Largo plazo | Limpiar consultas y pivote, retirar copias, documentar los dos modelos de costo, protección de hoja y evaluar una base de datos | Libro liviano y validado | DRM-A23, DRM-A24, DRM-A25, DRM-A27, DRM-A28 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| DRM-A01 | Verificar permisos de ambos co-responsables y pasar a la carpeta compartida los archivos del OneDrive de Jennifer | P0 | Dueño y suplente | Dueño | T-001 |
| DRM-A02 | Publicar este resumen y el diccionario junto al libro | P0 | Dueño | Dueño | T-002 |
| DRM-A03 | Hoja visible `Parametros` con todos los supuestos del costo (valor, fecha, aprobador) | P0 | Dueño | Dueño | T-003 |
| DRM-A04 | Reemplazar las búsquedas por letra de columna por referencias de tabla | P0 | Dueño | Dueño | T-004 |
| DRM-A05 | Reparar o borrar `#REF!` | P0 | Dueño | Dueño | T-006 |
| DRM-A06 | Quitar vínculos a archivos personales | P0 | Dueño | Dueño | T-007 |
| DRM-A07 | Completar `FS-CLUSTER` | P0 | Dueño | Dueño | T-008 |
| DRM-A08 | Quitar filtro guardado y ocultos | P0 | Dueño | Dueño | T-010 |
| DRM-A09 | Corregir fechas, `stop` y la celda con fórmula | P0 | Dueño | Dueño | T-011 |
| DRM-A10 | Documentar el flujo de un cambio de ruta (plantilla de correo e identificador por solicitud) | P1 | Dueño | Dueño | T-026 |
| DRM-A11 | Preparar Michaels: factor en `Cargas` y pruebas de las consultas | P1 | Dueño | Dueño | T-027 |
| DRM-A12 | Revisar la audiencia del libro y proteger las hojas de costo por FS y DM si se decide | P1 | Dueño | Dueño | T-009 |
| DRM-A13 | Separar `RATE` en tipo y valor; resolver "Third parties" | P1 | Dueño | Dueño | T-012 |
| DRM-A14 | Regla de cambio de columnas | P1 | Dueño | Dueño | T-013 |
| DRM-A15 | `Start Time` sin depender del orden | P1 | Dueño | Dueño | T-014 |
| DRM-A16 | Catálogo de IDs | P1 | Dueño | Dueño | T-015 |
| DRM-A17 | Alinear Frequency y Duration con el Store Master (que manda) | P1 | Dueño | Dueño | T-016 |
| DRM-A18 | Diccionario y validaciones | P1 | Dueño | Dueño | T-017/T-018 |
| DRM-A19 | Registro de cambios | P1 | Dueño | Dueño | T-019 |
| DRM-A20 | Incluir Michaels en rutas existentes (2 a 4 meses) | P1 | Dueño | Dueño | T-020 |
| DRM-A21 | Avisos a dueños de archivos dependientes | P1 | Dueño | Dueño | T-022 |
| DRM-A22 | Vínculo de FS Route Master (en su propio análisis) | P1 | Dueño | Dueño | T-005 |
| DRM-A23 | Limpiar consultas y pivote | P2 | Dueño | Dueño | T-021 |
| DRM-A24 | Retirar copias | P2 | Dueño | Dueño | T-023 |
| DRM-A25 | Documentar los dos modelos de costo y medir su diferencia | P2 | Dueño | Dueño | T-025 |
| DRM-A26 | Documentar Route Studio | P2 | Dueño | Dueño | T-028 |
| DRM-A27 | Protección de hoja | P2 | Dueño | Dueño | T-033 |
| DRM-A28 | Evaluar una base de datos | P2 | Dueño | Dueño | T-040 |
| DRM-A29 | Confirmar si Last Visit y Visit FS leen este libro y, si no, corregir el inventario | P1 | Dueño y PERFORMANCE | Inicial | C-04 |
| DRM-A30 | Revisar la lista de personas con acceso al libro y quién aprueba los accesos nuevos | P1 | Dueño e IT | Inicial | Q-20 |
| DRM-A31 | Hacer la revisión técnica con IT: tarifas, costos y contactos del personal | P1 | IT | Inicial | — |
| DRM-A32 | Guardar esta spec, el código de las consultas de Power Query y la hoja de parámetros en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| DRM-A33 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-18 | ¿Qué diferencia entre el costo de App Routes y el C2S del Route Master es aceptable? ¿Se comparó con rutas reales? | Jennifer Guarin | Dueño |
| Q-06 a Q-13 | `RATE` y "Third parties", Global vs Route ID, visitas repetidas de Costco, columnas ABC, hojas ocultas, regla de duración por ABC, vigencia de archivos externos y copias. Ver el documento completo | Varios | Dueño |
| Q-19 | ¿Last Visit y Visit FS leen este libro, o solo los archivos que menciona el dueño? | Dueño y PERFORMANCE | Inicial |
| Q-20 | ¿Quiénes tienen acceso al libro y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Hojas visibles y ocultas | Inicial: 7 visibles y 3 ocultas. Dueño: 10 hojas, 8 ocultas | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-02 | Tamaño | Inicial: ≈ 3.658 filas × 56 columnas. Dueño: 3.664 filas × 49 columnas | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-03 | Responsables y suplente | Inicial: creador y administrador el dueño, sin suplente. Dueño: son co-responsables, ambos tienen la contraseña y cada uno respalda al otro | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-04 | Quién lo lee | Inicial (inventario): Last Visit y Visit FS. Dueño: Execution Team y FS, DM y RM en lectura; lo copian o leen el DSD FS Route Master, el Route Master Copy, el Michaels Router Pilot y el análisis de incidentes | Lo del dueño; confirmar con PERFORMANCE (Q-19) | ❓ Por confirmar |
| C-05 | Frecuencia | Inicial: según la necesidad. Dueño: 500 versiones en 42 días, con cada cambio de ruta | Cada cambio de ruta; casi diaria | ✅ Resuelta a favor del dueño |
| C-06 | Cómo se alimenta | Inicial: por confirmar; sugería relación con Isolved y AFS. Dueño: desde App Routes (traspaso manual), el Store Master y archivos externos, entre ellos el Requis ID Book con el ID de iSolved | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-07 | Nivel de riesgo | Inicial: estabilidad «Medio» y escalabilidad «Bajo». Dueño: supuestos del costo sin documentar, búsquedas por letra de columna, `#REF!`, dependencias personales y poco historial | Estabilidad «Alto» y escalabilidad «Medio» | ❓ Por confirmar |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, inventario de consultas y fórmulas, calidad de datos y backlog completo) todavía no están integrados.
- Las preguntas menores Q-06 a Q-13 (`RATE` y «Third parties», Global frente a Route ID, visitas repetidas de Costco, columnas ABC, hojas ocultas, regla de duración por ABC, vigencia de archivos externos y copias) están en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/dsd-route-master/spec.md`. [Inicial]
- Incluir el código de las 12 consultas de Power Query y la hoja `Parametros` del costo, sin datos de rutas, tarifas ni salarios. [Dueño · Inicial]
- Mantener en el mismo repositorio la documentación de los dos modelos de costo (App Routes y Route Master) y su comparación. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Modelar rutas y paradas como tablas (ruta, parada, tienda) con clave `Route ID` más `stop`. [Dueño · Inicial]
2. Guardar los supuestos del costo en una tabla de parámetros con valor, fecha y aprobador (DRM-A03). [Dueño]
3. Leer la jerarquía del Store Master por nombre de columna o desde la réplica SQL, no por letra de columna (DRM-A04). [Dueño · Inicial]
4. Calcular el costo de servir en SQL y medir la diferencia con App Routes (DRM-A25). [Dueño]
5. Exponer una vista con los nombres actuales de las tablas `RouteMaster` y `StoreMaster_DSD` para el DSD FS Route Master, el Plan de visitas y el Stores Contact List. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 4 | Dos co-responsables que se respaldan; falta mover los archivos personales |
| Operación documentada | 2 | Flujo de cambio por correo y lista de verificación propuesta |
| Control de acceso | 2 | Todos los FS, DM y RM abren el libro; hojas de costo sin proteger |
| Contrato de datos | 1 | Supuestos del costo en las consultas; búsquedas por letra de columna |
| Calidad y validación | 2 | Los IDs cumplen el patrón; `#REF!` y `#FS = 0` |
| Automatización e integración | 2 | Consultas de Power Query, pero el traspaso desde App Routes es manual |
| Trazabilidad de cambios | 1 | Solo 500 versiones (≈ 2 meses) y un flujo en correos sin identificador |
| Entornos y pruebas | 2 | Hay copias y pilotos; falta probar Michaels |

**Nivel global: 2,1 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.
