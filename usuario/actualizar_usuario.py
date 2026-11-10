from sqlalchemy import select
from conexion import SessionLocal
from modelos import Usuario


def actualizar_usuario(usuario_id):
    with SessionLocal() as session:
        usuario = session.get(Usuario, usuario_id)

        if usuario is None:
            print("No existe un usuario con ese ID.")
            return

        nombre = input(f"Nuevo nombre [{usuario.nombre}]: ").strip()
        correo = input(f"Nuevo correo [{usuario.correo}]: ").strip()

        if len(nombre) > 100 or len(correo) > 100:
            print("El nombre y el correo deben tener máximo 100 caracteres.")
            return

        if nombre:
            usuario.nombre = nombre

        if correo and correo != usuario.correo:
            existe = session.scalars(
                select(Usuario).where(Usuario.correo == correo)
            ).first()

            if existe:
                print("Ya existe un usuario con ese correo.")
                return

            usuario.correo = correo

        session.commit()
        print("Usuario actualizado correctamente.")