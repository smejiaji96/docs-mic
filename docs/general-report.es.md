# Inventario de herramientas MIC · Reporte general (español)

Principios, qué se necesita, plan, tareas, glosario y plan de acción. Versión 1.14. No contiene nombres de personas, correos, teléfonos, tarifas ni enlaces; es información interna.

## Contenido

1. Principios del proyecto (constitución): mic-tools-governance
2. Qué se necesita (especificación): Gobierno de las herramientas MIC: acceso seguro y actualización confiable
3. Plan: cómo se hace: Gobierno de las herramientas MIC: acceso seguro y actualización confiable
4. Tareas: Gobierno de las herramientas MIC: acceso seguro y actualización confiable
5. Glosario en palabras simples
6. Plan de acción para cargar la lista de trabajo: 001-secure-reliable-mic-tools

---

# Principios del proyecto (constitución): mic-tools-governance

## Para qué sirve

Estos son los principios que gobiernan el proyecto mic-tools-governance. Toda la especificación, el plan y las tareas deben respetarlos. Una excepción necesita una justificación escrita en el plan.

## Punto de partida (cómo estamos hoy)

- Los enlaces de los dashboards de Power BI que existen hoy son públicos: cualquier persona que tenga el enlace puede abrirlos, sin cuenta.
- Los formularios también los puede abrir y responder cualquiera que tenga el enlace.
- Costo de servir es el único dashboard al que se entra por un Portal, y solo pueden entrar quienes tienen acceso a ese Portal.
- Las bases de datos en Excel, en SharePoint, sí piden cuenta de la empresa y permiso.
- Solo pueden publicar enlaces en la web las personas con acceso a Power BI (Power BI Pro); es un permiso limitado.

---

## Principio I: Entrar con la cuenta de la empresa

Quien entra a una herramienta con información sensible lo hace con su cuenta de la empresa (correo Falcon Farms).

**Qué implica:**
- Si algo debe ser público, se justifica y se aprueba.
- Los gerentes y demás usuarios ven toda la información de sus dashboards. No se limita lo que ve cada persona.
- Los comentarios escritos libremente nunca se publican.

---

## Principio II: Datos en un lugar de la empresa

Los datos viven en un lugar de la empresa, con dueño y permisos revisados; nunca en la cuenta personal de alguien.

**Qué implica:**
- Hay una sola lista maestra de tiendas.
- Las bases de datos en Excel pueden pasarse a un servidor, por seguridad (sugerencia).

---

## Principio III: Información al día

Cada reporte se actualiza solo y muestra cuándo; cada archivo anota cuándo y quién lo actualizó.

**Qué implica:**
- Actualizar a mano solo vale como excepción anotada.
- Si una actualización falla, se avisa al dueño y a su suplente.

---

## Principio IV: Responsables

Cada herramienta tiene un dueño y un suplente, ambos personas.

**Qué implica:**
- Un equipo o departamento no puede ser el único responsable.
- Hay un plan para cuando cambie el dueño, el creador o la licencia.

---

## Principio V: Documentar y cambiar con orden

Cada herramienta tiene su ficha al día en 7 temas, y los cambios se escriben antes de hacerse.

**Qué implica:**
- Cada dato se marca como verificado, deducido, pendiente o sugerencia; los pendientes se revisan cada trimestre.
- Estos documentos no llevan nombres de personas, correos, teléfonos ni tarifas.

---

## Herramientas aprobadas

### Lista aprobada
| Tema | Herramienta | ¿Requiere aprobación para cambiarla? |
|---|---|---|
| Reportes | Power BI | Sí |
| Entrar con cuenta de la empresa | Cuentas de la empresa (Microsoft) | Sí |
| Formularios | Microsoft Forms | No |
| Bases de datos maestras | Servidor de base de datos (sugerido); hoy Excel en SharePoint | No |
| Lista de trabajo | Azure DevOps o GitHub (por decidir) | Por decidir |

### Cómo se cambia una herramienta

Cambiar una herramienta aprobada requiere:
1. Una nota breve con la decisión y el motivo
2. Revisar qué partes de la especificación se afectan
3. Actualizar los principios si el cambio los toca

---

## Cambios a los principios

| # | Date | Qué cambió | Por qué |
|---|---|---|---|
| 1 | 2026-10-13 | Principios iniciales | Inicio del proyecto |
| 2 | 2026-10-13 | Identidad esperada: cuentas con dominio de la empresa (por verificar) | Respuestas de aclaración |

