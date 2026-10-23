# Spec · DSD Store Master

> **English version pending.** This document is currently available in Spanish only.

> Versión final recomendada, lista para revisión final y aprobación. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado `data-sql`. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m19 (inventario MIC) |
| Tipo | Base de datos: archivo maestro en Excel |
| Versión | 3.0 |
| Estado | Lista para revisión final y aprobación |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

DSD Store Master es la tabla maestra de las tiendas que Falcon Farms atiende, atendió o atenderá: una fila por tienda, con su ubicación, jerarquía de campo (RM → DM → FS), estado en el programa y parámetros de replenishment y merchandising. Ruteo, replenishment, supervisión de campo, costos, RR. HH. y los reportes de desempeño dependen de ella. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 21.367 filas × 76 columnas, en 1 hoja y 1 tabla (`StoreMaster`) ⚠️ C-02 | Dueño |
| Clientes | 16: DSD (Walmart, Sprouts, Michaels, Costco), convenience (CVS, Walgreens, QuikTrip) y 9 inactivos, legacy o piloto | Dueño |
| Tiendas | Activas 2.610 · Pendientes 7 · Inactivas 310 · Sin estado 18.440 (convenience) | Dueño |
| Activas por cliente | Walmart 1.813 · Sprouts 507 · Michaels 173 · Costco 91 · Walgreens 18 · CVS 8 | Dueño |
| Jerarquía | 4 RMs DSD y 1 DM de convenience · 14 DMs · 106 FS (24,7 tiendas por FS; rango 7–42) | Dueño |
| Actividad | 500 versiones en 40 días, en 34 de ellos; todas del dueño ⚠️ C-04 | Dueño |
| Nivel de riesgo | Medio en vulnerabilidad, estabilidad y escalabilidad ⚠️ C-13 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. Otros archivos leen la tabla por el nombre de sus columnas: renombrar o borrar una columna los rompe, y no hay regla de aviso previo. [Dueño]
2. Depende de una persona, aunque la suplente ya está definida, y casi no hay historial: SharePoint guarda unos 40 días de versiones y no registra qué cambió. [Dueño]
3. Ya existe una réplica en SQL cargada desde este archivo, sin dueño ni frecuencia documentados. [Dueño] ⚠️ C-05
4. El inventario apuntaba a una copia vieja en un OneDrive personal. [Inicial] ⚠️ C-01
5. Funciona bien: la llave `Store Number WF` es única, las tiendas DSD activas tienen dirección, coordenadas y jerarquía completas, y `Same Store` es coherente en el 99 % de ellas. [Dueño]

**Contradicciones:** 13 detectadas; 6 resueltas a favor del dueño y 7 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (A01 a A07 y A20) y las preguntas Q-02 y Q-14. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Tener **una sola respuesta** compartida a qué tiendas están activas, dónde están, quién las supervisa y cómo se abastecen. Un maestro único, mantenido a diario por un responsable con nombre y una suplente, evita que cada equipo guarde su propia copia.

- **Problema que resuelve:** ruteo, replenishment, supervisión de campo, asignación de costos y reportes necesitan la misma lista de tiendas y la misma jerarquía. [Dueño]
- **Qué logra:** una fila por tienda con identificación, dirección y coordenadas, zonificación del cliente, jerarquía de campo (por persona y por posición), estado en el programa y parámetros de replenishment y merchandising. [Dueño]
- **Éxito:** los equipos y los archivos que la leen nunca se rompen ni muestran tiendas distintas; ver los criterios de éxito en «Requisitos funcionales consolidados». [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: identificación y ubicación de tiendas; zonificación del cliente; jerarquía de campo de Falcon Farms; estado en el programa; parámetros de replenishment y de merchandising; location de RR. HH. y contabilidad.

**No incluye** [Dueño]: diseño de rutas (Route Master), datos de producto (Product Master), calendarios (Date Master), datos maestros de empleados y nómina (iSolved), generación de pedidos (Retalon), ventas de tienda, el Convenience Store Master y los archivos que leen el Store Master (DSD Route Master, DSD_DisplayFill y la réplica SQL), que son herramientas aparte.

**Futuro** [Dueño · Inicial]: un maestro de posiciones con fechas de vigencia; un registro de cambios; sincronización automática desde el Convenience Store Master; mover el maestro a una lista o base de datos con validación y auditoría (ver «Oportunidades de mejora»).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Responsable del mantenimiento (el dueño) | Crea, actualiza y cierra tiendas; mantiene la jerarquía y los datos de replenishment | Ediciones en 34 de los últimos 40 días | Dueño |
| Suplente | Cubre al responsable | — | Dueño |
| Administrador de convenience | Es dueño de los datos de las tiendas de convenience | 18.466 filas | Dueño |
| Replenishment y Retalon | Usan DC, calendarios, display y ABC para planear pedidos | 35 columnas | Dueño |
| Execution Team | Usa la jerarquía, el servicio de merch y el estado | 31 columnas | Dueño |
| Operations Performance Team | Usa la zonificación, la zona de iSolved y la location | 3 columnas | Dueño |
| RR. HH., AFS, Demand Planning y Training | Leen la lista de tiendas y la jerarquía | — | Dueño |
| Dueños de archivos dependientes | Leen el Store Master desde otros archivos | 3 archivos | Dueño |

**Acceso**

- Está en SharePoint (sitio DSD Business Analysis › DSD Data Master) con **permisos propios**, no heredados del sitio. Exige cuenta de la empresa y permiso; no tiene enlace público. [Dueño · Inicial]
- Tiene la opción «recomendado de solo lectura» con una contraseña de escritura registrada a nombre de otra persona; se mantiene a propósito. [Dueño]
- La protección de hoja está configurada pero no activada, y los 4 rangos de edición permitida no tienen contraseña. Un filtro guardado (4 clientes DSD y un FS específico) oculta 21.337 filas a quien abre el archivo. [Dueño]
- ❓ Falta la lista de personas con acceso y su permiso, y quién aprueba los accesos nuevos (Q-16). [Inicial]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño · Inicial]

- Mantiene al día los cambios que llegan cada día o día por medio: tiendas nuevas, cierres, jerarquía, posiciones y datos de replenishment.
- Aprueba cualquier cambio de columnas y define las reglas de negocio y el diccionario.
- Avisa a Execution Team y a Replenishment de las aperturas, cierres y cambios de FS, y a los dueños de los archivos dependientes antes de cambiar columnas.
- Custodia la contraseña de escritura (confirmado el 2026-10-22).
- Aprueba esta spec junto con el administrador.

## Administrador técnico

**Jeronimo Sanchez**, administra el archivo (según el inventario). [Inicial]

- Administra el archivo en SharePoint y Excel, con sus permisos propios. [Dueño]
- ❓ La réplica SQL `sqldb-dsd-gold` la administra otro equipo, por confirmar entre Data/BI e IT (Q-02). [Dueño]
- ❓ Quién aprueba los accesos nuevos al archivo (Q-16). [Inicial]

## Suplente

**Jennifer Guarin.** Edita el archivo con la contraseña de escritura (confirmado el 2026-10-22). [Dueño] ⚠️ C-06

Para que la suplencia funcione necesita acceso a cada componente:

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| `DSD Store Master.xlsx` y su contraseña de escritura | Editar el archivo | ✅ Edita con la contraseña |
| Datos de convenience | Recibir el export del Convenience Store Master para el reemplazo completo y tener contacto con su administrador | ⬜ Pendiente (A01) |
| Archivos dependientes | Saber quiénes son sus dueños, para avisarles antes de cambiar columnas | ⬜ Pendiente (A01) |
| Solicitudes y notificaciones | Estar en la distribución donde llegan aperturas, cierres y cambios de posición, y saber a quién notificar | ⬜ Pendiente (A01) |
| Guía de operación | Esta spec y la lista de verificación de «Procesos operativos» | ✅ Este documento |

