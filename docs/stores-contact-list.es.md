# Spec · Stores Contact List

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m23 (inventario MIC) |
| Tipo | Base de datos: libro de Excel (maestro de contactos de las tiendas activas) |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos), el análisis inicial del equipo MIC y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Independiente]** análisis independiente · ❓ por confirmar. Esta herramienta todavía no tiene análisis inicial del equipo MIC, por eso no hay contradicciones que resolver.

## Resumen Ejecutivo

Es el **maestro de contactos** de las tiendas activas. Cada fila de la hoja `Contact List` es una tienda con su dirección y, para su RM, su DM y su FS, el nombre, el correo y el teléfono. La hoja `People` guarda el correo y el teléfono de cada persona. Es pequeño (2.557 filas × 11 columnas y 122 personas), pero el **DSD Route Master lo lee** para tener el contacto de cada parada. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 2.557 tiendas × 11 columnas · 122 personas × 3 columnas | Dueño |
| Clientes | Walmart 1.785 · Sprouts 512 · Michaels 169 · Costco 91 | Dueño |
| Jerarquía | 4 RMs · 14 DMs · 105 FS | Dueño |
| Cobertura | 2.557 de 2.617 tiendas activas (97,7 %); faltan 60 en la versión 286.0 y quedan 4 Michaels en la 287.0 | Dueño |
| Concordancia con el Store Master | RM, DM y FS iguales en las 2.557 filas (100 %) | Dueño |
| Libro | 3 hojas (1 oculta) · 25.569 fórmulas · 2 vínculos externos · 27 hipervínculos | Dueño |
| Actividad | 285 versiones: dueño 206 · suplente 7 · otras 7 personas 72 | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Bajo | Dueño (nivel propuesto) |

**Hallazgos principales**

1. 🟠 **Alcance y tiendas que faltan:** el dueño definió solo Walmart, Sprouts, Michaels y Costco con `Active = Y`; en la versión 287.0 agregó las 28 Walmart y quedan 4 Michaels por agregar. [Dueño]
2. 🟠 **El contacto faltante se ve como `0`,** no como un error: las 10 fórmulas terminan en `XLOOKUP(…,0)` y el Route Master repite el patrón (479 de sus 3.664 filas con algún contacto en 0 en la versión 286.0). [Dueño]
3. 🟠 **Lectura por letra de columna en ambos sentidos:** si alguien inserta o mueve una columna, nada da error y se entregan otros datos. [Dueño]
4. 🟠 **Más personas guardan versiones** de las que se describieron; el dueño bloqueará las hojas para que los demás solo visualicen. [Dueño]
5. 🟠 **Todo depende de una persona** y de un procedimiento no escrito (72 % de las versiones). [Dueño]

**Funciona bien:** **Jerarquía:** RM, DM y FS coinciden con el Store Master vivo en las 2.557 filas; cada DM tiene un solo RM y cada FS un solo DM. **Tiendas:** ninguna repetida ni inactiva; Costco cubierto 91 de 91. **`People` limpia:** las 122 personas tienen puesto activo (nadie sobra), sin nombres, correos ni teléfonos repetidos, y todos los correos son del dominio de la empresa (salvo el `N/A`). **Direcciones:** las 2.557 tienen valor; 2.517 son idénticas a las del Store Master y 40 solo difieren en el cero inicial. [Dueño]

**Contradicciones:** ninguna (no hay análisis inicial con el que contrastar).

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (SCL-A01, SCL-A02, SCL-A03, SCL-A04, SCL-A05, SCL-A06, SCL-A23). El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Tener en un solo libro el contacto (nombre, correo y teléfono) del RM, DM y FS de cada tienda activa, y que el DSD Route Master lo lea para mostrar el contacto de cada parada.