---

# Qué se necesita (especificación): Gobierno de las herramientas MIC: acceso seguro y actualización confiable

## Resumen

**Nombre:** Gobierno de las herramientas MIC: acceso seguro y actualización confiable
**Número:** 001
**Fecha:** 2026-10-13
**Autor:** Generado a partir de la documentación del inventario MIC
**Estado:** Borrador

### Qué problema hay

Los dashboards, formularios y bases de datos del inventario MIC tienen información sensible y clave para la operación, pero algunos son públicos para cualquiera con el enlace, parte de la información se actualiza a mano y varios archivos o herramientas dependen de una sola persona o de una cuenta personal.

### Qué se propone

Que cada herramienta tenga acceso controlado, información que se actualiza sola y a la vista, dueño y suplente registrados, y fuentes ordenadas, para que el equipo confíe en las cifras y la operación no dependa de una persona.

### Para quién

- Responsable del inventario: coordina la documentación y los cambios.
- Administrador de herramienta: mantiene un dashboard, formulario o archivo.
- Consumidor de reportes: gerentes, supervisores y equipos que usan los dashboards.
- Equipo de TI y de BI: aprueba cambios de acceso y de plataforma.

---

## Necesidades de las personas

### US-001: Acceso seguro a los dashboards
Como persona de la empresa que usa los dashboards, quiero entrar con mi cuenta de la empresa, para que la información de la operación no esté abierta a cualquiera.

**Cómo se comprueba:**
- Dado un dashboard con información sensible, Cuando alguien abre su enlace sin haber iniciado sesión, Entonces no puede ver el contenido
- Dado una persona con cuenta de la empresa, Cuando abre el dashboard con su cuenta, Entonces puede ver el contenido

**Cómo probarlo por separado:** Abrir cada dashboard en una ventana privada y confirmar que pide inicio de sesión.
**Prioridad:** Imprescindible (Must Have)

### US-002A: Actualización automática y visible
Como persona que consulta los reportes, quiero que cada reporte se actualice solo y muestre cuándo se actualizó, para que pueda confiar en que las cifras están al día.

**Cómo se comprueba:**
- Dado un reporte con programación, Cuando llega la hora programada, Entonces sus datos se actualizan sin intervención manual
- Dado un reporte abierto, Cuando se mira su encabezado, Entonces muestra la fecha y hora de su última actualización

**Cómo probarlo por separado:** Revisar que cada reporte se actualice solo y muestre su fecha y hora.
**Prioridad:** Imprescindible (Must Have)

### US-002B: Aviso si una actualización falla
Como dueño de una herramienta, quiero enterarme si una actualización falla, para que pueda corregirla antes de que alguien use cifras viejas.

**Cómo se comprueba:**
- Dado una actualización que falla, Cuando termina con error, Entonces el dueño y su suplente reciben un aviso
- Dado el historial de actualización, Cuando se revisa con el administrador, Entonces se sabe si hubo fallas

**Cómo probarlo por separado:** Provocar una falla de prueba y confirmar que llega el aviso.
**Prioridad:** Imprescindible (Must Have)

### US-003A: Dueño registrado
Como responsable del inventario, quiero que cada herramienta tenga su dueño registrado (su creador), para que se sepa quién responde por ella.

**Cómo se comprueba:**
- Dado una herramienta del inventario, Cuando se consulta su ficha, Entonces muestra un dueño que es una persona

**Cómo probarlo por separado:** Revisar las 17 fichas y confirmar que todas tienen dueño.
**Prioridad:** Imprescindible (Must Have)

### US-003B: Suplente registrado
Como responsable del inventario, quiero que cada herramienta tenga un suplente registrado, para que la continuidad no dependa de una sola persona.

**Cómo se comprueba:**
- Dado una persona deja su rol, Cuando se asigna a su reemplazo, Entonces la herramienta sigue operando sin perder acceso

**Cómo probarlo por separado:** Revisar las 17 fichas y confirmar que todas tienen suplente.
**Prioridad:** Imprescindible (Must Have)

### US-004: Fuentes de datos ordenadas
Como analista de datos, quiero las bases de datos maestras en un lugar de la empresa, con una sola lista maestra de tiendas, para que las cifras coincidan y no se pierdan archivos clave.

