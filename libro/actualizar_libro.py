from conexion import SessionLocal
from modelos import Libro


def actualizar_libro(libro_id):
    with SessionLocal() as session:
        libro = session.get(Libro, libro_id)

        if libro is None:
            print("No existe un libro con ese ID.")
            return

        titulo = input(f"Nuevo título [{libro.titulo}]: ").strip()
        autor = input(f"Nuevo autor [{libro.autor}]: ").strip()
        disponibles = input(f"Ejemplares disponibles [{libro.disponibles}]: ").strip()

        if titulo:
            if len(titulo) > 100:
                print("El título no puede superar los 100 caracteres.")
                return
            libro.titulo = titulo

        if autor:
            if len(autor) > 100:
                print("El autor no puede superar los 100 caracteres.")
                return
            libro.autor = autor

        session.commit()
        print("Libro actualizado correctamente.")
