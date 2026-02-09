"""CLI para la aplicación Lista de Tareas usando TaskManager.

Cumple HU-01..HU-04. Guarda en `tareas.json` por defecto.
"""
from tareas_core import TaskManager


def mostrar_tareas(tm: TaskManager):
    tasks = tm.list_tasks()
    if not tasks:
        print("No hay tareas registradas.")
        return
    print("\nLista de Tareas:")
    for t in tasks:
        estado = "[Completada]" if t.get('completada') else "[Pendiente]"
        print(f"{t['id']}. {t['descripcion']} {estado}")


def menu_principal():
    tm = TaskManager('tareas.json')
    while True:
        print("\n--- Menú de Lista de Tareas ---")
        print("1. Ver lista de tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Eliminar completadas")
        print("6. Exportar JSON")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ").strip()
        if opcion == '1':
            mostrar_tareas(tm)
        elif opcion == '2':
            descripcion = input("Ingrese la descripción de la nueva tarea: ").strip()
            try:
                tm.add_task(descripcion)
                print("Tarea agregada exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == '3':
            mostrar_tareas(tm)
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a marcar como completada: "))
                if tm.complete_task(id_tarea):
                    print("Tarea marcada como completada.")
                else:
                    print("ID de tarea no válido.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
        elif opcion == '4':
            mostrar_tareas(tm)
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
                if tm.delete_task(id_tarea):
                    print("Tarea eliminada exitosamente.")
                else:
                    print("ID de tarea no válido.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
        elif opcion == '5':
            removed = tm.clear_completed()
            print(f"Se eliminaron {removed} tareas completadas.")
        elif opcion == '6':
            print(tm.export_json())
        elif opcion == '7':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == '__main__':
    menu_principal()
