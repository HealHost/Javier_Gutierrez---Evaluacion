from conexion import SessionLocal
from modelos import Libro


def eliminar_libro(libro_id):
    with SessionLocal() as session:
        libro = session.get(Libro, libro_id)

        if libro is None:
            print("No existe un libro con ese ID.")
            return

        session.delete(libro)
        session.commit()

        print("Libro eliminado correctamente.")