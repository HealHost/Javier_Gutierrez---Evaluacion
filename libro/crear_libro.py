from conexion import SessionLocal
from modelos import Libro

def crear_libro():
    print("\n--- REGISTRAR LIBRO ---")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()


    if not titulo or not autor:
        print("El título y el autor son obligatorios.")
        return

    if len(titulo) > 100 or len(autor) > 100:
        print("El título y el autor deben tener máximo 100 caracteres.")
        return

    try:
        disponibles = int(input("Ejemplares disponibles: "))

        if disponibles < 0:
            print("Los ejemplares no pueden ser negativos.")
            return

    except ValueError:
        print("Debe ingresar números enteros válidos.")
        return

    with SessionLocal() as session:
        libro = Libro(
            titulo=titulo,
            autor=autor,
            disponibles=disponibles
        )

        session.add(libro)
        session.commit()

        print(f"Libro registrado. ID: {libro.id}")