# 🏗️ Taller Scrum - Gestión Integrada (Python)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/figueredoestupinan2025/Taller-scrum-gestion)](https://github.com/figueredoestupinan2025/Taller-scrum-gestion/issues)

Una aplicación de consola en Python para la gestión de tareas, desarrollada siguiendo metodologías ágiles Scrum. Incluye pruebas automatizadas, control de versiones con Git Flow y Conventional Commits.

## 📋 Descripción del Proyecto

Este repositorio contiene el material completo del taller de desarrollo de software, incluyendo:
- Documentación del proyecto (`PROYECTO_GESTION.md`)
- Aplicación de consola para gestión de tareas (`tarea_app.py` y `tareas_core.py`)
- Suite de pruebas con `pytest`
- Guías para Git Flow y Conventional Commits
- Configuración de hooks de pre-commit

El proyecto demuestra la implementación práctica de un sistema de gestión de tareas con las siguientes funcionalidades:
- ✅ Visualización de lista de tareas
- ➕ Agregado de nuevas tareas
- ✅ Marcado de tareas como completadas
- 🗑️ Eliminación de tareas

## 🎯 Objetivos

- Evidenciar el trabajo técnico en desarrollo de software
- Demostrar gestión adecuada de Historias de Usuario
- Implementar trazabilidad completa
- Utilizar Git de manera profesional con Git Flow
- Seguir metodologías ágiles Scrum

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.8+
- **Framework de Pruebas:** pytest
- **Control de Versiones:** Git + GitHub
- **Metodología:** Scrum
- **Convenciones:** Conventional Commits

## 📋 Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/figueredoestupinan2025/Taller-scrum-gestion.git
cd Taller-scrum-gestion
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. (Opcional) Configura los hooks de pre-commit:
   - **Bash (Git Bash/WSL):**
     ```bash
     ./scripts/setup-hooks.sh
     ```
   - **PowerShell (Windows):**
     ```powershell
     .\scripts\setup-hooks.ps1
     ```

## 📖 Uso

### Ejecutar la Aplicación
```bash
python tarea_app.py
```

La aplicación es interactiva y te guiará a través de las opciones disponibles.

### Ejecutar Pruebas
```bash
pytest -q
```

Para ver reportes detallados:
```bash
pytest -v
```

## 📁 Estructura del Proyecto

```
Taller-scrum-gestion/
├── PROYECTO_GESTION.md      # Documentación del proyecto y gestión Scrum
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias del proyecto
├── tarea_app.py             # Aplicación principal (interfaz de usuario)
├── tareas_core.py           # Lógica de negocio
├── tareas.json              # Almacenamiento de datos (JSON)
├── TODO.md                  # Lista de tareas pendientes
├── tests/                   # Directorio de pruebas
│   ├── __init__.py
│   └── test_tareas_core.py
├── imagenes/                # Capturas de pantalla y evidencias
└── scripts/                 # Scripts de configuración
```

## 🔄 Flujo de Trabajo Recomendado

1. **Crear rama de feature** desde `main`:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

2. **Realizar commits** siguiendo Conventional Commits:
   ```bash
   git commit -m "feat: agregar nueva funcionalidad"
   ```

3. **Push y crear Pull Request**:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
   Usa la plantilla `.github/PULL_REQUEST_TEMPLATE.md`

4. **Revisión y merge**: Esperar al menos una aprobación y que las pruebas CI pasen.

## 🤝 Contribución

1. Fork el proyecto
2. Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Convenciones

- **Commits:** Seguir [Conventional Commits](https://www.conventionalcommits.org/)
- **Ramas:** Usar Git Flow (main, develop, feature/*, hotfix/*)
- **Código:** Seguir PEP 8 para Python

## 👥 Equipo

- **Scrum Master:** José Figueredo
- **Product Owner:** Andrés Molina
- **QA/Developer:** José Solano

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

- **Scrum Master:** José Figueredo
- **Proyecto:** [GitHub Repository](https://github.com/figueredoestupinan2025/Taller-scrum-gestion)

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella en GitHub!