- **Problema que resuelve:** el Route Master y las personas de Execution Team y de HR (talento) necesitan saber a quién llamar en cada tienda. [Dueño]
- **Qué logra:** una fila por tienda con dirección y contactos, armada con fórmulas desde el Store Master, el Route Master y la hoja `People`. [Dueño]
- **Éxito:** todas las tiendas activas tienen fila y contactos completos, y ningún cambio de columnas rompe al Route Master (ver «Criterios de éxito»). [Dueño]

## Alcance

**Incluye** [Dueño]: el libro, el proceso que lo mantiene (alta de tiendas y mantenimiento de `People`) y los archivos que lo leen.

**No incluye** [Dueño]: el Store Master y el Route Master, que ya tienen su análisis y aquí son dependencias; Walgreens y CVS quedan fuera.

**Futuro** [Dueño]: una fuente corporativa de contactos (SCL-A17), un aviso automático de cambios de puesto (SCL-A18) y protección de columnas (SCL-A19).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Responsable (el dueño) | Es el único editor, según su descripción; mantiene `Contact List` y `People` | 206 de 285 versiones | Dueño |
| Suplente | Cubre al responsable | 7 versiones | Dueño |
| DSD Route Master (y sus dos copias) | Lee las columnas D, E, G, H, J y K de `Contact List`, por letra | — | Dueño |
| Execution Team y HR (talento) | Consultan los contactos | — | Dueño |
| Otras personas con versiones | Según el dueño, solo visualizaron o filtraron | 72 versiones | Dueño |

**Acceso**

- Está en SharePoint › Sales Administration › Consulta Route Master › Varios, con permisos propios; su lista no se pudo leer. [Dueño]
- El dueño bloqueará las hojas para que los demás solo visualicen. [Dueño]
- ❓ Falta la lista de editores y quién aprueba los accesos nuevos (SCL-A01). [Dueño]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño]

- Es el único editor según su descripción: agrega las tiendas activas y mantiene la hoja `People`.
- Define el alcance de la lista (4 clientes, solo `Y`).
- Aprobó su análisis el 2026-10-21 (v1.3).

## Administrador técnico

**Jeronimo Sanchez.** [Dueño]

- Administra el libro en SharePoint y sus permisos propios.
- ❓ Quién aprueba los accesos nuevos (SCL-A01).

## Suplente

**Jennifer Guarin.** [Dueño] Tiene 7 versiones entre junio y agosto; falta verificar sus accesos al Store Master y al Route Master y escribir el procedimiento.

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| `Stores Contact List.xlsx` | Editar el libro | ⬜ Por verificar (SCL-A01) |
| Store Master y Route Master | Leerlos desde las fórmulas | ⬜ Por verificar (SCL-A01) |
| Procedimiento escrito | Seguirlo sin ayuda | ⬜ Pendiente (SCL-A03) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| DSD Store Master | Nombre del RM, DM y FS de cada tienda | Dueño | Dueño |
| Hoja `StoreMaster DSD` del DSD Route Master | Dirección de cada tienda | Dueño | Dueño |
| Hoja `People` | Correo y teléfono de cada persona | El dueño, a mano, desde Onboarding, los DM y RM y avisos por email | Dueño |
| Onboarding, DM y RM, IT | Teléfonos, avisos de cambios y creación de correos | Cada equipo | Dueño |

**Cómo se alimenta** [Dueño]

1. Solo `Store` se escribe a mano: cuando se activa una tienda en el Store Master, se copia al final de la tabla.
2. Las otras 10 columnas son `XLOOKUP`: el nombre sale del Store Master, la dirección del Route Master y el correo y teléfono de `People`.
3. `People` se mantiene a mano: se borra a quien se va, se agrega a quien llega y se actualizan correos y teléfonos según los avisos. Si IT aún no creó el correo, queda `N/A`.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | SharePoint · Excel |
| Archivos | Store Master · DSD Route Master · hoja `People` |
| Personas | El dueño y su suplente · Onboarding y los avisos de DM y RM · IT |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| DSD Route Master y sus dos copias | Leen `Contact List` columnas D, E, G, H, J y K por su letra | Dueño del DSD Route Master |
| Execution Team y HR (talento) | Consultan los contactos | — |

