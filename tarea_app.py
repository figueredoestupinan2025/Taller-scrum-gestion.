# Aplicación Lista de Tareas en Python
# HU-01: Ver lista de tareas
# HU-02: Agregar tareas
# HU-03: Marcar tareas como completadas
# HU-04: Eliminar tareas

tareas = []  # Lista de diccionarios: {'id': int, 'descripcion': str, 'completada': bool}
id_counter = 1  # Contador para IDs únicos

def mostrar_tareas():
    """Muestra todas las tareas con su estado."""
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\nLista de Tareas:")
    for tarea in tareas:
        estado = "[Completada]" if tarea['completada'] else "[Pendiente]"
        print(f"{tarea['id']}. {tarea['descripcion']} {estado}")

def agregar_tarea():
    """Agrega una nueva tarea."""
    descripcion = input("Ingrese la descripción de la nueva tarea: ").strip()
    if not descripcion:
        print("Error: La tarea no puede estar vacía.")
        return
    global id_counter
    tareas.append({'id': id_counter, 'descripcion': descripcion, 'completada': False})
    id_counter += 1
    print("Tarea agregada exitosamente.")

def completar_tarea():
    """Marca una tarea como completada."""
    mostrar_tareas()
    if not tareas:
        return
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a marcar como completada: "))
        tarea = next((t for t in tareas if t['id'] == id_tarea), None)
        if tarea:
            if tarea['completada']:
                print("La tarea ya está completada.")
            else:
                tarea['completada'] = True
                print("Tarea marcada como completada.")
        else:
            print("ID de tarea no válido.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")

def eliminar_tarea():
    """Elimina una tarea."""
    mostrar_tareas()
    if not tareas:
        return
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        tarea = next((t for t in tareas if t['id'] == id_tarea), None)
        if tarea:
            tareas.remove(tarea)
            print("Tarea eliminada exitosamente.")
        else:
            print("ID de tarea no válido.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")

def menu_principal():
    """Bucle principal del menú."""
    while True:
        print("\n--- Menú de Lista de Tareas ---")
        print("1. Ver lista de tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()
        if opcion == '1':
            mostrar_tareas()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            completar_tarea()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
