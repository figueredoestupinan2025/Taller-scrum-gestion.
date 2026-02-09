# 📋 Documento de Gestión Maestro
## Gestión Integrada Scrum + GitHub

**Asignatura:** Desarrollo de Software  
**Duración:** 120 minutos  
**Metodología:** Aprendizaje Basado en Proyectos (ABP)

---

## Sección 1: Planificación (Integrante A - Scrum Master)

### Nombres de los Integrantes y Roles
- **Integrante A (Scrum Master / Facilitador):** [Tu Nombre como Scrum Master]  
- **Integrante B (Product Owner / Analista):** [Nombre del Compañero B]  
- **Integrante C (QA / Developer):** [Nombre del Compañero C]

### Enlace al Tablero de Gestión
[Enlace a Trello o Jira: https://trello.com/b/... o https://jira.com/...]

### Captura de Pantalla del Tablero al Inicio del Sprint
![Captura del Tablero Inicial](imagenes/tablero_inicial.png)  
*(Coloca aquí la captura del tablero con las HU en Backlog, To Do, etc.)*

---

## Sección 2: Historias de Usuario (Integrante B - Product Owner)

### 📝 Aplicación Lista de Tareas (Python)

#### 📌 Descripción del Proyecto
Este proyecto consiste en el desarrollo de una aplicación simple de **Lista de Tareas** en **Python**, ejecutada desde consola.  
El objetivo principal es evidenciar el trabajo técnico y la correcta gestión de **Historias de Usuario**, **trazabilidad** y **uso de Git**, siguiendo una metodología básica de desarrollo ágil.

#### 👤 Product Owner
**Nombre:** Andrés  
**Rol:** Analista de requisitos e Historias de Usuario

#### 🎯 Objetivo del Producto
Permitir a los usuarios:
- Ver una lista de tareas.
- Agregar nuevas tareas.
- Marcar tareas como completadas.
- Eliminar tareas existentes.

#### 📘 Historias de Usuario

##### HU-01: Ver lista de tareas
**Como** usuario  
**Quiero** ver una lista de tareas registradas  
**Para** conocer las tareas pendientes y completadas.

**Criterios de Aceptación:**
- El sistema muestra todas las tareas.
- Cada tarea indica su estado (completada o pendiente).
- Si no hay tareas, se muestra un mensaje informativo.

##### HU-02: Agregar tareas
**Como** usuario  
**Quiero** agregar nuevas tareas mediante un input  
**Para** registrar actividades por realizar.

**Criterios de Aceptación:**
- No se permiten tareas vacías.
- Las tareas se agregan como pendientes.
- El sistema confirma la creación de la tarea.

##### HU-03: Marcar tareas como completadas
**Como** usuario  
**Quiero** marcar tareas como completadas  
**Para** llevar control de las tareas realizadas.

**Criterios de Aceptación:**
- El usuario puede seleccionar una tarea existente.
- La tarea cambia su estado a completada.
- El sistema valida entradas incorrectas.

##### HU-04: Eliminar tareas
**Como** usuario  
**Quiero** eliminar tareas  
**Para** mantener la lista organizada.

**Criterios de Aceptación:**
- El usuario puede eliminar una tarea existente.
- El sistema confirma la eliminación.
- Se valida que el número de tarea sea correcto.

#### 📊 Tabla de Trazabilidad

| ID Historia | Funcionalidad               | Rama de Git      | Estado     |
|------------|-----------------------------|------------------|------------|
| HU-01      | Ver lista de tareas         | rama-historias   | Finalizado |
| HU-02      | Agregar tareas              | rama-historias   | Finalizado |
| HU-03      | Marcar tareas completadas   | rama-historias   | Finalizado |
| HU-04      | Eliminar tareas             | rama-historias   | Finalizado |

#### 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3
- **Control de versiones:** Git y GitHub
- **Entorno:** Consola

---

## Sección 3: Evidencias y Retro (Integrante C - QA/Developer)

### Captura de Pantalla del Historial de Network en GitHub
![Historial de GitHub](imagenes/github_network.png)  
*(Captura del historial de red en GitHub mostrando ramas, commits y merges)*

### Retrospectiva
#### ¿Qué fue lo más difícil de sincronizar?
La sincronización de ramas y merges fue desafiante debido a la necesidad de coordinar cambios entre compañeros. Los conflictos en el documento requerían comunicación constante.

#### ¿Cómo resolvieron los conflictos de código/texto?
Resolvimos conflictos revisando los cambios en GitHub, discutiendo con el equipo y aceptando la versión más actualizada o fusionando manualmente las diferencias.

---

**Fin del Documento de Gestión Maestro**