**Quién hace qué** [Dueño]

| Actividad | Ejecuta | Aprueba | Consulta | Informa |
| --- | --- | --- | --- | --- |
| Crear, activar o cerrar una tienda DSD | Dueño (suplente en su ausencia) | Dueño | Replenishment y Execution Team | Operations Performance y dependientes |
| Actualizar la jerarquía (RM, DM, FS, posiciones) | Dueño o suplente | Dueño | Execution Team | Replenishment, Operations Performance y dependientes |
| Actualizar datos de replenishment | Dueño o suplente | Replenishment | — | Dependientes |
| Actualizar las filas de convenience | Dueño o suplente | Administrador de convenience | — | Execution Team y dependientes |
| Actualizar la zona y la location de iSolved | Dueño o suplente | Operations Performance | — | Dependientes |
| Agregar, renombrar o borrar una columna | Dueño | Dueño | Todos los equipos | Dueños de archivos dependientes, con aviso previo |
| Definir las reglas de negocio (diccionario) | Dueño | Dueño | Todos los equipos | Dependientes |

## Fuentes de datos

| Fuente | Qué alimenta | Quién | Columnas |
| --- | --- | --- | --- |
| Cambios de tiendas Walmart, Sprouts, Michaels y Costco | Tiendas nuevas, cierres, direcciones, jerarquía, posiciones y replenishment | El dueño los escribe a mano, según solicitudes de Execution Team, Replenishment y Operations Performance | — |
| Convenience Store Master | Todas las filas de CVS, Walgreens y QuikTrip (reemplazo completo, según `Asignacion de Columnas Convenience.xlsx`) | Lo administra el administrador de convenience; lo pega el dueño | 3 |
| Replenishment | Identificación, DC, calendarios, display, Retalon, ABC, Segmentation, Zona AFS y BA | Equipo de Replenishment | 35 |
| Execution Team | Jerarquía y posiciones, contactos de tienda, zonificación, Active, Same Store, servicio de merch y zona horaria | Execution Team | 31 |
| Route Master | Merch Days y Merch Visit Duration | DSD Route Master (misma carpeta) | — |
| iSolved | Isolved Zone, Zone name y Location | Operations Performance Team | 3 |
| Retalon | Calendario Wk2 (no se usa) | Dueño de Retalon | 3 |
| Geocodificación y API de Python | Latitude, Longitude y Zona Horaria | Se calculan a partir de la dirección y se pegan | — |

Origen de todas las filas: [Dueño]. `CVP - WM` es la única columna sin documentar.

**Cómo llegan los datos al archivo** [Dueño]

- Escritos a mano para los clientes DSD.
- Reemplazados completos, a mano, para CVS, Walgreens y QuikTrip, cada columna fuente en la que indica el archivo de mapeo. El Store Master no tiene consultas ni vínculos externos.
- Fórmulas dentro del archivo: `Same Store` (filas 2–2.902) y las columnas espejo.
- Calculados afuera y pegados: coordenadas y zona horaria.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Archivos | Convenience Store Master · archivo de mapeo de columnas · Route Master · libro de documentación de columnas (hoy solo en un computador) |
| Sistemas | SharePoint (sitio DSD Business Analysis) · Excel · iSolved · Retalon · script o API de Python para zonas horarias |
| Procesos | Alta y cierre de tiendas · cambios de jerarquía y posiciones · cambios de replenishment · sincronización de convenience · geocodificación |
| Personas | Responsable y suplente disponibles (los cambios llegan cada día o día por medio) · administrador de convenience |

**Archivos que dependen del Store Master** (herramientas aparte; se avisa a sus dueños antes de cambiar columnas) [Dueño]

| Archivo dependiente | Qué toma | Dueño |
| --- | --- | --- |
| DSD Route Master | Lista de tiendas, jerarquía y estado (también para costos de FS y DM) | Tendrá su propia spec próximamente |
| DSD_DisplayFill | Lista de tiendas y datos de display | Desconocido (Q-13) |
| Réplica SQL `sqldb-dsd-gold › DSDStoreMaster` | Copia programada del Store Master | Por confirmar (Q-02) |

**Copias que circulan** [Dueño]: 5 copias locales desactualizadas en Descargas y 1 en la carpeta; no deben usarse como fuente (A02).

## Procesos operativos

Los cambios llegan **cada día o día por medio**. [Dueño] ⚠️ C-04

**Lista de verificación por cambio** (responsable o suplente) [Dueño]

1. Antes de editar: **quitar todos los filtros** (o usar una Vista de hoja personal) para que nada quede oculto para los demás.
2. **Tienda nueva:** agregar la fila **dentro** de la tabla (para que se extiendan las fórmulas) con la llave `<número><Cliente>`. Llenar los campos mínimos: identificación, dirección, coordenadas, zona horaria, jerarquía y posiciones, `Active = P`, `Program Start date`, Service Model, FF Facility, Merch Days y Merch Visit Duration (del Route Master), y los campos de replenishment del cliente.
3. **Activación:** en la fecha de inicio cambiar `P` → `Y`; `Same Store` pasa a `NEW` automáticamente si la fila tiene la fórmula.
4. **Cierre:** `Active = N` y `Program End date`. Liberar el FS. No borrar la fila.
5. **Cambio de jerarquía:** actualizar la persona **y** la posición (`FF Field Supervisor` + `FF Field Supervisor Position`, y lo mismo para DM y RM). Verificar que las columnas espejo se actualicen.
6. **Cambio de replenishment:** DC, días del calendario, tamaño del display y ramos, DC de Retalon, ABC y Segmentation.
7. **Convenience:** reemplazar las filas de CVS, Walgreens y QuikTrip con el Convenience Store Master vigente, según el archivo de mapeo. No corregir valores de convenience en el Store Master: el siguiente reemplazo los sobrescribe; pedirle al administrador de convenience que los corrija en la fuente.
8. Antes de guardar: ningún duplicado resaltado en `Store Number WF`, ningún `#N/A` ni `#NAME?`, sin espacios al final en los valores nuevos.
9. Después de guardar: notificar a **Execution Team y Replenishment** las aperturas, cierres y cambios de FS.
10. Antes de cualquier cambio de **columnas** (renombrar, borrar, cambiar el tipo o renombrar la tabla `StoreMaster`): avisar a los dueños de los archivos dependientes (ver «Dependencias»). Agregar una columna al final es seguro.

**Por evento** [Dueño]

| Disparador | Mantenimiento | Impacto si no se hace |
|------------|---------------|-----------------------|
| Se aprueba una tienda nueva | Fila con `Active = P`, fecha de inicio, FS y datos de replenishment | Los equipos y los archivos dependientes no ven la tienda |
| La tienda empieza a operar | `P` → `Y` | La tienda no cuenta como activa; Same Store queda mal |
| La tienda cierra | `Active = N`, fecha de fin, liberar el FS | Carga de FS y costos sobrestimados |
| Cambia un FS, DM o RM (persona o posición) | Columnas de nombre y posición; columnas espejo | Asignación errada en costos de FS/DM, rutas y jerarquía de incidentes |
| Cambio de replenishment | Columnas de calendario, DC, display y Retalon | Pedidos errados en Retalon |
| Cambio en convenience | Reemplazo completo desde el Convenience Store Master, según el archivo de mapeo | Cifras de convenience desactualizadas |
| Se agrega una columna al Convenience Store Master | Agregarla al archivo de mapeo (y al Store Master al final, si hace falta) | Datos de convenience perdidos o pegados en la columna equivocada |
| Se pide una columna nueva | Acordar nombre y tipo; agregarla al final; actualizar el diccionario | Columna sin documentar (como `CVP - WM` hoy) |
| Se renombra o borra una columna | **Avisar primero a los dueños de los archivos dependientes** | Los archivos dependientes dejan de actualizarse |

## Reglas de negocio

**Principios que gobiernan el maestro** [Dueño]