**Cómo se comprueba:**
- Dado un archivo maestro, Cuando se consulta su ubicación, Entonces está en un sitio de equipo, no en una cuenta personal
- Dado dos reportes que usan la maestra de tiendas, Cuando se compara el mismo dato, Entonces ambos muestran el mismo valor

**Cómo probarlo por separado:** Confirmar la ubicación y los permisos de los 4 archivos y comparar un dato de la maestra en dos reportes.
**Prioridad:** Importante (Should Have)

### US-005: Formularios controlados
Como administrador de un formulario, quiero que solo responda gente de la empresa y que las respuestas tengan un destino, para que no haya respuestas falsas ni se pierdan respuestas.

**Cómo se comprueba:**
- Dado un formulario limitado a cuentas de la empresa, Cuando alguien sin cuenta de la empresa intenta responder, Entonces no puede enviar la respuesta
- Dado un formulario con respuestas, Cuando se consulta dónde se guardan, Entonces existe un destino y un tiempo de retención definidos

**Cómo probarlo por separado:** Intentar responder cada formulario desde una cuenta que no sea de la empresa y desde una que sí lo sea.
**Prioridad:** Importante (Should Have)

### US-006: Definiciones compartidas
Como analista de datos, quiero un glosario con las definiciones de las cifras clave, para que todos las interpreten igual.

**Cómo se comprueba:**
- Dado una cifra clave de un reporte, Cuando se busca su definición, Entonces existe una definición escrita y una fórmula documentada

**Cómo probarlo por separado:** Elegir 5 cifras clave y verificar que cada una tenga definición y fórmula.
**Prioridad:** Importante (Should Have)

---

## Lo que debe cumplir (requisitos)

### Acceso

**FR-001:** El sistema DEBE exigir entrar con una cuenta de la empresa (correo Falcon Farms) para ver cualquier reporte con datos del personal o de la operación; no se crean grupos por rol.
**FR-002:** El sistema DEBE unificar en un solo sitio los enlaces de las herramientas y retirar los enlaces públicos directos; ningún dashboard queda público por diseño.
**FR-003:** El sistema DEBE ocultar o restringir las páginas con comentarios de texto libre.
**FR-004:** El sistema DEBE seguir dando a los gerentes y demás usuarios acceso a toda la información de sus dashboards, sin limitar lo que ve cada persona.
**FR-005:** El sistema DEBERÍA eliminar las páginas duplicadas u ocultas que no tengan un propósito documentado.

### Actualización

**FR-006:** El sistema DEBE actualizar cada reporte por programación definida.
**FR-007:** El sistema DEBE mostrar en cada reporte la fecha y hora de su última actualización.
**FR-008:** El sistema DEBE avisar al dueño y a su suplente cuando una actualización falle.

### Responsabilidad y documentación

**FR-009:** Cada herramienta DEBE tener su dueño registrado (su creador).
**FR-010:** Cada herramienta DEBE tener un suplente registrado, que sea una persona.
**FR-011:** El sistema DEBE mantener la documentación de las 7 áreas por herramienta.
**FR-012:** El sistema DEBERÍA mantener un glosario con las definiciones y fórmulas de las cifras clave.

### Datos y formularios

**FR-013:** El sistema DEBE mantener cada base de datos maestra en un lugar controlado por la empresa, nunca en una cuenta personal, con permisos revisados. Se sugiere pasarlas a un servidor, por seguridad.
**FR-014:** El sistema DEBERÍA mantener una sola lista maestra de tiendas y retirar las copias.
**FR-015:** El sistema DEBE limitar quién puede responder cada formulario a personas con una cuenta de la empresa.
**FR-016:** El sistema DEBE definir el destino y el tiempo de guardado de las respuestas de cada formulario.

---

## De qué cosas habla este documento

Herramienta: Dashboard, formulario, base de datos en Excel o aplicación del inventario, con un tipo, un uso y un estado.
Reporte: Una herramienta de tipo dashboard, compuesta por páginas, algunas ocultas.
Fuente de datos: Sistema o archivo que alimenta una o varias herramientas.
Persona responsable: Dueño o suplente de una herramienta.
Grupo de acceso: Conjunto de personas autorizadas a ver una o varias herramientas.
Programación de actualización: Frecuencia y horario con que se actualiza un reporte, con su historial.

---

## Cómo sabremos que funcionó

