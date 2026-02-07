from tareas import (
    mostrar_tareas,
    agregar_tarea,
    completar_tarea,
    eliminar_tarea
)

def mostrar_menu():
    print("""
    --- MENÚ ---
    1.Ver tareas
    2.Agregar tarea
    3.Completar tarea
    4.Eliminar tarea
    5.Salir
    """)

def ejecutar_menu(tareas):
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")