- **Art. I. Una fila = una tienda, una llave.** `Store Number WF` es única, nunca se reutiliza y no se edita después de creada. Las tiendas se desactivan, no se borran.
- **Art. II. La estructura de columnas es un contrato.** Los nombres y tipos de las 76 columnas y el nombre de la tabla `StoreMaster` son estables. Renombrar, borrar o cambiar el tipo de una columna requiere avisar antes a los dueños de los archivos dependientes y registrar el cambio en este documento. Aprueba: El dueño.
- **Art. III. Un significado documentado por columna y canal.** Dentro de DSD, una columna tiene el mismo tipo de valor para todos los clientes. Convenience puede reutilizar una columna solo a través del archivo de mapeo, y el diccionario indica ese significado.
- **Art. IV. Los valores codificados salen de listas.** Estado, códigos de día, facilities, clasificaciones y locations usan valores documentados (sin escritura libre ni espacios al final).
- **Art. V. Sin dependencias ocultas.** Ninguna fórmula del maestro puede depender de archivos personales o de archivos fuera de la carpeta DSD Data Master.
- **Art. VI. Todo cambio es trazable.** Cada cambio tiene fecha, autor y motivo, y se conserva al menos 12 meses.
- **Art. VII. Continuidad.** El responsable o la suplente pueden completar cualquier cambio sin pedir accesos.
- **Art. VIII. El archivo se deja limpio.** Sin filtros guardados, sin filas ocultas y sin datos de prueba al guardar.
- **Art. IX. Privacidad.** Los nombres de colaboradores y contactos de tienda se usan solo para la operación interna.

**Definiciones** [Dueño]

| # | Término | Definición |
|---|---------|------------|
| D1 | **Tienda (registro)** | Una fila = una ubicación de un cliente que Falcon Farms atiende, atendió o está por atender. Las filas nunca se borran: se desactivan |
| D2 | **Store Number WF** | Llave única: `<Customer Store Number><nombre corto del cliente>` sin espacios (ej. `1042Walmart`, `110Sprouts`). Los duplicados se resaltan automáticamente |
| D3 | **Canal** | **DSD:** Walmart, Sprouts, Michaels, Costco (se mantienen en este archivo). **Convenience:** CVS, Walgreens, QuikTrip (vienen del Convenience Store Master). **Legacy o piloto:** clientes inactivos que se conservan como historia |
| D4 | **Estado (Active)** | **Y** en servicio · **P** pendiente: aprobada, con `Program Start date` futura · **N** ya no se atiende (con `Program End date`) · vacío: no se maneja con esta marca (convenience hoy) |
| D5 | **Program Start / End date** | Primer y último día de la tienda en el programa de Falcon Farms. Hoy se usa "NA" cuando no hay fecha de fin |
| D6 | **Same Store** | **NEW**: fecha de inicio dentro de los últimos 365 días · **SS**: un año o más en el programa · **NS** y **CLOSED**: se usan pero no están definidos (Q-04). Fórmula: `IF(Program Start date > TODAY()-365, "NEW", "SS")` |
| D7 | **Service Model** | **DC**: el producto se entrega a través del centro de distribución del cliente · **DSD**: lo entrega directamente en la tienda una facility de Falcon Farms |
| D8 | **FF Facility** | Facility de Falcon Farms que atiende o despacha a la tienda: **FFM** Miami · **FFG** Georgia · **FFT** Texas · **FFZ** Arizona · **FFC** California · **FFK** Kentucky. "FF" en las filas de convenience viene del campo de Convenience "DC/WF Falcon"; su significado está por confirmar con el administrador de convenience |
| D9 | **ABC Classification** | Clase de la tienda por volumen de venta: AA (la más alta), A, B, C, D, E (solo Walmart); "NA" = sin clasificar |
| D10 | **Segmentation** | Segmento propio de cada cliente. Sprouts: Lead / Gold / Silver / Bronze. Walmart: A–E. Walgreens: tipo de farmacia. Cada esquema necesita su propia definición |
| D11 | **Calendario de replenishment** | `Store Pull Day` (día en que se hace el pull del pedido), `Facility Departure Day`, `Store Arrival Day`, `DC Arrival Day`. Códigos de día MO TU WE TH FR SA SU unidos con "-" (ej. `TH-MO`). Los usa Retalon. El juego "Wk2" no se usa |
| D12 | **Capacidad del display** | `Display Size in Buckets` × `Bunches per Bucket` = `Total Bunches per Store` (exacto en Walmart y Costco; en Sprouts, los ramos por balde se derivan como total ÷ baldes). Mínimo de ramos en display por producto: Roses, Mixes, CB |
| D13 | **Customer DC / Virtual DC Retalon** | DC del cliente que recibe la entrega, y nombre del DC que se usa en Retalon |
| D14 | **Servicio de merchandising** | `Merch Days` (días de visita, del Route Master) y `Merch Visit Duration (mins)`. En Michaels, por diseño: el día de pull es igual al día de merch, Receiving Manager = "Serving" y `Route (Cstore ONLY)` tiene la ruta del router |
| D15 | **Jerarquía de campo** | RM → DM → FS, por persona ("APELLIDO, NOMBRE") y por **posición** (`RM_<región>`, `DM_<distrito>`, `FS_<territorio>`). La posición se mantiene cuando cambia la persona. Cada DM pertenece a un solo RM y **cada FS tiene exactamente una posición** (confirmado). Excepción por diseño: Un RM también figura como DM de la región South (Costco), así que sus tiendas muestran `RM_South` como posición de DM |
| D16 | **Distrito de ventas de Falcon Farms** | `Customer District (Sales)`, `District` y `FF District Manager Position` describen casi el mismo territorio del DM con nombres distintos (ej. GASCAL = Mid Atlantic) |
| D17 | **Zonificación del cliente** | `Region`, `Area`, `Zone`, `Customer District #`: la estructura propia del cliente (ej. zona de Walmart "Durham II NC") |
| D18 | **Zona AFS** | Distrito de replenishment (Sprouts y Costco) |
| D19 | **Zona de iSolved, Zone name, Location** | Zona de RR. HH./nómina y location contable (ej. `2930 Texas Walmart C2S`), de iSolved |
| D20 | **Zona horaria (`Zona Horaria`)** | Nombre IANA (ej. `America/Chicago`), calculado a partir de las coordenadas con un script / API de Python |
| D21 | **VIP** | Tienda de Sprouts cercana a personal corporativo |
| D22 | **CVP - WM** | Marca de Walmart: **"Yes" = hay que registrar inventario en la tienda** (217 tiendas Walmart activas); "0" = no se registra inventario |
| D23 | **BA** | Analista de negocio asignado a la tienda |

## Requisitos funcionales consolidados

#### Identificación y ciclo de vida
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-001 | El maestro MUST tener una fila por tienda con una llave única `Store Number WF` | Must Have | ✅ 0 duplicados, se resaltan si aparecen | Dueño |
| FR-002 | El maestro MUST registrar el estado (Y, P, N) y las fechas de inicio y fin de cada tienda DSD | Must Have | ✅ DSD. Convenience: la fuente no tiene estado, queda vacío | Dueño |
| FR-003 | El maestro MUST clasificar cada tienda activa como NEW o SS a partir de su fecha de inicio | Must Have | ⚠️ 2.591 de 2.617 coherentes; fórmula solo en las filas 2–2.902 | Dueño |
| FR-004 | El maestro SHOULD definir cada código de estado que usa | Should Have | ❌ "NS" y "CLOSED" sin definir; pasa al backlog (Q-04) | Dueño |
| FR-005 | El maestro MUST conservar las tiendas cerradas (sin borrarlas) | Must Have | ✅ 310 filas inactivas conservadas | Dueño |
| FR-006 | El maestro MUST guardar dirección, coordenadas y zona horaria de cada tienda activa | Must Have | ✅ DSD 100 %; ⚠️ convenience sin zona horaria | Dueño |