SC-001: El 100 % de los reportes con información sensible exigen inicio de sesión; ninguno se abre solo con un enlace, salvo excepciones aprobadas.
SC-002: El 100 % de los reportes se actualiza por programación y muestra la fecha y hora de su última actualización.
SC-003: El 100 % de las 17 herramientas tiene un suplente registrado en 30 días (el dueño, su creador, ya está registrado).
SC-004: Ningún archivo maestro permanece en una cuenta personal.
SC-005: Una actualización fallida se detecta por su dueño en menos de 1 día hábil.
SC-006: Las líneas pendientes de la documentación bajan de 32 a menos de 10.

---

## Lo que damos por cierto y de qué dependemos

### Damos por cierto
- La documentación actual del inventario es la línea base.
- Quienes usan los dashboards (district managers, regional managers, field supervisors y administración) deberían tener correo de la empresa con correo Falcon Farms; se verifica al crear los grupos de acceso.
- Quienes llenan los formularios deberían tener cuenta de la empresa; se verifica antes de limitar el acceso. Hoy no inician sesión.
- Las 5 aplicaciones quedan fuera de esta versión.
- Costo de servir ya se consume por el Portal y su enlace directo puede retirarse, según la responsable del inventario.
- Los archivos de Excel se actualizan según la necesidad, no por programación.
- Los gerentes necesitan acceso a toda la información de sus dashboards.

### Dependemos de
- Aprobación de TI y del administrador de la plataforma de reportes para cambiar la configuración de acceso.
- Dueños de las fuentes externas (Zona DSD, CopCot y otras) para documentar su método y frecuencia.
- Los administradores de cada herramienta para registrar dueño y suplente.

---

## Qué entra y qué no

### Entra
- 8 dashboards, 5 formularios y 4 bases de datos en Excel.
- Acceso, actualización, responsables, fuentes, formularios y glosario.

### No entra
- Las 5 aplicaciones (Tallie, AFS Console, Staffing Request, F.I.T. y Portal).
- Reconstruir los reportes o cambiar la definición de las cifras del negocio.

### Más adelante
- Monitoreo y alertas centralizados.
- Consolidar los archivos mensuales de Unify en una base de datos.

---

## Preguntas y respuestas

| # | Pregunta | Respuesta | Fecha | A qué afecta |
|---|---|---|---|---|
| 1 | ¿Cómo se accede a Costo de servir? | Solo se entra por el Portal, y solo pueden entrar quienes tienen acceso a ese Portal. | 2026-10-12 | FR-001, FR-002 |
| 2 | ¿Quién es el dueño de cada reporte? | Su creador. | 2026-10-12 | FR-009 |
| 3 | ¿Qué reportes se actualizan por programación? | Todos, excepto Performance Audit Walmart y Sprouts Execution Report, que se actualizan a mano. | 2026-10-12 | FR-006 |
| 4 | ¿Quién recibe las respuestas de cada formulario? | Su administrador, que también lo actualiza. | 2026-10-12 | FR-009, FR-016 |
| 5 | ¿Quiénes son los visitantes externos de los dashboards públicos y tienen cuenta de la empresa? | Son district managers, regional managers y field supervisors, que deberían tener correo de la empresa (Falcon Farms), y administración, que también debería tenerlo. Cualquier persona con el enlace puede ver hoy la información. Falta verificar que todos tengan correo de la empresa. | 2026-10-13 | FR-001, US-001 |
| 6 | ¿Hay algún dashboard que deba seguir siendo público de forma deliberada? | No necesariamente públicos; lo que se necesita es que las personas con correo de la empresa tengan acceso. | 2026-10-13 | FR-002 |
| 7 | ¿Deben iniciar sesión las personas que responden los formularios? | Hoy no; quienes los llenan deberían tener correo de la empresa, por verificar. | 2026-10-13 | FR-015, US-005 |
| 8 | ¿Qué enlaces piden inicio de sesión hoy? | Ningún dashboard (salvo Costo de servir, por el Portal) ni formulario: cualquiera que tenga el enlace puede abrirlos. Las bases de datos en Excel, en SharePoint, exigen una cuenta de la empresa y permiso. | 2026-10-13 | Principle 1, FR-001, FR-002 |
| 9 | ¿Se crean grupos de acceso por rol? | No; los roles ya están listados en cada herramienta y el acceso es para las personas con correo de la empresa. | 2026-10-13 | FR-001 |
| 10 | ¿Con qué frecuencia se actualizan los archivos de Excel? | Según la necesidad. | 2026-10-13 | US-004 |
| 11 | ¿Las bases de datos de Excel podrían migrarse a un servidor? | Sí, como sugerencia por seguridad. | 2026-10-13 | FR-013, US-004 |
| 12 | ¿Quién puede publicar en la web? | Quienes tienen acceso a Power BI (Power BI Pro); es un permiso limitado. | 2026-10-13 | FR-002 |
| 13 | ¿Cada persona debe ver solo lo suyo? | No: los gerentes necesitan acceso a toda la información. | 2026-10-13 | FR-004 |

