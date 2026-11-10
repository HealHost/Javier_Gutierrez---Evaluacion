from conexion import engine
from modelos import Base

def crear_tablas():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    crear_tablas()
    print("Tablas creadas correctamente.")