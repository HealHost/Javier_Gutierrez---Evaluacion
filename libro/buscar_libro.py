from sqlalchemy import select
from conexion import SessionLocal
from modelos import Libro


def mostrar_libro(libro):
    print(
        f"ID: {libro.id} | "
        f"Título: {libro.titulo} | "
        f"Autor: {libro.autor} | "
        f"Disponibles: {libro.disponibles}"
    )


def consultar_libros():
    with SessionLocal() as session:
        libros = session.scalars(select(Libro)).all()

        if not libros:
            print("No hay libros registrados.")
            return

        print("\n--- LISTADO DE LIBROS ---")

        for libro in libros:
            mostrar_libro(libro)


def buscar_libro_por_id(libro_id):
    with SessionLocal() as session:
        libro = session.get(Libro, libro_id)

        if libro is None:
            print("No existe un libro con ese ID.")
            return

        mostrar_libro(libro)