### Preguntas abiertas

- Ninguna: todas las preguntas de aclaración están respondidas.

---

# Plan: cómo se hace: Gobierno de las herramientas MIC: acceso seguro y actualización confiable

## Datos del plan

| Campo | Valor |
|---|---|
| Feature | 001-secure-reliable-mic-tools |
| Date | 2026-10-13 |
| Spec | [spec.md](./spec.md) |
| Constitution | [constitution.md](../../constitution.md) |

---

## Revisión antes de empezar

Antes de avanzar, comprobar que se respetan los principios:

- [ ] Principio 1: Entrar con la cuenta de la empresa: el acceso con cuenta y el retiro de los enlaces públicos están planeados (US-001).
- [ ] Principio 2: Datos en un lugar de la empresa: la lista maestra única y el lugar controlado están planeados (US-004).
- [ ] Principio 3: Información al día: actualización programada, fecha visible y avisos de falla están planeados (US-002A, US-002B).
- [ ] Principio 4: Responsables: dueño y suplente por herramienta están definidos (US-003A, US-003B).
- [ ] Principio 5: Documentar y cambiar con orden: la documentación de 7 temas y el glosario están planeados (US-006).

---

## Cómo encaja todo

### Dónde estamos

Este plan cambia cómo se entra, quién es responsable y dónde viven los datos de las 17 herramientas del inventario MIC. No se programa nada nuevo.

### Cómo viajan los datos

Las fuentes (otros sistemas y los archivos maestros de Excel) alimentan los modelos de datos de los reportes. La gente ve los reportes entrando con su cuenta. Los formularios guardan sus respuestas en un destino definido, y uno de ellos alimenta un dashboard.

### Decisiones sobre herramientas

| Tema | Qué se elige | Por qué |
|---|---|---|
| Acceso desde un solo sitio | Entrar con la cuenta de la empresa (Microsoft) desde un solo sitio de entrada, por ejemplo el Portal, abierto a toda la organización | Quienes usan las herramientas deberían tener cuenta de la empresa y sus roles ya están en cada ficha; no hace falta crear grupos por rol. Costo de servir ya se usa por el Portal, y unificar evita enlaces sueltos. |
| Enlaces públicos | Retirar los enlaces públicos que existen; publicar en la web queda limitado a quienes tienen Power BI Pro | Quienes tienen acceso pueden publicar y retirar enlaces por su cuenta; los enlaces que existen siguen abiertos a cualquiera hasta que se retiren (fuentes de terceros consultadas). |
| Actualización | Actualización programada en Power BI, con aviso al dueño y a su suplente si falla | Quita la actualización a mano y avisa de las fallas. Varios reportes ya tienen una tabla «Last Refresh» que se reutiliza. |
| Bases de datos maestras | Pasar las 4 bases de datos de Excel a un servidor (sugerido), con una sola lista maestra de tiendas | Mejora la seguridad frente a los archivos de Excel y evita cifras distintas entre reportes. |
| Formularios | Formularios a nombre de un grupo, solo para personas de la empresa, con las respuestas guardadas en un lugar de la empresa | El formulario no depende de una persona y las respuestas tienen destino y tiempo de guardado definidos. |
| Registro y documentación | Esta página del inventario como registro, con revisión cada trimestre | Ya tiene la documentación de los 7 temas y la matriz de riesgos. |
| Lista de trabajo | Azure DevOps (organización «FALCON FARMS»; proyecto «Inventario de herramientas») | Se carga con un archivo CSV listo para importar (ver el punto 6); la conexión directa es opcional. |

---

## Cómo se organizan los archivos

```
mic-tools-governance/
├── constitution.md
├── registry/tools.csv
├── docs/                 # one record per tool (7 areas)
├── access/               # sign-in rollout, link retirement, hidden pages
├── refresh/              # schedules, freshness card, failure notices
├── ownership/            # owners, backups, continuity plan
├── data/                 # master files, permissions, single store master
├── forms/                # respondents, responses, backups
├── review/               # integration, success criteria, security
└── glossary.md
```