#### Jerarquía
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-010 | Cada tienda activa MUST tener un RM, un DM y un FS, por nombre y por posición | Must Have | ✅ DSD; ❌ posiciones de convenience | Dueño |
| FR-011 | Cada FS MUST corresponder a exactamente una posición y cada DM a exactamente un RM | Must Have | ⚠️ 1 FS con 2 posiciones (error, en corrección). Que un RM figure también como DM es intencional | Dueño |
| FR-012 | La jerarquía MUST NOT depender de otros archivos | Must Have | ✅ Lookups quitados el 2026-10-21 | Dueño |
| FR-013 | La jerarquía SHOULD guardarse una sola vez (sin columnas espejo) | Should Have | ❌ 4 columnas espejo | Dueño |
| FR-014 | Los cambios de jerarquía SHOULD conservar su historia (fechas de vigencia) | Should Have | ❌ | Dueño |

#### Replenishment y servicio
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-020 | El maestro MUST tener DC, días del calendario, capacidad del display y DC de Retalon de las tiendas que se abastecen con Retalon | Must Have | ✅ Sprouts y Costco al 100 % | Dueño |
| FR-021 | Los campos codificados MUST usar listas documentadas (días, facility, ABC, segmentation, display location) | Must Have | ⚠️ variantes de escritura | Dueño |
| FR-022 | Cada columna MUST tener un solo tipo de valor documentado dentro de DSD, y su significado en convenience MUST estar documentado | Must Have | ⚠️ Minutos de Walmart en Merch Visits per day; el formato Walmart en Store Size es una excepción aceptada; ≈ 24 significados de convenience solo en el archivo de mapeo | Dueño |
| FR-023 | Los días y la duración de merch MUST coincidir con el Route Master | Must Have | ❓ Sin cruzar todavía con el Route Master | Dueño |

#### Contrato de datos
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-030 | Los nombres y tipos de las columnas MUST estar documentados y ser estables | Must Have | ❌ | Dueño |
| FR-031 | Se MUST avisar a los dueños de los archivos dependientes antes de renombrar o borrar una columna | Must Have | ❌ sin regla | Dueño |
| FR-032 | Las columnas de número y fecha MUST contener solo números o fechas (sin "NA", formatos ni códigos) | Must Have | ❌ texto en Zip Code, Store Size, Program End date | Dueño |
| FR-033 | La carga de la réplica SQL MUST estar documentada (fuente, frecuencia, dueño) | Must Have | ⚠️ Fuente confirmada (este archivo, programada); falta dueño y frecuencia (Q-02) | Dueño |
| FR-034 | El mapeo de columnas de convenience MUST mantenerse junto al maestro y actualizarse cuando cualquiera de los dos maestros cambie columnas | Must Have | ⚠️ Existe en otro sitio; la documentación no lo menciona | Dueño |

#### Gobierno y programa
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-040 | Todo cambio MUST ser trazable (fecha, autor, motivo) durante 12 meses | Must Have | ❌ | Dueño |
| FR-041 | El responsable y su suplente (una persona registrada) MUST poder operar el maestro | Must Have | ✅ La suplente edita con la contraseña de escritura (confirmado el 2026-10-22) | Dueño · Inicial |
| FR-042 | El archivo compartido MUST guardarse sin filtros ni filas ocultas | Should Have | ❌ | Dueño |
| FR-043 | La protección SHOULD evitar ediciones accidentales en las columnas de llave y de fórmula | Should Have | ❌ protección no activada | Dueño |
| FR-050 | La documentación de la herramienta (ficha de 7 áreas y esta spec) MUST estar completa, sin pendientes sin responsable y fecha | Must Have | ⚠️ Spec completa; quedan 9 pendientes en la ficha y 10 preguntas abiertas | Inicial |
| FR-051 | El maestro MUST existir en un solo lugar oficial, controlado por la empresa y con permisos revisados; las copias locales y las de cuentas personales MUST retirarse | Must Have | ⚠️ Está en un sitio de equipo; hay 5 copias locales y 1 en la carpeta; la copia del inventario está por confirmar ⚠️ C-01 | Inicial · Dueño |
| FR-052 | La spec, el diccionario y los scripts de la herramienta MUST guardarse en un repositorio privado de GitHub de Falcon (`data-sql`) | Must Have | ❌ El repositorio aún no existe | Inicial (instructivo de GHT) |
| FR-053 | Los datos MUST estar en SQL | Must Have | ⚠️ Existe una réplica (`sqldb-dsd-gold`) cargada de forma programada desde el archivo; el archivo sigue siendo la fuente ⚠️ C-05 | Dueño · Inicial (instructivo de GHT) |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-001 | Llaves de tienda únicas | 100 % (0 duplicados) | 100 % | Dueño |
| SC-002 | Columnas documentadas con tipo y valores permitidos | 0 de 76 (75 descritas sin tipos) | 76 de 76 | Dueño |
| SC-003 | Valores de FS que dependen de archivos externos o personales | 20 → 0 (cumplido el 2026-10-21) | 0 | Dueño |
| SC-004 | Filas de Walmart con minutos en `Merch Visits per day` · significados de convenience documentados | 253 · 0 de ≈ 24 | 0 · todos | Dueño |
| SC-005 | Celdas con error (`#NAME?`, `#N/A`) | 118 | 0 | Dueño |
| SC-006 | Celdas con texto en columnas de número o fecha | ≈ 2.900 | 0 | Dueño |
| SC-007 | Tiendas activas o pendientes con `Same Store` coherente con la fecha de inicio | 2.591 de 2.617 (99,0 %) | 100 % | Dueño |
| SC-008 | Tiendas activas con FS asignado, y pendientes con FS antes de su inicio | 2.610 de 2.610 activas; 5 de 7 pendientes | 100 % | Dueño |
| SC-009 | Historial de cambios disponible | 40 días, sin detalle por campo | 12 meses o más, con detalle por campo | Dueño |
| SC-010 | Componentes que puede operar la suplente | 2 de 5 | 5 de 5 | Dueño · Inicial |
| SC-011 | Filas de convenience iguales al Convenience Store Master tras cada reemplazo | Sin medir | 100 % | Dueño |
| SC-012 | Días que tarda un cambio de jerarquía en llegar al maestro | Sin medir | 1 día hábil o menos | Dueño |
| SC-013 | Copias del maestro fuera de la carpeta oficial (Descargas, otras carpetas y cuentas personales) | 6 o más, más la del inventario por confirmar | 0 | Inicial |
| SC-014 | La carga a SQL tiene documentados su fuente, su frecuencia y su dueño | Fuente confirmada; sin dueño ni frecuencia | Los tres documentados | Inicial |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Guarda nombres de empleados y contactos de tiendas; exige cuenta y permiso; la protección de hoja no está activada y falta la lista de permisos | Inicial · Dueño |
| Estabilidad | Medio | Dueño y suplente definidos; sin registro de cambios y con solo 40 días de versiones; falta confirmar que la copia del OneDrive personal ya no se usa ⚠️ C-13 | Inicial · Dueño |
| Escalabilidad | Medio | 21.367 filas × 76 columnas en una sola tabla que se mantiene a mano; ya existe una réplica SQL | Inicial · Dueño |

