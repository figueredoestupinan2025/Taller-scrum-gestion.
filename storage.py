import json
import os

ARCHIVO = "tareas.json"

def cargar_tareas():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)
    tareas
from storage import guardar_tareas

def mostrar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return

    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. [{estado}] {tarea['nombre']}")

def agregar_tarea(tareas):
    nombre = input("\nEscribe la nueva tarea: ").strip()
    if nombre:
        tareas.append({
            "nombre": nombre,
            "completada": False
        })
        guardar_tareas(tareas)
        print("Tarea agregada y guardada.")
    else:
        print("La tarea no puede estar vacía.")

def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        num = int(input("\nNúmero de tarea a completar: "))
        tareas[num - 1]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.")
    except (ValueError, IndexError):
        print("Número inválido.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        num = int(input("\nNúmero de tarea a eliminar: "))
        tareas.pop(num - 1)
        guardar_tareas(tareas)
        print("Tarea eliminada.")
    except (ValueError, IndexError):
        print("Número inválido.")