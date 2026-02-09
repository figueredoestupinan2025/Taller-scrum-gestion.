Taller Scrum - Gestión Integrada (Python)

Resumen
-------
Este repositorio contiene el material del taller: `PROYECTO_GESTION.md`, la aplicación de consola en Python para la lista de tareas (`tarea_app.py` y `tareas_core.py`), pruebas con `pytest` y guías para Git Flow y Conventional Commits.

Requisitos
----------
- Python 3.8+
- pip

Instalación
-----------
```bash
cd "c:\Users\User\Documents\Taller-scrum-gestion"
pip install -r requirements.txt
```

Hooks (una vez por equipo)
--------------------------
Habilita los hooks de commit para validar Conventional Commits:

Bash (Git Bash/WSL):
```bash
./scripts/setup-hooks.sh
```

PowerShell (Windows):
```powershell
.\scripts\setup-hooks.ps1
```

Ejecución
---------
- Iniciar la app (interactiva):
```bash
python tarea_app.py
```

- Ejecutar tests:
```bash
pytest -q
```

Flujo de trabajo recomendado
----------------------------
- Crear rama de feature desde `main` (ej: `feature/rama-historias` o `rama-historias`).
- Realizar commits siguiendo Conventional Commits.
- Push y abrir PR contra `main` usando la plantilla `.github/PULL_REQUEST_TEMPLATE.md`.
- Esperar al menos una aprobación y que CI pase antes de mergear.

Contacto
--------
Scrum Master: José Figueredo