**Decisión:** Una carpeta de documentos y configuración (sin código), ordenada por tema: acceso, actualización, responsables, datos y formularios.

---

## Fases

### Fases 1 a 6: una por necesidad
Cada fase resuelve una necesidad y se puede entregar sola, en orden de prioridad (ver las tareas).

### Fase final: cierre
Revisión con TI, comprobación de los criterios de éxito y actualización del inventario.

---

## Definiciones para US-003 (resueltas, sin tareas)

- **D-1 Dueño:** El dueño de cada herramienta es su creador (reporte, formulario o archivo), tal como está registrado en el inventario. En los formularios, es quien los administra y recibe las respuestas.
- **D-2 Suplente:** El suplente es una persona del mismo equipo, distinta del dueño, designada por el responsable del área y registrada en el campo «Suplente» de la ficha. Un equipo o departamento no puede ser el suplente ni el único administrador.
- **D-3 Plan de continuidad:** Si cambia el dueño, el creador o la licencia: (1) el suplente asume; (2) se transfiere la propiedad del reporte, formulario o archivo en la plataforma; (3) se actualiza el inventario; (4) se revisan los accesos; (5) se avisa a quien administra la licencia o la capacidad.
- **D-4 Revisión trimestral:** Cada trimestre se revisan la documentación, los dueños y suplentes, los pendientes, los accesos y la programación de actualización. La fecha de cada revisión se anota en el inventario.

---

## Riesgos y cómo evitarlos

| Riesgo | Impacto | Probabilidad | Cómo evitarlo |
|---|---|---|---|
| Visitantes que aún no tienen o no usan una cuenta de la empresa | High | Medium | Verificar la lista de usuarios de cada dashboard (los roles ya están en cada ficha) antes de retirar los enlaces; quien no tenga correo de la empresa se resuelve antes. |
| Quitar el enlace público interrumpe a quien lo usa | Medium | High | Avisar antes, validar el acceso nuevo y retirar el enlace al final, un dashboard a la vez. |
| Falta de acuerdo de TI con el cambio de acceso | High | Medium | Presentarles la matriz de riesgos antes de empezar. |
| Programar la actualización requiere credenciales o puerta de enlace | Medium | Medium | Documentar la fuente de cada modelo y probar la actualización en un reporte antes de generalizar. |
| El dueño o el creador cambia de rol durante el proyecto | Medium | Medium | Registrar suplente desde la Fase 1. |
| Modelos grandes tardan en actualizarse (Last Visit, 331 MB) | Medium | Low | Medir el tiempo de actualización antes de programarlo. |
| Quienes responden los formularios deberán iniciar sesión por primera vez | Medium | Medium | Avisar antes, probar con pocas personas y mantener el mismo enlace. |
| Pasar las bases de Excel a un servidor interrumpe a quien las usa hoy | Medium | Medium | Pasar una base a la vez, avisar antes y conservar el archivo original hasta validar el resultado. |

---

## Qué tan difícil es cada parte

| Parte | Tamaño | Qué tan seguros estamos | Notas |
|---|---|---|---|
| Maestra de tiendas compartida | L | Low | Afecta a los 8 modelos. |
| Retiro de enlaces públicos | S | High | Una vez validado el acceso nuevo. |
| Actualización programada | M | Medium | Según credenciales y tamaño del modelo. |
| Formularios controlados | S | Medium | Cinco formularios, cambio de configuración. |

---

# Tareas: Gobierno de las herramientas MIC: acceso seguro y actualización confiable

## Cómo leer las tareas

- **[P]** = se puede hacer al mismo tiempo que otras
- **[Story: USX]** = a qué necesidad pertenece la tarea
- **[Dep: T-NNN]** = no se puede empezar hasta terminar la tarea T-NNN
- Las rutas de archivos son relativas a la carpeta del proyecto
- Las tareas siguen la estructura del plan
- No se piden pruebas de código; en su lugar hay tareas de revisión

---

## Fase 1: Acceso seguro a los dashboards

Imprescindible.