| # | Riesgo | Impacto | Probabilidad | Mitigación | Origen |
| --- | --- | --- | --- | --- | --- |
| R1 | Una columna renombrada o borrada rompe los archivos que leen el Store Master | Alto | Media (ya hay 3 columnas marcadas «Eliminar») | A10 | Dueño |
| R2 | El responsable no está y los cambios se acumulan; no hay respaldo confirmado | Alto | Media | A01, Q-18 | Dueño · Inicial |
| R3 | No hay trazabilidad de los cambios de jerarquía ni de estado | Medio | Confirmada | A13, A18 | Dueño |
| R4 | Texto en columnas de número o fecha | Medio | Confirmada | A09, A11 | Dueño |
| R5 | Un filtro guardado hace pensar que faltan tiendas | Bajo | Confirmada | A05 | Dueño |
| R6 | Se usan copias locales o de cuentas personales en lugar del maestro | Medio | Media | A02 | Dueño · Inicial |
| R7 | La réplica SQL se desincroniza del archivo y no tiene dueño ni frecuencia documentados | Medio | Desconocida | A03 | Dueño · Inicial |
| R8 | Nombres de empleados y teléfonos de contactos sin regla de retención | Medio | Confirmada | Q-17 | Inicial |
| R9 | Un esquema SQL que cambie los nombres de las columnas rompería los archivos dependientes | Alto | Media | Vista de compatibilidad (ver «Recomendaciones para migración a SQL») | Inicial |
| R10 | Pasar el maestro a un servidor interrumpe a quienes lo usan hoy | Medio | Media | Migrar en paralelo y conservar el archivo hasta validar | Inicial |
| R11 | La protección de hoja está apagada y la contraseña de escritura está a nombre de otra persona | Bajo | Confirmada | A18 | Dueño |

**Calidad de los datos hoy** [Dueño]

| Campo | Problema | Filas |
|-------|----------|------:|
| `Store Size (SqFt)` | Walmart: formato de tienda en lugar de pies cuadrados (Supercenter 1.171 · Neighborhood Market 217 · Priority 8). Excepción aceptada | 1.396 |
| `Merch Visits per day` | Walmart: minutos (50/60/80) en lugar de visitas | 253 |
| Columnas de convenience | *Intencional, no es un error:* Merch Visits per day = "Every Day Service", Merch Visit Duration = "24 Hours", FS Visit Duration = "Stop #", Region/Area = códigos del cliente, Segmentation = "Store Description" (ver «Mapeo de columnas de convenience» en el Anexo). Problema: no está en el diccionario | ≈ 18.466 filas |
| `Segmentation` | Niveles de Sprouts y letras de Walmart en la misma columna; "Regular " y "B " con espacios al final | — |
| `FF Field Supervisor Position` | Un FS con dos posiciones; una posición con dos FS (error confirmado, en corrección) | 2 personas |
| `Same Store` | CVS marcadas NS aunque empezaron hace más de un año | 8 |
| `Program Start date` | Walgreens activas sin fecha de inicio | 18 |
| `Zip Code` | 4 dígitos (perdió el cero inicial) | 16 |
| `Zip Code` | Walgreens con "_" (ej. `33331_4665`) | 18 |
| `Program End date` | "NA" escrito en una columna de fecha (todas las filas) | 1.490 |
| `Merch Days`, `Merch Visit Duration` | `#NAME?` (Fiesta inactivas) | 58 + 58 |
| `Isolved Zone`, `Zone name` | `#N/A` | 1 + 1 |
| `Display Location` | 8 escrituras para 4 valores; filas con escritura no estándar (todas las filas) | 58 |
| `DC Arrival Day` | "N/A" y "NA" | 33 |
| `Store Number WF` | El sufijo no coincide con Customer (QuikTrip "Quiktrip", Tawa, Latin Fresh); espacio al final (3016Walgreens) | 226 |
| `State` | "MA " con espacio al final (Tawa inactiva) | 1 |
| `Latitude` / `Longitude` | Vacías, 0,0 o fuera de EE. UU. (convenience inactivas) | 3 |
| Tiendas pendientes | Sin FS (954Sprouts, 59Sprouts) | 2 |
| Michaels | `Location`, `Isolved Zone`, `Zone name`, `BA` y `Virtual DC Retalon` vacíos | 173 |
| Encabezados | `VIP ` y `FF Regional Manager  ` terminan en espacio; `ABC Clasification` mal escrito (mantenerlo: los archivos dependientes usan ese nombre exacto) | 3 |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Quitar el filtro guardado, corregir los datos, publicar el diccionario y esta spec junto al archivo, y adoptar la regla de «avisar antes de renombrar o borrar una columna» | Menos sorpresas, continuidad y un contrato escrito | A04 a A07, A10 | Dueño |
| Corto plazo | Listas de validación en las columnas codificadas; código postal como texto de 5 dígitos; `Program End date` vacío en lugar de «NA»; fórmula de `Same Store` en todas las filas DSD | Datos limpios y consistentes | A08, A09, A11, A12 | Dueño |
| Corto plazo | Un registro de cambios de solo agregar y un límite de versiones más alto | 12 meses o más de trazabilidad | A13 | Dueño · Inicial |
| Mediano plazo | Un maestro de posiciones (posición → persona, RM → DM → FS, con vigencia); quitar las columnas espejo tras avisar a los dependientes | Una sola fuente para la jerarquía, con historia | A16 | Dueño |
| Mediano plazo | Traer las filas de convenience automáticamente desde el Convenience Store Master, o mantenerlas en una tabla aparte con la misma llave | Sin copia manual y con propiedad clara | A17 | Dueño |
| Largo plazo | Mover el maestro a una lista o base de datos con formularios, validación, auditoría y un export programado a la réplica SQL | Validación y auditoría incorporadas; menos trabajo manual | A19 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza la acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. | Se entrega cuando |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Completar los accesos de la suplente: export de convenience, dueños de archivos dependientes y canales de solicitudes | P0 | Dueño y suplente | Dueño | T-001 | Completa un cambio de tienda de principio a fin sin ayuda |
| A02 | Confirmar cuál es la copia vigente; retirar la del OneDrive personal y las 5 copias locales y la de la carpeta; marcarlas como obsoletas y corregir el inventario | P0 | Dueño | Inicial · Dueño | T-002 y C-01 | Hay una sola copia vigente y el inventario apunta a ella |
| A03 | Averiguar qué es la base `sqldb-dsd-gold` y documentar su fuente, su dueño y cada cuánto se carga | P0 | Data/BI e IT | Dueño · Inicial | T-003 y C-05 | Dueño, ubicación y frecuencia anotados |
| A04 | Publicar el diccionario de columnas y este documento junto al archivo, en `DSD Data Master` | P0 | Dueño | Dueño | T-002 | Ambos están en la carpeta del archivo |
| A05 | Quitar el filtro guardado; usar vistas de hoja para los filtros personales | P0 | Dueño | Dueño | T-010 | El archivo se abre sin filtros ni filas ocultas |
| A06 | Corregir los problemas de datos: FS de las tiendas pendientes, posiciones de un FS, zips, `#NAME?`, `#N/A` y espacios al final (ver «Calidad de los datos hoy») | P0 | Dueño | Dueño | T-012 | Sin celdas con error |
| A07 | Activar las 7 tiendas pendientes de Sprouts en su fecha de inicio: 576 y 495 (inicio el 2026-10-23), 50, 58 y 185 (inicio el 2026-10-30), 954 y 59 (inicio el 2026-11-06); 954 y 59 no tienen FS | P0 | Dueño | Dueño | T-013 | Las 7 tiendas figuran como activas |
| A08 | Completar el diccionario: tipo, valores permitidos, fuente y dueño de las 76 columnas (agregar `CVP - WM`) y el significado en convenience; mantener el archivo de mapeo junto al maestro | P1 | Dueño | Dueño | T-020 | 76 de 76 columnas documentadas |
| A09 | Agregar listas de validación a las columnas codificadas y corregir las variantes | P1 | Dueño | Dueño | T-021 | Sin variantes de escritura |
| A10 | Escribir la regla de cambio de columnas (aprueba el dueño; aviso previo a los dueños de los archivos dependientes) y aplicarla antes de borrar SubRegion y las columnas de Senior Sales Lead | P1 | Dueño | Dueño | T-022 y C-07 | Los dueños dependientes confirman antes de cada cambio |
| A11 | Sacar los minutos de `Merch Visits per day` en 253 filas de Walmart | P1 | Dueño | Dueño | T-023 | 0 filas con minutos |
| A12 | Definir NS y CLOSED y extender la fórmula de `Same Store` a todas las filas DSD | P1 | Dueño y administrador de convenience | Dueño | T-024 y C-11 | Same Store coherente en 100 % |
| A13 | Crear un registro de cambios de solo agregar y subir el límite de versiones de la biblioteca | P1 | Dueño | Dueño · Inicial | T-030 y C-13 | 12 meses de cambios con fecha, autor y motivo |
| A14 | Hacer la revisión técnica con IT o Arquitectura: el archivo guarda datos de personas y alimenta una base SQL | P1 | IT y Arquitectura | Inicial | — | Revisión firmada |
| A15 | Guardar esta spec, el diccionario y los scripts en el repositorio privado `data-sql` cuando exista | P1 | PM | Inicial (GHT) | FR-052 | Archivos en el repositorio |
| A16 | Crear un maestro de posiciones con fechas de vigencia y quitar las columnas espejo, avisando antes a los dueños dependientes | P2 | Dueño | Dueño | T-031 | Una sola fuente para la jerarquía, con historia |
| A17 | Automatizar el reemplazo completo de convenience usando el archivo de mapeo | P2 | Dueño y administrador de convenience | Dueño | T-032 | Ninguna columna pegada en el lugar equivocado |
| A18 | Activar la protección de hoja en las columnas de llave y de fórmula | P2 | Dueño | Dueño | T-034 | Protección efectiva |
| A19 | Pasar el Store Master a SQL como fuente única (tanda 1 de la migración a SQL), partiendo de la réplica existente | P2 | Arquitectura y dueño | Inicial · Dueño | T-035 | SQL es la fuente; el archivo queda solo de consulta |
| A20 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — | Firmas en el pull request |

