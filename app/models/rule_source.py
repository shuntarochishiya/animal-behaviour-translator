from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class RuleSource(Base):
    __tablename__ = "rule_sources"

    rule_id: Mapped[int] = mapped_column(
        ForeignKey(
            "interpretation_rules.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    source_id: Mapped[int] = mapped_column(
        ForeignKey(
            "sources.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