- [ ] T-001: Pasar los dashboards públicos, uno a la vez, a acceso con cuenta de la empresa desde un solo sitio (por ejemplo el Portal) y retirar los enlaces públicos directos (Costo de servir ya entra por el Portal) [Story: US-001]
  - Se entrega cuando: Cada uno abre solo con cuenta y desde un solo sitio; los enlaces públicos ya no abren sin cuenta (probado en una ventana privada).

- [ ] T-002: Limpiar los dashboards: ocultar las páginas de comentarios libres y eliminar o documentar las 13 páginas ocultas (SPR 1, Walmart Audit 3, Costo de servir 1, Last Visit 5, Costco 3) [P] [Story: US-001]
  - Se entrega cuando: No quedan comentarios libres ni páginas ocultas sin explicación.

---

## Fase 2: Actualización confiable y visible

Imprescindible.

- [ ] T-003: Programar la actualización de Performance Audit Walmart y Sprouts Execution Report, y agregar el visual con la fecha y hora de la última actualización donde falta (Costco Report) [P] [Story: US-002]
  - Se entrega cuando: Los dos se actualizan solos y todos los reportes muestran su fecha y hora de actualización.

- [ ] T-004: Confirmar si las actualizaciones han fallado y activar el aviso de fallas al dueño y su suplente; revisar con el administrador el historial de SPR, Walmart Audit y Costco [Dep: T-003] [Story: US-002]
  - Se entrega cuando: Se sabe si hubo fallas y una falla de prueba avisa a ambos.

---

## Fase 3: Dueño y suplente por herramienta

Sin tareas: se resuelve con las reglas D-1 a D-4 (ver plan) y el campo «Suplente» de cada ficha del inventario.

---

## Fase 4: Bases de datos ordenadas

Importante.

- [ ] T-005: Pasar las 4 bases de datos de Excel a un servidor, con una sola lista maestra de tiendas; revisar permisos, anotar quién las actualiza y cuándo, y sacar los archivos de cuentas personales [Story: US-004]
  - Se entrega cuando: Las bases están en el servidor, muestran su última actualización y quién tiene acceso, y no queda ningún archivo en cuentas personales.

---

## Fase 5: Formularios controlados

Importante.

- [ ] T-006: Limitar los 5 formularios a personas con cuenta de la empresa y definir dónde se guardan las respuestas [P] [Story: US-005]
  - Se entrega cuando: Una cuenta externa no puede responder y cada formulario tiene destino de respuestas.

---

## Fase 6: Definiciones compartidas

Importante.

- [ ] T-007: Crear el glosario de abreviaturas y cifras clave (SL, DL, RTV, AUR, visita efectiva, tienda evaluada, Audit Rating %) [P] [Story: US-006]
  - Se entrega cuando: Cada término tiene una definición escrita.

---

## Fase final: Cierre

Depende de todo lo anterior.

- [ ] T-008: Revisión final con TI: comprobar los criterios de éxito y actualizar la documentación del inventario [Dep: T-001, T-002, T-003, T-004, T-005, T-006, T-007]
  - Se entrega cuando: Los 6 criterios están medidos y los pendientes bajan a menos de 10.

---

## Tareas anteriores

- ~~T-001 a T-026 (v1.7): Tareas de versiones anteriores~~ — Reemplazadas: se juntaron en 8 tareas sin repetidos. Se eliminaron la Fase 0 de preparación y la consulta a TI sobre publicar, y se unieron las que hacían el mismo paso (acceso y enlace único; base de datos y su registro).

## Qué va primero

```
T-001                                  → US-001
T-002 (en paralelo)                    → US-001
T-003 ── T-004                         → US-002A / US-002B
T-005                                  → US-004
T-006                                  → US-005
T-007                                  → US-006
T-001 a T-007 ── T-008                 → cierre
```

## Cómo se cargan a la lista de trabajo

| Task | GitHub Issue Label | Azure DevOps Type | Priority |
|------|--------------------|-------------------|----------|
| T-001..T-002 | `story:US-001` | PBI (under Feature) | P0-P1 |
| T-003..T-004 | `story:US-002` | PBI (under Feature) | P0-P1 |
| T-005 | `story:US-004` | PBI (under Feature) | P1 |
| T-006 | `story:US-005` | PBI (under Feature) | P0 |
| T-007 | `story:US-006` | PBI (under Feature) | P2 |
| T-008 | `phase:integration` | Task (under Feature) | P1 |

---

# Glosario en palabras simples

