# Taller Scrum – Gestión Integrada (Python)

## 📌 Descripción general
Este repositorio contiene el material y el desarrollo del **Taller Scrum – Gestión Integrada**, cuyo objetivo es aplicar buenas prácticas de **Scrum**, **Git Flow** y **Conventional Commits**, junto con el desarrollo de una **aplicación de consola en Python** para la gestión de tareas.

El proyecto incluye documentación, código fuente, pruebas automatizadas y scripts de apoyo para estandarizar el trabajo colaborativo del equipo.

---

## 📂 Contenido del repositorio
- **PROYECTO_GESTION.md**  
  Documento principal del proyecto con el alcance, objetivos y lineamientos del taller.
- **tarea_app.py**  
  Aplicación de consola en Python para la gestión de tareas.
- **tareas_core.py**  
  Lógica principal de negocio de la aplicación.
- **tests/**  
  Pruebas automatizadas implementadas con `pytest`.
- **scripts/**  
  Scripts para configurar hooks de Git.
- **.github/**  
  Plantillas y configuraciones para Pull Requests.

---

## ⚙️ Requisitos
Antes de comenzar, asegúrate de contar con:
- **Python 3.8 o superior**
- **pip**
- **Git**

---

## 🚀 Instalación
Clona el repositorio y luego instala las dependencias:

```bash
cd "C:\Users\User\Documents\Taller-scrum-gestion"
pip install -r requirements.txt
🔗 Configuración de Hooks (una vez por equipo)
Los hooks permiten validar automáticamente los mensajes de commit según Conventional Commits.

Bash (Git Bash / WSL)
bash
Copiar código
./scripts/setup-hooks.sh
PowerShell (Windows)
powershell
Copiar código
.\scripts\setup-hooks.ps1
▶️ Ejecución del proyecto
Iniciar la aplicación (modo interactivo)
bash
Copiar código
python tarea_app.py
Ejecutar pruebas automatizadas
bash
Copiar código
pytest -q
🔄 Flujo de trabajo recomendado
Crear una rama a partir de main:

feature/rama-historias

rama-historias

Realizar commits siguiendo el estándar Conventional Commits.

Hacer push de la rama al repositorio remoto.

Abrir un Pull Request contra main usando la plantilla:

.github/PULL_REQUEST_TEMPLATE.md

Esperar al menos una aprobación y que el pipeline de CI pase correctamente.

Realizar el merge a main.

👤 Contacto
Scrum Master:
José Figueredo

📄 Licencia
Este proyecto es de uso académico y formativo, desarrollado como parte del Taller Scrum – Gestión Integrada.

yaml
Copiar código

---

Si quieres, también puedo:
- Adaptarlo a un **estilo más académico**  
- Ajustarlo a un **estándar empresarial**
- Traducirlo al **inglés**
- Revisarlo según **rubricas universitarias**

Tú dime 👌📘