## Procesos operativos

[Dueño] Cada vez que se activa una tienda, llega o se va una persona, o cambia un correo o teléfono.

1. **Tienda nueva:** confirmar en el Store Master que está activa y que tiene RM, DM y FS; copiar su `Store` al final de `Contact List`; confirmar que sus 10 columnas quedaron llenas.
2. **Persona nueva:** agregar a `People` con el nombre **exactamente como en el Store Master** ("Apellido, Nombre", sin espacios dobles), el teléfono en un solo formato y el correo; si IT aún no lo crea, escribir `N/A` y anotar la fecha para cerrarlo.
3. **Persona que se va:** borrarla de `People` después de que el Store Master ya no la use.
4. **Cambio de correo o teléfono:** actualizar `People` y anotar quién lo pidió y cuándo.
5. **Revisar:** sin `0`, sin celdas vacías en las 10 columnas y sin `N/A` pendientes.
6. **Avisar:** al dueño del Route Master antes de cambiar el orden o la letra de cualquier columna.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- Solo entran tiendas de Walmart, Sprouts, Michaels y Costco con `Active = Y`; las `P` son tiendas por abrir y no entran todavía.
- La dirección sale del Route Master a propósito, porque su consulta la concatena y organiza.
- Los 40 códigos postales sin cero inicial se dejan así.
- Solo el dueño edita; los demás visualizan o filtran.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Tienda activa** | Tienda del Store Master con `Active` = `Y` de Walmart, Sprouts, Michaels o Costco. `P` = tienda por abrir: no entra todavía (3 Sprouts en `P` se dejaron porque se activan la próxima semana) |
| **Store** | Identificador de la tienda en el Store Master (`119Sprouts`, `3501Walmart`). Única columna manual y llave de las búsquedas |
| **RM, DM, FS** | Regional Manager (4), District Manager (14) y Field Supervisor (105) de cada tienda, según el Store Master |
| **People** | Hoja con nombre, correo y teléfono de cada persona en un puesto de RM, DM o FS (122) |
| **`N/A` en el correo** | La persona ya está en el Store Master y se sabe su teléfono, pero IT aún no creó su correo (hoy 1 persona, 30 tiendas) |
| **`0` en un contacto** | Lo que devuelve la fórmula si no encuentra a la persona o la tienda; no es un dato |
| **Dirección** | `Store Address, City, State, Zip`, armada en la hoja `StoreMaster DSD` del Route Master |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | La lista MUST tener una fila por tienda de Walmart, Sprouts, Michaels y Costco con `Active = Y` | Must Have | ⚠️ Faltan 4 Michaels (SCL-A04) | Dueño |
| FR-02 | El RM, DM y FS de cada fila MUST coincidir con el Store Master | Must Have | ✅ 2.557 de 2.557 | Dueño |
| FR-03 | El contacto faltante MUST mostrarse con un texto claro, no con `0` | Must Have | ❌ (SCL-A07) | Dueño |
| FR-04 | Las búsquedas MUST hacerse por nombre de columna y debe existir la lista de columnas que lee el Route Master | Must Have | ❌ Lectura por letra en ambos sentidos (SCL-A08) | Dueño |
| FR-05 | `People` MUST tener nombres como en el Store Master y un formato único de teléfono | Should Have | ❌ 5 formatos; 36 teléfonos como texto (SCL-A10, SCL-A11) | Dueño |
| FR-06 | Solo el dueño MUST poder editar las hojas | Must Have | ⚠️ Más personas guardan versiones (SCL-A01) | Dueño |
| FR-07 | Se MUST avisar al dueño del Route Master antes de mover columnas | Must Have | ❌ (SCL-A15) | Dueño |
| FR-08 | El mantenimiento MUST seguir un procedimiento escrito y dejar registro de cambios | Should Have | ❌ (SCL-A03, SCL-A13) | Dueño |
| FR-09 | Una hoja `Control` MUST mostrar tiendas sin fila, contactos en `0` o `N/A` y personas sin puesto | Should Have | ❌ (SCL-A05) | Dueño |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Tiendas con `Active = Y` de los 4 clientes sin fila | 4 (Michaels) | 0 | Dueño |
| SC-02 | Filas del Route Master con algún contacto en 0 (versión 286.0) | 479 de 3.664 (30 tiendas) | 0 | Dueño |
| SC-03 | Tiendas con correo `N/A` | 30 (1 persona) | 0 al crear IT el correo | Dueño |
| SC-04 | Formatos de teléfono | 5 | 1 | Dueño |
| SC-05 | Personas que editan | Varias guardan versiones | El dueño y su suplente | Dueño |
| SC-06 | Concordancia de RM, DM y FS con el Store Master | 100 % | 100 % | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Nombres, correos y teléfonos de empleados; permisos propios con lista no leída; más personas guardan versiones | Dueño (nivel propuesto) |
| Estabilidad | Alto | Dos archivos se leen por letra de columna, el contacto faltante se ve como 0 y todo depende de una persona sin procedimiento | Dueño (nivel propuesto) |
| Escalabilidad | Bajo | 2.557 filas × 11 columnas y 122 personas | Dueño (nivel propuesto) |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🟠 Alta | **Alcance de la lista y tiendas que faltan.** El dueño definió: solo Walmart, Sprouts, Michaels y Costco, y solo `Active` = `Y` (las `P` son tiendas por abrir y no se ponen todavía). En la 286.0 faltaban 60 tiendas; con esa regla eran 32. **En la 287.0 el dueño agregó las 28 Walmart; quedan 4 Michaels en `Y`**, las 4 son `9876Michaels`, `9811Michaels`, `8387Michaels` y `8385Michaels`. Las 3 Sprouts en `P` (50, 58, 185) ya están en la lista y **se dejan** porque se activan la próxima semana. Walgreens y CVS (26) quedan fuera. | Dueño |
| R2 | 🟠 Alta | **El contacto faltante se ve como `0`, no como un error.** Las 10 fórmulas terminan en `XLOOKUP(…,0)` y el Route Master repite el patrón: con la 286.0 había **479 de sus 3.664 filas (30 tiendas)** con algún contacto en 0 (28 tiendas Walmart que no estaban en la lista, 1 que no existe y 1 por la celda vacía del hallazgo 7; ya corregidas en la 287.0), y 27 filas (24 tiendas) tienen `N/A` en el correo del FS. | Dueño |
| R3 | 🟠 Alta | **Lectura por letra de columna en ambos sentidos.** El Route Master lee `'Contact List'!D, E, G, H, J, K`; este libro lee el Store Master (`B`, `BC`, `U`, `V`) y el Route Master (`B`, `BY`). Si alguien inserta o mueve una columna, nada da error y se entregan otros datos. | Dueño |
| R4 | 🟠 Alta | **Más personas guardan versiones de las que se describieron** (el dueño dice que solo visualizaron o filtraron, y bloqueará las hojas). otra persona (41, 10 en los últimos 30 días), otra persona (18, todas desde 2026-09-29), otra persona, otra persona, otra persona y otra persona, además de Jennifer Guarin (7). El archivo tiene permisos propios y su lista no se pudo leer. | Dueño |
| R5 | 🟠 Alta | **40 códigos postales pierden el cero inicial** (`NJ, 8096` en lugar de `NJ, 08096`): el 100 % de las tiendas con código que empieza en 0. La dirección sale del Route Master a propósito (su consulta concatena y organiza la dirección completa), pero ahí el código postal se arma como número; en el Store Master está bien escrito. | Dueño |
| R6 | 🟠 Alta | **Dependencia cruzada entre dos archivos.** El Contact List lee la dirección del Route Master y el Route Master lee los contactos del Contact List. Como la dirección sale de la copia del Store Master del Route Master (2.592 tiendas), una tienda que aún no esté en esa copia saldría con dirección `0` aunque esté en la lista. | Dueño |
| R7 | 🟡 Media | **Un hipervínculo mal escrito y hipervínculos sueltos.** La celda vacía de la fila 114 (`Regional Email`) ✅ ya la corrigió el dueño (287.0); 27 hipervínculos `mailto:` puestos a mano (4 RM, 3 DM, 20 FS) conviven con 2.530 celdas sin él, y uno apunta a `falconfarm.com`. | Dueño |
| R8 | 🟡 Media | **Teléfonos en 5 formatos y 2 tipos.** En `People` 86 son números y 36 son texto; la lista entrega 6.774 sin formato, 424 con guiones, 397 con paréntesis, 56 con espacio y 20 con paréntesis pegado. | Dueño |
| R9 | 🟡 Media | **30 filas con correo `N/A`:** todas de un FS (IT aún no le crea el correo). El `N/A` se arrastra al Route Master. | Dueño |
| R10 | 🟡 Media | **Hoja oculta `Sheet1`** (2.533 filas y una tabla dinámica de 14 DMs): ninguna fórmula ni archivo revisado la lee; el dueño la usa a mano para sacar rápido los correos de los DM. No se borra; hay que documentarla. | Dueño |
| R11 | 🟡 Media | **Nombres y correos irregulares:** un nombre con espacio doble (`un FS`, igual en el Store Master) y 11 correos que no contienen nombre y apellido (apodos y apellidos compuestos); uno de ellos pertenece a otro nombre (por confirmar). | Dueño |
| R12 | 🟠 Alta | **Todo depende de una persona y de un procedimiento no escrito.** El dueño hizo el 72 % de las versiones; no hay lista de verificación ni registro de cuándo cambió cada contacto. | Dueño |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Agregar las 4 Michaels, bloquear las hojas, corregir el hipervínculo, escribir el procedimiento y crear la hoja `Control` | Lista completa y controlada | SCL-A01, SCL-A03, SCL-A04, SCL-A05, SCL-A06 | Dueño |
| Corto plazo | Cambiar el `0` por un texto claro, buscar por nombre de columna, leer la dirección del Store Master y unificar teléfonos | Menos errores silenciosos | SCL-A07, SCL-A08, SCL-A09, SCL-A10 | Dueño |
| Mediano plazo | Validaciones en `People`, diccionario, registro de cambios y revisión de `Sheet1` | Datos limpios y trazables | SCL-A11 a SCL-A16 | Dueño |
| Largo plazo | Evaluar una fuente corporativa de contactos, avisos automáticos y protección de columnas | Menos trabajo manual | SCL-A17, SCL-A18, SCL-A19 | Dueño |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| SCL-A01 | Verificar accesos de Jennifer Guarin y la lista de editores | P0 | Dueño y suplente | Dueño | T-001 |
| SCL-A02 | Publicar el documento y el diccionario | P0 | Dueño | Dueño | T-002 |
| SCL-A03 | Procedimiento escrito | P0 | Dueño | Dueño | T-003 |
| SCL-A04 | Agregar las 4 Michaels en `Y` y escribir la regla (4 clientes, solo `Y`) | P0 | Dueño | Dueño | T-004 |
| SCL-A05 | Hoja `Control` | P0 | Dueño | Dueño | T-005 |
| SCL-A06 | Hipervínculo mal escrito (la fila 114 ya está corregida) | P0 | Dueño | Dueño | T-006 |
| SCL-A07 | Cambiar el `0` por un texto claro | P1 | Dueño | Dueño | T-008 |
| SCL-A08 | Búsquedas por nombre de columna y lista de columnas que lee el Route Master | P1 | Dueño | Dueño | T-009 |
| SCL-A09 | Leer la dirección del Store Master | P1 | Dueño | Dueño | T-010 |
| SCL-A10 | Formato único de teléfono | P1 | Dueño | Dueño | T-011 |
| SCL-A11 | Validaciones en `People` | P1 | Dueño | Dueño | T-012 |
| SCL-A12 | Diccionario | P1 | Dueño | Dueño | T-013 |
| SCL-A13 | Registro de cambios | P1 | Dueño | Dueño | T-014 |
| SCL-A14 | Revisar `Sheet1` | P1 | Dueño | Dueño | T-015 |
| SCL-A15 | Avisar a los dueños de los archivos que lo leen | P1 | Dueño | Dueño | T-016 |
| SCL-A16 | Revisar trimestralmente a los editores | P1 | Dueño | Dueño | T-017 |
| SCL-A17 | Evaluar una fuente corporativa de contactos | P2 | Dueño | Dueño | T-018 |
| SCL-A18 | Aviso automático de cambios de puesto | P2 | Dueño | Dueño | T-019 |
| SCL-A19 | Protección de columnas | P2 | Dueño | Dueño | T-020 |
| SCL-A20 | Hacer la revisión técnica con IT: nombres, correos y teléfonos de empleados | P1 | IT | Dueño (nivel propuesto) | — |
| SCL-A21 | Hacer el análisis inicial del equipo MIC de esta herramienta, para contrastarlo con el del dueño | P1 | Equipo MIC | — | — |
| SCL-A22 | Guardar esta spec en un repositorio privado de GitHub de Falcon | P1 | PM | Instructivo de GHT | — |
| SCL-A23 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-06 | hoja `Sheet1` (respondida) | Dueño (se resuelve con su tarea) | Dueño |
| Q-07 | hipervínculos | Dueño (se resuelve con su tarea) | Dueño |
| Q-08 | correos sin nombre y apellido | Dueño (se resuelve con su tarea) | Dueño |
| Q-09 | formato de teléfono | Dueño (se resuelve con su tarea) | Dueño |
| Q-10 | plazo del `N/A` | Dueño (se resuelve con su tarea) | Dueño |
| Q-11 | dónde se guardan los avisos de cambio | Dueño (se resuelve con su tarea) | Dueño |
| Q-12 | un RM que también figura como DM, y columnas BC/U/V frente a BM/BO/BS | Dueño (se resuelve con su tarea) | Dueño |

