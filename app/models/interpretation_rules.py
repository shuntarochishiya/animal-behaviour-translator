from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.db import Base

if TYPE_CHECKING:
    from app.models.species import Species


class InterpretationRule(Base):
    __tablename__ = "interpretation_rules"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    species_id: Mapped[int] = mapped_column(
        ForeignKey("species.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    primary_signal_slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    context_slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    supporting_signals: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
    )

    interpretation_label: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    interpretation_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    evidence_level: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    evidence_basis: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    limitations: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    species: Mapped["Species"] = relationship()