- **Publicar en la web:** Una opción de Power BI que da un enlace abierto a cualquiera, sin pedir cuenta. Es lo que usan hoy los dashboards públicos. Pueden usarla quienes tienen acceso a Power BI Pro.
- **Portal:** El sitio de la empresa desde el que se entra a Costo de servir. Pide iniciar sesión.
- **Cuenta de la empresa:** El usuario con correo Falcon Farms con el que cada persona entra a los sistemas.
- **Modelo de datos del reporte (modelo semántico):** Donde el reporte guarda y organiza sus datos. Varios reportes pueden usar el mismo.
- **Actualización programada:** El reporte se actualiza solo, a una hora fija, sin que nadie lo haga a mano.
- **DirectQuery (consulta en vivo):** El reporte pregunta los datos a la fuente cada vez que se abre, en vez de guardar una copia.
- **Servidor de base de datos:** Un lugar central y protegido donde viven los datos, mejor que los archivos de Excel sueltos.
- **Dueño y suplente:** El dueño responde por la herramienta; el suplente lo reemplaza si no está. Ambos son personas.
- **Verificado, Inferido, Pendiente, Sugerencia:** Verificado: confirmado. Inferido: deducido, sin confirmar. Pendiente: falta información. Sugerencia: recomendación.
- **Riesgo, prioridad y plazo:** Riesgo: qué tan grave sería. Prioridad: qué atender primero. Plazo: cuándo conviene actuar (Quick win = rápido y fácil).
- **Principios del proyecto (constitución):** Las reglas que no se negocian y que guían todo lo demás.
- **Necesidades de las personas (historias de usuario):** Lo que alguien necesita, escrito como «Como ___, quiero ___, para que ___». Se numeran US-001, US-002...
- **Lo que debe cumplir (requisitos, FR):** Cada punto concreto que se debe lograr. Se numeran FR-001, FR-002...
- **Cómo sabremos que funcionó (criterios, SC):** Metas que se pueden medir. Se numeran SC-001, SC-002...
- **Tareas (T):** Los pasos de trabajo concretos. Se numeran T-001, T-002... y la P significa que se puede hacer a la vez que otra.
- **Lista de trabajo (backlog):** Donde el equipo guarda las tareas pendientes, por ejemplo en Azure DevOps o GitHub.
- **Skill spec-driven-dev:** La herramienta de Claude que ordenó este plan en principios, necesidades, requisitos, plan y tareas.

---

# Plan de acción para cargar la lista de trabajo: 001-secure-reliable-mic-tools

El archivo backlog.csv está listo para importarse en Azure DevOps. No hace falta ninguna conexión.

## Pasos
1. Elegir dónde vive la lista de trabajo: Azure DevOps, en la organización «FALCON FARMS», proyecto «Inventario de herramientas»
   - Quién: Responsable del inventario | Cuándo: Primer día
2. Revisar el tipo de proyecto (Agile, Scrum o Basic) en la configuración del proyecto. El archivo viene hecho para Agile (Epic, Feature, User Story); si es Scrum, se cambia «User Story» por «Product Backlog Item»
   - Quién: Responsable del inventario, con quien administra Azure DevOps | Cuándo: Primer día
3. Importar el archivo backlog.csv: en Azure DevOps, Boards → Queries → Import work items; revisar y guardar. Quedan 1 Epic, 7 Features y 8 tareas, con prioridad y «se entrega cuando»
   - Quién: Responsable del inventario | Cuándo: Primer día
4. Asignar a cada tarea su responsable y su fecha, y ordenar la lista por prioridad. Empezar por las imprescindibles: T-001, T-003 y T-006
   - Quién: Responsable del inventario, con el equipo | Cuándo: Primera semana
5. Cada semana, marcar las tareas terminadas. Si cambia algo de lo que se necesita, primero se actualiza este documento y después la lista
   - Quién: Responsable del inventario | Cuándo: Cada semana
6. Opcional, más adelante: para que Claude cree y actualice las tareas solo, se usa el archivo ado-sync.md con Claude Code. Esa conexión la aprueba TI
   - Quién: Responsable del inventario y TI | Cuándo: Cuando se decida

## Dónde va cada archivo
```
mic-tools-governance/
├── constitution.md
├── glossary.md
└── specs/001-secure-reliable-mic-tools/
    ├── spec.md  plan.md  tasks.md
    ├── research.md  data-model.md
    ├── backlog.csv   (importar en Azure DevOps)
    └── ado-sync.md   (conexión directa, opcional)
```

---
