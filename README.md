🧩 Taller Scrum – Gestión Integrada
Aplicación de Consola para Gestión de Tareas en Python
1. Descripción General

El presente repositorio contiene el desarrollo del proyecto Taller Scrum – Gestión Integrada, una iniciativa académica orientada a la aplicación práctica de los principios, roles, eventos y artefactos del marco de trabajo Scrum, integrados con buenas prácticas de ingeniería de software, control de versiones, trabajo colaborativo y aseguramiento de la calidad.

El proyecto materializa estos conceptos mediante la construcción de una aplicación de consola desarrollada en Python, cuyo propósito es permitir la gestión básica de tareas (creación, consulta, actualización y eliminación), sirviendo como escenario para simular un entorno real de desarrollo ágil.

Adicionalmente, el repositorio incorpora documentación técnica, lineamientos de colaboración, pruebas automatizadas y convenciones de versionado que fortalecen la trazabilidad y la mantenibilidad del sistema.

2. Propósito del Proyecto

Este proyecto tiene como finalidad fortalecer las competencias del estudiante en:

Aplicación práctica de metodologías ágiles, particularmente Scrum.

Implementación de soluciones utilizando Python.

Uso profesional de Git y flujos de trabajo colaborativos.

Implementación de estándares de calidad en el desarrollo de software.

Elaboración de documentación técnica clara y estructurada.

3. Objetivos
3.1 Objetivo General

Desarrollar una aplicación de consola en Python para la gestión de tareas, aplicando el marco de trabajo Scrum y buenas prácticas de ingeniería de software.

3.2 Objetivos Específicos

Implementar una arquitectura modular y mantenible.

Aplicar el flujo de trabajo Git Flow.

Utilizar el estándar Conventional Commits.

Diseñar e implementar pruebas automatizadas.

Documentar adecuadamente el proyecto.

Simular un entorno real de trabajo colaborativo.

4. Alcance

La aplicación permitirá:

Registrar nuevas tareas.

Listar tareas existentes.

Actualizar información de tareas.

Eliminar tareas.

Persistir información durante la ejecución.

No se incluye interfaz gráfica ni persistencia en base de datos; el enfoque está orientado al aprendizaje del flujo de desarrollo ágil.

5. Tecnologías Utilizadas

Lenguaje: Python 3

Control de versiones: Git

Gestor de dependencias: pip

Framework de pruebas: pytest

Sistema operativo: Multiplataforma

6. Arquitectura General

El proyecto sigue una arquitectura modular:

Capa de presentación → tarea_app.py

Capa de lógica de negocio → tareas_core.py

Capa de pruebas → carpeta tests/

Este enfoque facilita la escalabilidad, el mantenimiento y las pruebas.

7. Estructura del Repositorio
Taller-scrum-gestion/
│
├── PROYECTO_GESTION.md
├── tarea_app.py
├── tareas_core.py
├── requirements.txt
│
├── tests/
│   └── test_tareas.py
│
├── scripts/
│   ├── setup-hooks.sh
│   └── setup-hooks.ps1
│
└── .github/
    └── PULL_REQUEST_TEMPLATE.md

8. Requisitos del Sistema

Python 3.8 o superior

pip

Git

Conexión a internet para instalación inicial

9. Instalación

Clonar el repositorio:

git clone https://github.com/figueredoestupinan2025/Taller-scrum-gestion.git


Ingresar al directorio:

cd Taller-scrum-gestion


Instalar dependencias:

pip install -r requirements.txt

10. Configuración de Hooks de Git
Bash
./scripts/setup-hooks.sh

PowerShell
.\scripts\setup-hooks.ps1


Estos hooks validan los mensajes de commit según Conventional Commits.

11. Ejecución
Aplicación
python tarea_app.py

Pruebas
pytest -q

12. Flujo de Trabajo (Git Flow)

Crear rama:

feature/nombre-funcionalidad


Desarrollar funcionalidad.

Realizar commits con Conventional Commits.

Push al repositorio.

Crear Pull Request a main.

Esperar aprobación.

Realizar merge.

13. Convención de Commits

Ejemplo:

feat: agregar creación de tareas
fix: corregir validación de entrada
docs: actualizar README
test: agregar pruebas de eliminación

14. Gestión Scrum

Product Backlog

Sprint Backlog

Daily Scrum (simulado)

Sprint Review

Sprint Retrospective

15. Roles

Scrum Master: José Figueredo

Desarrollador: José Figueredo

16. Calidad del Software

Pruebas automatizadas

Código modular

Convenciones de estilo

Revisión mediante Pull Requests

17. Consideraciones Finales

Este proyecto es de carácter académico y demuestra la aplicación integrada de metodologías ágiles y desarrollo de software, sentando bases sólidas para proyectos de mayor complejidad.

18. Licencia

Proyecto de uso académico.
Todos los derechos reservados para fines educativos.
