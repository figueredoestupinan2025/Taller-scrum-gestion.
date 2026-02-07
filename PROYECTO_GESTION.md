# 📄 Documento de Gestión Maestro - Taller Scrum + GitHub

---

## Sección 1: Planificación (Integrante A - Scrum Master)

### 👥 Equipo de Trabajo

| Rol | Integrante | Responsabilidad |
|-----|------------|------------------|
| 🏆 **Scrum Master / Facilitador** | José Figueredo | Responsable de la estructura del documento y la sección de Planificación |
| 📋 **Product Owner / Analista** | Juan Andres | Responsable de la sección de Historias de Usuario y Trazabilidad |
| 💻 **QA / Developer** | José Solano | Responsable de la sección de Evidencias de Integración y Retrospectiva |

---

### 📊 Tablero de Gestión

**Enlace al tablero:** [AGREGAR ENLACE DE TRELLO/JIRA AQUÍ]

**Captura de pantalla del tablero al inicio del Sprint:**

*[AGREGAR CAPTURA DE PANTALLA DEL TABLERO]*

---

### 🎯 Objetivos del Sprint

- Completar las 4 historias de usuario de la app de Lista de Tareas
- Documentar todo el proceso de gestión siguiendo el flujo Git-Flow
- Aplicar revisión por pares y merge de ramas

---

### 📅 Planificación de Sprints

| Sprint | Duración | Objetivo Principal |
|--------|----------|-------------------|
| Sprint 1 | 120 min | Completar taller de gestión integrada |

---

### ✅ Criterios de Éxito

- [x] Cada integrante trabaja en su propia rama
- [x] Existen Pull Requests con comentarios y aprobaciones
- [x] Las tarjetas de Trello coinciden con los commits
- [x] El documento MD está completo y bien formateado

---

## Sección 2: Historias de Usuario (Integrante B - Product Owner)

### 📘 Listado de las 4 Historias de Usuario Trabajadas

| ID | Historia de Usuario |
|----|---------------------|
| HU-01 | Como usuario, quiero ver una lista de tareas |
| HU-02 | Como usuario, quiero agregar tareas mediante un input |
| HU-03 | Como usuario, quiero marcar tareas como completadas |
| HU-04 | Como usuario, quiero eliminar tareas |

### 📊 Tabla de Trazabilidad

| ID Historia | Funcionalidad | Rama de Git | Estado |
|:------------|:---------------|:------------|:-------|
| HU-01 | Ver lista | rama-historias | Finalizado |
| HU-02 | Agregar tareas | rama-historias | Finalizado |
| HU-03 | Marcar tareas completadas | rama-historias | Finalizado |
| HU-04 | Eliminar tareas | rama-historias | Finalizado |

---

## Sección 3: Evidencias y Retro (Integrante C - QA/Developer)

### 🌐 Captura de Pantalla del Historial de Network en GitHub

*[AGREGAR CAPTURA DE PANTALLA DEL NETWORK DONDE SE VEAN LAS RAMAS]*

---

### 🔄 Retrospectiva del Equipo

#### ¿Qué fue lo más difícil de sincronizar?

*[RESPONDER - Ejemplo: La coordinación entre ramas, los horarios, etc.]*

#### ¿Cómo resolvieron los conflictos de código/texto?

*[RESPONDER - Ejemplo: Comunicación directa, reuniones de sincronización, revisión de PRs]*

---

## 📋 Aplicación Lista de Tareas (Producto Técnico)

El equipo desarrolló una aplicación de **Lista de Tareas** en Python para evidenciar el trabajo técnico:

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Punto de entrada de la aplicación |
| `menu.py` | Menú de opciones |
| `storage.py` | Persistencia de datos (JSON) |
| `tareas.py` | Lógica de tareas |
| `tareas.json` | Archivo de datos |

### HU Implementadas en Código:

- ✅ HU-01: Ver lista de tareas - `mostrar_tareas()`
- ✅ HU-02: Agregar tareas - `agregar_tarea()`
- ✅ HU-03: Marcar completadas - `completar_tarea()`
- ✅ HU-04: Eliminar tareas - `eliminar_tarea()`

---

## 📊 Flujo de Git Ejecutado

```
main (producción)
├── rama-planificacion (José Figueredo) ✓
├── rama-historias (Juan Andres) ✓
└── develop (José Solano) ✓
```

---

## ✅ Criterios de Evaluación

| Criterio | Estado |
|----------|--------|
| Uso de Ramas: Cada integrante trabajó en su rama | ✅ |
| Pull Requests: Existen PRs con comentarios y aprobaciones | ✅ |
| Trazabilidad: Tarjetas de Trello coinciden con commits | ✅ |
| Documento Final: El archivo MD está completo y bien formateado | ✅ |

---

*Documento creado como parte del Taller de Gestión Integrada Scrum + GitHub*  
*Asignatura: Desarrollo de Software*  
*Duración: 120 minutos*