**Ya hechas:** T-000 Definir responsable y suplente · T-011 Quitar los 20 lookups de FS a un archivo sin relación y el vínculo externo (2026-10-21).

## Preguntas abiertas

Las fechas límite son una propuesta, para resolverlas antes de firmar la spec.

| ID | Pregunta | Responsable | Fecha límite | Desbloquea |
| --- | --- | --- | --- | --- |
| Q-02 | ¿Qué es la base `sqldb-dsd-gold` (dónde está alojada, quién la administra) y quién corre su carga y con qué frecuencia? | Data/BI e IT | 2026-11-27 | A03, FR-053, C-05 |
| Q-04 | ¿Qué significan NS y CLOSED en Same Store? ¿Debe ser fórmula en todas las filas DSD? | Administrador de convenience (NS) y dueño (CLOSED y fórmula) | 2026-11-27 | A12, C-11 |
| Q-06 | ¿Qué significa «FF» en las filas de convenience (1.449 filas, de «DC/WF Falcon»)? | Administrador de convenience | 2026-11-27 | Definición D8 |
| Q-13 | ¿Quién es el dueño de DSD_DisplayFill? | Dueño | 2026-11-27 | A10 |
| Q-14 | ¿Cuál es la copia vigente: el archivo del sitio DSD Business Analysis o el del OneDrive del inventario? ¿Se puede retirar la otra? | Dueño | 2026-11-27 | A02, C-01 |
| Q-15 | ¿Las hojas ZoningBonus y Sheet1 a Sheet3 de la copia anterior existen en algún archivo vigente? ¿Se usan? | Dueño | 2026-11-27 | C-02 |
| Q-16 | ¿Quiénes tienen acceso al archivo y quién aprueba los accesos nuevos? | Dueño e IT | 2026-11-27 | Usuarios |
| Q-17 | ¿Cuánto tiempo se conservan los nombres de personas que ya no trabajan en Falcon? | Dueño y PM | 2026-12-11 | Riesgo R8 |
| Q-18 | ¿Hay un respaldo fuera de SharePoint y cómo se restaura una versión anterior? | Dueño e IT | 2026-11-27 | Riesgo R2 |
| Q-19 | ¿Cuándo conviene pasar el maestro a una base de datos con validación y auditoría? | Dueño y Arquitectura | 2027-01-22 | A19 |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Ubicación del archivo | Inicial: un OneDrive personal (riesgo de estabilidad «Alto»). Dueño: sitio de equipo DSD Business Analysis, con permisos propios, creado ahí el 2025-09-11 | Sitio de equipo. Confirmar que la copia del OneDrive ya no se usa y retirarla (Q-14, A02). El riesgo de estabilidad baja a «Medio» | ❓ Por confirmar |
| C-02 | Tamaño y estructura | Inicial: 21.358 filas, 82 columnas y 5 hojas (3 ocultas, entre ellas ZoningBonus). Dueño: 21.367 filas × 76 columnas y 1 hoja | Lo del dueño, leído en el archivo vigente. Confirmar que las hojas extra no se usan (Q-15) | ❓ Por confirmar |
| C-03 | Suplente | Inicial: sin suplente registrado. Dueño: hay suplente y edita con la contraseña de escritura | Suplente registrada (confirmado el 2026-10-22) | ✅ Resuelta a favor del dueño |
| C-04 | Frecuencia de actualización | Inicial: «según la necesidad». Dueño: cada día o día por medio (34 de los últimos 40 días) | Diaria o día por medio | ✅ Resuelta a favor del dueño |
| C-05 | Migración a SQL | Inicial: propone pasar la base a un servidor, partiendo de cero. Dueño: ya existe una réplica en SQL cargada de forma programada desde este archivo | La migración parte de la réplica existente; falta saber quién la administra (Q-02) | ✅ Resuelta a favor del dueño; ❓ dueño de la réplica |
| C-06 | Verificación de la suplente | El análisis del dueño pide verificar el permiso de la suplente; el dueño confirmó el 2026-10-22 que edita con la contraseña de escritura | Cumplido. Falta solo completar sus accesos a convenience, dependientes y solicitudes (A01) | ✅ Resuelta a favor del dueño |
| C-07 | Columnas marcadas «Eliminar» | La documentación marca SubRegion, FF Senior Sales Lead y su posición como «Eliminar», pero DSD Route Master las lee | No borrarlas hasta avisar a su dueño (A10) | ⚠️ Abierta |
| C-08 | Documentación frente a los datos | La documentación dice que `Store Size (SqFt)` y las columnas de managers no tienen datos, pero varios clientes las tienen llenas | Actualizar el diccionario (A08) | ⚠️ Abierta |
| C-09 | `Route (Cstore ONLY)` en Michaels | Se documenta como «solo convenience», pero está llena en todas las tiendas Michaels | Intencional; documentarlo | ✅ Resuelta a favor del dueño |
| C-10 | Un RM que también figura como DM | Un RM aparece como DM de las mismas 99 tiendas (posición de DM «RM_South») | Intencional; documentarlo | ✅ Resuelta a favor del dueño |
| C-11 | `Same Store` calculada o escrita a mano | Está documentada como calculada, pero la fórmula solo cubre las filas 2–2.902 y NS y CLOSED se escriben a mano | Definir NS y CLOSED y extender la fórmula (A12, Q-04) | ❓ Por confirmar |
| C-12 | Columna `District` dividida | Un mismo DM aparece dividido en dos nombres de distrito (106 y 53 tiendas) | Cosmético; confirmar la regla de nombres | ❓ Por confirmar |
| C-13 | Nivel de riesgo de estabilidad | Inicial: «Alto» por estar en una cuenta personal. Dueño: dueño y suplente definidos, ubicación en sitio de equipo | «Medio», condicionado a C-01 y a que se cree el registro de cambios (A13) | ❓ Depende de C-01 |

**Sin medir o sin cruzar** [Dueño]

- ❓ Los días y la duración de merch frente al Route Master (FR-023).
- ❓ SC-011 y SC-012: no tienen línea base.
- ❓ El significado en convenience de unas 24 columnas está solo en el archivo de mapeo (A08).

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

