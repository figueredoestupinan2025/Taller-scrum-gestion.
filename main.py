from storage import cargar_tareas
from menu import ejecutar_menu

def main():
    tareas = cargar_tareas()
    ejecutar_menu(tareas)

if __name__ == "__main__":
    main()