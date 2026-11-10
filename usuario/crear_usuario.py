from sqlalchemy import select
from conexion import SessionLocal
from modelos import Usuario


def crear_usuario():
    print("\n--- REGISTRAR USUARIO ---")

    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    if not nombre or not correo:
        print("El nombre y el correo son obligatorios.")
        return

    if len(nombre) > 100 or len(correo) > 100:
        print("El nombre y el correo deben tener máximo 100 caracteres.")
        return

    with SessionLocal() as session:
        existe = session.scalars(
            select(Usuario).where(Usuario.correo == correo)
        ).first()

        if existe:
            print("Ya existe un usuario con ese correo.")
            return

        usuario = Usuario(nombre=nombre, correo=correo)
        session.add(usuario)
        session.commit()

        print(f"Usuario registrado. ID: {usuario.id}")