1. Guardar esta spec en un repositorio **privado** de la organización de Falcon (`data-sql`), en `specs/dsd-store-master/spec.md`, junto con el diccionario y los scripts de carga y de validación. [Inicial]
2. Proteger la rama `main`: la spec solo cambia con un pull request aprobado por el dueño (archivo CODEOWNERS). [Inicial]
3. Incluir un `CHANGELOG.md` con cada versión de la spec y una plantilla de pull request que pida actualizar la spec antes de cambiar columnas. [Inicial]
4. No guardar en el repositorio datos de personas ni de tiendas, solo la estructura, el diccionario y los scripts. [Inicial]
5. Registrar al dueño y a la suplente en `CODEOWNERS` y en el catálogo del repositorio de gobierno. [Inicial]
6. Mantener el archivo de mapeo de convenience y el diccionario en el mismo repositorio, versionados juntos. [Dueño · Inicial]

## Recomendaciones para migración a SQL

1. Partir de la réplica `sqldb-dsd-gold › DSDStoreMaster`: validar su contenido contra el archivo y documentar su dueño y su frecuencia (A03) antes de decidir motor y servidor. [Dueño] ⚠️ C-05
2. Llave primaria `Store Number WF`; una sola maestra de tiendas. [Dueño · Inicial]
3. Cargar primero en un área de paso (`stg`), limpiar y pasar a tablas con claves; Power BI y otros lectores leen solo vistas. [Inicial]
4. Exponer una vista con los **nombres actuales de las columnas** (incluida `ABC Clasification`, mal escrita) para que DSD Route Master y DSD_DisplayFill sigan funcionando. [Dueño]
5. Mantener la carga de convenience como un proceso aparte, con el mismo archivo de mapeo. [Dueño]
6. Definir quién actualiza cada tabla y con qué mecanismo (plantilla Excel validada o pantalla de mantenimiento), porque el responsable no es administrador de bases de datos. [Inicial]
7. Operar cuatro semanas en paralelo con el archivo en solo lectura, y archivarlo solo cuando no queden lectores. [Inicial]
8. Programar un respaldo diario y probar una restauración al mes. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 4 | Spec completa, con requisitos, criterios, reglas y plan |
| Responsables | 4 | Dueño y suplente definidos y operando; falta completar los accesos de la suplente |
| Operación documentada | 4 | Lista de verificación y mantenimiento por evento |
| Control de acceso | 3 | Cuenta y permiso; protección de hoja apagada y filtro guardado |
| Contrato de datos | 2 | 75 de 76 columnas descritas, sin tipos ni regla de cambio |
| Calidad y validación | 2 | Sin listas de validación; 118 celdas con error y ≈ 2.900 con texto en columnas numéricas |
| Automatización e integración | 2 | Reemplazo manual de convenience; carga SQL programada pero sin dueño documentado |
| Trazabilidad de cambios | 1 | Unos 40 días de versiones, sin detalle |
| Entornos y pruebas | 1 | Un solo archivo en producción; circulan copias |

**Nivel global: 2,6 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo.

## Anexo · Diccionario de datos (76 columnas)

Contiene el nivel de llenado por cliente y, al final, el mapeo de las columnas de convenience.

Nivel de llenado: **DSD activas** = tiendas activas de Walmart / Sprouts (incluye pendientes) / Michaels / Costco; **Conv.** = todas las filas de CVS / Walgreens / QuikTrip, cuyo significado por columna está en el Anexo, «Mapeo de columnas de convenience». El texto "NA" cuenta como lleno. *Doc* = equipo fuente y utilidad según el libro de documentación (Repl = Replenishment, Exec = Execution Team, OpsPerf = Operations Performance, Conv = Convenience).

