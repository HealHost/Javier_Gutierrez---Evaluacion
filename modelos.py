from sqlalchemy import String, Integer, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass
#

class Libro(Base):
    __tablename__ = "libro"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    autor: Mapped[str] = mapped_column(String(100), nullable=False)
    ejemplares: Mapped[str] = Mapped(Integer, CheckConstraint("disponible >= 0"))


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), nullable=False)


class Prestamo(Base):
    __tablename__ = "prestamo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, CheckConstraint("cantidad > 0"))
    libro_id: Mapped[int] = mapped_column(ForeignKey("libro.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
