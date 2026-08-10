from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class Species(Base):
    __tablename__ = "species"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    common_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    scientific_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