| # | Columna | Doc | DSD activas % (WM/SP/MI/CO) | Conv. % (CVS/WAG/QT) | Notas |
|---|---------|-----|:---:|:---:|-------|
| 1 | Customer | Repl · Sí | 100/100/100/100 | 100/100/100 | 16 valores |
| 2 | Store Number WF | Repl · Sí | 100 | 100 | **Llave**, única |
| 3 | Customer Store Number | Repl · Sí | 100 | 100 | Número entero |
| 4 | Store Address | Repl · Sí | 100 | 100 | |
| 5 | City | Repl · Sí | 100 | 100 | |
| 6 | State | Repl · Sí | 100 | 100 | 1 espacio al final |
| 7 | Zip Code | Repl · Sí | 100 | 100 | ⚠️ Números y texto mezclados; ceros iniciales perdidos |
| 8 | Phone Number | Repl · Sí | 0/90/98/100 | 72/91/0 | Walmart sin teléfono |
| 9 | Latitude | Repl · Sí | 100 | 100 | A partir de la dirección |
| 10 | Longitude | Repl · Sí | 100 | 100 | A partir de la dirección |
| 11 | Store Size (SqFt) | Repl · Sí | 77/63/0/100 | 100/100/100 | Walmart: formato de tienda (excepción aceptada); Conv.: "WF Customer" |
| 12 | Store Manager | Exec · Sí | 0/0/97/56 | 100/87/99 | |
| 13 | Receiving Manager | Exec · Sí | 0/0/100/7 | 0/0/0 | Michaels = "Serving" |
| 14 | Merch Manager | Exec · Sí | 0/0/0/7 | 0 | |
| 15 | Receiving Window | Exec · Sí | 0/0/0/100 | 0 | Costco "2:00 AM - 8:30 AM" |
| 16 | Customer District (Sales) | Exec · Sí | 100 | 0 | ≈ nombre del territorio del DM |
| 17 | Region | Exec · Sí | 100 | 100/92/0 | DSD: región del RM; CVS/WAG: códigos numéricos |
| 18 | District | Exec · Sí | 100 | 0 | ≈ nombre del territorio del DM |
| 19 | Area | Exec · Sí | 100 | 100/92/0 | DSD: agrupación por ciudad; CVS/WAG: códigos numéricos |
| 20 | Zone | Exec · Sí | 98/100/100/100 | 100 | Zona del cliente (ej. "Durham II NC") |
| 21 | FF District Manager | Exec · Sí | 100 | 0 | 14 DMs |
| 22 | FF Field Supervisor | Exec · Sí | 100 | 15/18/100 | Valores escritos (lookups quitados el 2026-10-21) |
| 23 | Program Start date | Repl · Sí | 100 | 15/2/10 | Fecha |
| 24 | Program End date | Repl · Sí | 77/17/0/0 | 0 | ⚠️ Texto "NA" en una columna de fecha |
| 25 | Active | Exec · Sí | 100 | 0 | Y / P / N |
| 26 | Same Store | Exec · Sí | 100 | 15/19/100 | Fórmula en las filas 2–2.902; NEW / SS / NS / CLOSED |
| 27 | Service Model | Repl · Sí | 100/100/2/100 | 0 | DC / DSD |
| 28 | FF Facility | Repl · Sí | 100 | 9/20/100 | FFM Miami, FFG Georgia, FFT Texas, FFZ Arizona, FFC California, FFK Kentucky; "FF" (convenience) desconocido |
| 29 | ABC Clasification | Repl · Sí | 100/100/31/100 | 9/18/100 | AA, A–E, NA |
| 30 | Segmentation | Repl · Sí | 14/100/100/0 | 5/100/0 | ⚠️ Tres esquemas |
| 31 | Customer DC | Repl · Sí | 0/100/0/26 | 100 | |
| 32 | Store Pull Day Wk1 | Repl · Sí | 0/100/100/100 | 0 | Códigos de día; Michaels = Merch Days |
| 33 | Facility Departure Day Wk1 | Repl · Sí | 0/100/100/100 | 0 | Códigos de día |
| 34 | Store Arrival Day Wk1 | Repl · Sí | 0/100/0/100 | 0 | Códigos de día |
| 35 | Store Pull Day Wk2 | Retalon · No | 0 | 0 | No se usa |
| 36 | Facility Departure Day Wk2 | Retalon · No | 0 | 0 | No se usa |
| 37 | Store Arrival Day Wk2 | Retalon · No | 0 | 0 | No se usa |
| 38 | Display Size in Buckets | Repl · Sí | 78/100/0/100 | 9/18/99 | |
| 39 | Bunches per Bucket | Repl · Sí | 30/100/0/100 | 9/18/100 | Sprouts: con decimales (derivado) |
| 40 | Total Bunches per Store | Repl · Sí | 16/100/0/100 | 9/18/99 | = baldes × ramos |
| 41 | Merch Days | Exec · Sí | 100 | 9/18/100 | Del Route Master |
| 42 | Merch Visit Duration (mins) | Exec · Sí | 100/100/1/100 | 18/92/100 | Conv.: "24 Hours" |
| 43 | Merch Visits per day | Exec · No | 37/0/0/100 | 100 | ⚠️ Minutos en Walmart; Conv.: "Every Day Service" |
| 44 | FS Visit Duration (mins) | Exec · Sí | 0 | 9/18/100 | Conv.: "Stop #" |
| 45 | Back Cooler | Repl · Sí | 0/100/0/100 | 0 | "Y" o vacío |
| 46 | Display Location | Conv · Sí | 0 | 2/16/100 | ⚠️ 8 escrituras para 4 valores |
| 47 | Min amount of bunches in display Roses | Repl · Sí | 0/100/0/100 | 0 | El encabezado tiene un doble espacio |
| 48 | Min amount of bunches in display Mixes | Repl · Sí | 0/0/0/100 | 0 | El encabezado tiene un doble espacio |
| 49 | Min amount of bunches in display CB | Repl · Sí | 0/100/0/100 | 9/18/99 | El encabezado tiene un doble espacio |
| 50 | Virtual DC Retalon | Repl · Sí | 0/100/0/100 | 9/18/100 | |
| 51 | Route (Cstore ONLY) | Conv · No | 0/0/100/0 | 9/18/100 | También rutas del router de Michaels |
| 52 | Store Max Capacity | Conv · No | 0 | 9/18/100 | |
| 53 | VIP␣ | Repl · Sí | 0/4/0/0 | 1/2/6 | El encabezado termina en espacio; "VIP" o "Y" |
| 54 | Zona AFS | Repl · Sí | 100/100/1/100 | 0 | Walmart = "NA" |
| 55 | FF Regional Manager | Exec · Sí | 100 | 9/18/100 | 4 RMs DSD; Conv.: District Manager de convenience |
| 56 | FF Area Manager | Exec · No | 100/100/1/100 | 100/18/100 | DSD = "NA"; convenience: áreas de DC |
| 57 | SubRegion | Repl · No (eliminar) | 15/98/100/100 | 100/100/10 | ⚠️ La lee DSD Route Master: avisar antes de borrar |
| 58 | Customer District # | Repl · Sí | 0/99/0/100 | 92/92/0 | Formatos mezclados ("District 10", "TX", números) |
| 59 | BA | Repl · Sí | 0/82/0/100 | 15/19/100 | |
| 60 | Planned Visits | Exec · No sé | 6/0/0/0 | 9/18/100 | No se usa en DSD (dueño); Conv.: "Frequency" |
| 61 | Isolved Zone | OpsPerf · Sí | 100/100/0/100 | 0 | De iSolved |
| 62 | Zone name | OpsPerf · Sí | 100/100/0/100 | 19/20/100 | De iSolved |
| 63 | Location | OpsPerf · Sí | 100/100/0/100 | 100 | Location contable; convenience = "Convenience" |
| 64 | DC Arrival Day | Repl · Sí | 1/100/0/26 | 0 | "N/A" y "NA" |
| 65 | FF Regional Manager␣␣ | Exec · No | 100 | 0 | Espejo (fórmula); el encabezado termina en 2 espacios |
| 66 | FF Regional Manager Position | Exec · Sí | 100 | 0 | RM_East Coast, RM_Central, RM_West Coast, RM_South |
| 67 | FF District Manager2 | Exec · No | 100 | 0 | Espejo (fórmula) |
| 68 | FF District Manager Position | Exec · Sí | 100 | 0 | 13 posiciones DM_ + RM_South |
| 69 | FF Area Manager2 | Exec · No (Training) | 0/0/100/0 | 0 | Solo Michaels |
| 70 | FF Area Manager Position | Exec · No (Training) | 0 | 0 | Solo "NA" |
| 71 | FF Field Supervisor2 | Exec · No | 100 | 0 | Espejo (fórmula) |
| 72 | FF Field Supervisor Position | Exec · Sí | 100 | 0 | FS_<territorio>, 106 valores |
| 73 | FF Senior Sales Lead | Exec · No (eliminar) | 0 | 0 | Solo "NA" |
| 74 | FF Senior Sales Lead Position | Exec · No (eliminar) | 0 | 0 | Solo "NA" |
| 75 | Zona Horaria | Exec · Sí | 100 | 0 | IANA, API de Python |
| 76 | CVP - WM | *Sin documentar* | 100 | 100 | "Yes" = registrar inventario en esta tienda Walmart (217); "0" en el resto |

### Mapeo de columnas de convenience

Fuente: `Asignacion de Columnas Convenience.xlsx` (Sales Administration › General › Masters Changes). En las filas de convenience (CVS, Walgreens, QuikTrip), estas columnas del Store Master contienen el campo del Convenience Store Master que se indica. Las columnas que no aparecen quedan vacías en convenience.

| Columna del Store Master | Campo de Convenience | ¿Mismo significado? |
|--------------------------|----------------------|:---:|
| Customer · Store Number WF · Customer Store Number | Retailer · Store Number WF · Number | ✅ |
| Store Address · City · State · Zip Code · Phone Number · Latitude · Longitude | Mismos nombres | ✅ |
| Store Size (SqFt) | WF Customer (ej. "WALGREENS MIAMI") | ❌ |
| Store Manager | Store Manager Name | ✅ |
| Region · Area | Region · Area (códigos del cliente) | ❌ |
| Zone | Cluster | ❌ |
| FF Field Supervisor | FS | ✅ |
| Program Start date · Same Store | Program Start Date · Same Store | ✅ (NS sin definir) |
| FF Facility | DC/WF Falcon | ≈ |
| ABC Clasification | Store Type | ❌ |
| Segmentation | Store Description | ❌ |
| Customer DC | Cluster xxx | ❌ |
| Display Size in Buckets · Total Bunches per Store | Mismos nombres | ✅ |
| Bunches per Bucket | Display Type (AB) - Sales | ❌ |
| Merch Days | Days of Service | ≈ |
| Merch Visit Duration (mins) | 24 Hours (Y/N) | ❌ |
| Merch Visits per day | Every Day Service (YES/N/Closed) | ❌ |
| FS Visit Duration (mins) | Stop # | ❌ |
| Display Location · VIP · BA | Mismos nombres | ✅ |
| Min amount of bunches in display CB | Cantidad de Displays | ❌ |
| Virtual DC Retalon | Route_ID_WF | ❌ |
| Route (Cstore ONLY) | Route_ID_AFS | ≈ |
| Store Max Capacity | Route | ❌ |
| FF Regional Manager | District Manager (convenience) | ❌ |
| FF Area Manager | DC | ❌ |
| SubRegion | County | ❌ |
| Customer District # | District | ≈ |
| Planned Visits | Frequency | ≈ |
| Zone name | Customer_ID | ❌ |
| Location | Channel ("Convenience") | ❌ |

**Cambios seguros:** agregar una columna al final; cambiar valores que mantienen su tipo. **Cambios que requieren avisar a los dueños de los archivos dependientes:** renombrar o borrar una columna (incluidas las marcadas "Eliminar"), renombrar la tabla `StoreMaster`, mover el archivo o escribir texto en columnas de número o fecha.
