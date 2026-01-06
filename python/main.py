from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():

    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir tarea")
    print("2. Añadir tarea compleja (con IA)")
    print("3. Listar tareas")
    print("4. Completar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")
    print("   ----------   ")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:
            choise = int(input("\nElige una opción: "))

            match choise:
                case 1:
                    description = input("Descripción de la tarea: ")
                    manager.add_task(description)

                case 2:
                    description = input("Descripción de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        manager.add_task(subtask)

                case 3:
                    manager.list_tasks()

                case 4:
                    id = int(input("Ingresa el identificador de la tarea: "))
                    manager.complete_task(id)

                case 5:
                    id = int(input("Ingresa el identificador de la tarea: "))
                    manager.remove_task(id)

                case 6:
                    print("\nSaliendo...")
                    break

                case _:
                    print("Opción no valida. Selecciona otra.")

        except ValueError:
            print("Opción no valida. Selecciona otra.")

if __name__ == "__main__":
    main()