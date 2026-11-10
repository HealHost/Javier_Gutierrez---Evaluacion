#lista usuarios y tambien los busca po el ID
from sqlalchemy import select
from conexion import SessionLocal
from modelos import Usuario


def mostrar_usuario(usuario):
    print(
        f"ID: {usuario.id} | "
        f"Nombre: {usuario.nombre} | "
        f"Correo: {usuario.correo}"
    )


def consultar_usuario():
    with SessionLocal() as session:
        usuarios = session.scalars(select(Usuario)).all()

        if not usuarios:
            print("No hay usuario registrados.")
            return

        print("\n--- LISTADO DE USUARIO ---")

        for usuario in usuarios:
            mostrar_usuario(usuario)


def buscar_usuario_por_id(usuario_id):
    with SessionLocal() as session:
        usuario = session.get(Usuario, usuario_id)

        if usuario is None:
            print("No existe un usuario con ese ID.")
            return

        mostrar_usuario(usuario)