## Información pendiente por confirmar


**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, fórmulas y vínculos, calidad de datos y backlog completo) todavía no están integrados.
- La distribución de tiendas por RM y DM está en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/stores-contact-list/spec.md`. [Dueño]
- Describir en el repositorio las columnas que lee el DSD Route Master (D, E, G, H, J y K), sin correos ni teléfonos de personas. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Dueño]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Dueño]

## Recomendaciones para migración a SQL

1. Una tabla de contactos de tienda con clave `Store` y una tabla de personas (`People`) con puesto, correo y teléfono. [Dueño]
2. Que el Route Master lea una vista con los nombres de columna actuales y no por letra (SCL-A08). [Dueño]
3. Poblar la tabla desde el Store Master en SQL (una sola fuente de tiendas, jerarquía y dirección). [Dueño]
4. Mostrar el contacto faltante como un valor nulo con una regla de calidad, no como `0` (SCL-A07). [Dueño]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 2 | Dueño y suplente definidos; la suplente tiene pocos accesos |
| Operación documentada | 2 | Lista de verificación propuesta; procedimiento no escrito |
| Control de acceso | 2 | Permisos propios; más personas guardan versiones |
| Contrato de datos | 1 | Lectura por letra de columna; sin diccionario |
| Calidad y validación | 2 | Concordancia del 100 % con el Store Master; `0` y `N/A` sin control |
| Automatización e integración | 3 | Casi todo son fórmulas; solo `Store` y `People` son manuales |
| Trazabilidad de cambios | 1 | Sin registro de cuándo cambió cada contacto |
| Entornos y pruebas | 2 | Hay copias del Route Master que también lo leen |

**Nivel global: 2,0 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis inicial del equipo MIC, el análisis completo del dueño y el análisis independiente.
